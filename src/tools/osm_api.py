import time

import overpy


class OSMQuery:
    header = """
        [out:json][timeout:60];
        node["name"="{name}"]["place"]({s},{w},{n},{e});
        (
        """
    header_vast = """
        [out:json][timeout:60];
        (
            node["name"="{name}"]["place"]({s},{w},{n},{e}) -> .city_n;
            way["name"="{name}"]["place"]({s},{w},{n},{e}) -> .city_w;
            relation["name"="{name}"]["place"]({s},{w},{n},{e}) -> .city_r;
        );
        (
        """
    fin = """
        );
        out body;
        >;
        out skel qt;
        """

    historic = """
        node(around:{radius})["historic"] -> .historic_n;
        way(around:{radius})["historic"] -> .historic_w;
        relation(around:{radius})["historic"] -> .historic_r;
        """
    leisure = """
        node(around:{radius})["leisure"] -> .leisure_n;
        way(around:{radius})["leisure"] -> .leisure_w;
        relation(around:{radius})["leisure"] -> .leisure_r;
        """
    tourism = """
        node(around:{radius})["tourism"] -> .tourism_n;
        way(around:{radius})["tourism"] -> .tourism_w;
        relation(around:{radius})["tourism"] -> .tourism_r;
        """
    hotel = """
        node(around:{radius})["building"="hotel"] -> .hotel_n;
        way(around:{radius})["building"="hotel"] -> .hotel_w;
        relation(around:{radius})["building"="hotel"] -> .hotel_r;
        """
    aerodrome = """
        node(around:{radius_x_2})["aeroway"="aerodrome"] -> .aerodrome_n;
        way(around:{radius_x_2})["aeroway"="aerodrome"] -> .aerodrome_w;
        relation(around:{radius_x_2})["aeroway"="aerodrome"] -> .aerodrome_r;
        """
    tag_keys_types = ['historic', 'leisure', 'tourism', 'building', 'aeroway']


class OSM:
    def __init__(self):
        self._api = overpy.Overpass()

    def get_pois(self, city_name: str, lat_lng: {float, float}, radius: int):
        query = (OSMQuery.header
                 + OSMQuery.historic
                 + OSMQuery.leisure
                 + OSMQuery.tourism
                 + OSMQuery.hotel
                 + OSMQuery.aerodrome
                 + OSMQuery.fin).format(name=city_name,
                                        n=lat_lng['lat'] + 1.0,
                                        s=lat_lng['lat'] - 1.0,
                                        w=lat_lng['lng'] - 1.0,
                                        e=lat_lng['lng'] + 1.0,
                                        radius=radius,
                                        radius_x_2=radius * 2)
        while True:
            try:
                query_result = self._api.query(query)
                result = OSM._process_query_result(query_result)
                if len(result) == 0:
                    break
                return result
            except overpy.exception.OverpassTooManyRequests:
                print("Exception handled by API: OverpassTooManyRequests")
                time.sleep(20)

        return self._get_pois_low_memory(city_name, lat_lng, radius)

    @staticmethod
    def _process_query_result(query_result):
        pois = []
        pois += OSM._process_query_result_parser(query_result.nodes)
        pois += OSM._process_query_result_parser(query_result.ways)
        pois += OSM._process_query_result_parser(query_result.relations)
        return pois

    @staticmethod
    def _process_query_result_parser(records):
        pois = []
        for record in records:
            record_id = record.id
            tags = record.tags

            name = ''
            if 'name' in tags.keys():
                name = tags['name']

            for key in OSMQuery.tag_keys_types:
                if key in tags.keys():
                    value = tags[key]
                    poi = {'id': record_id,
                           'name': name,
                           'type': key,
                           'value': value}
                    pois.append(poi)
                    break
        return pois

    def _get_pois_low_memory(self, city_name: str, lat_lng: {float, float}, radius: int):
        queries = self._build_low_memory_queries_poi_cnt_for_city(city_name, lat_lng, radius)
        pois = []
        for q in queries:
            while True:
                try:
                    r = self._api.query(q)
                    pois += OSM._process_query_result(r)
                except overpy.exception.OverpassTooManyRequests:
                    print("Exception handled by API: OverpassTooManyRequests")
                    time.sleep(20)
                    continue
                except overpy.exception.OverpassBadRequest:
                    print("Exception occurred: OverpassBadRequest")
                except overpy.exception.OverpassUnknownHTTPStatusCode:
                    print("Exception occurred: OverpassUnknownHTTPStatusCode")
                break
        return pois

    @staticmethod
    def _build_low_memory_queries_poi_cnt_for_city(name: str, lat_lng: {float, float}, radius: int):
        queries = [OSMQuery.header_vast + OSMQuery.historic + OSMQuery.fin,
                   OSMQuery.header_vast + OSMQuery.leisure + OSMQuery.fin,
                   OSMQuery.header_vast + OSMQuery.tourism + OSMQuery.fin,
                   OSMQuery.header_vast + OSMQuery.hotel + OSMQuery.fin,
                   OSMQuery.header_vast + OSMQuery.aerodrome + OSMQuery.fin]
        formatted_queries = []
        for q in queries:
            fq = q.format(name=name,
                          n=lat_lng['lat'] + 1.0,
                          s=lat_lng['lat'] - 1.0,
                          w=lat_lng['lng'] - 1.0,
                          e=lat_lng['lng'] + 1.0,
                          radius=radius,
                          radius_x_2=radius * 2)
            formatted_queries.append(fq)
        return formatted_queries
