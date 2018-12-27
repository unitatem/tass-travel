import time

import overpy


class OSM:
    def __init__(self):
        self._api = overpy.Overpass()

        self._query_header = """
        [out:json][timeout:60];
        node["name"="{name}"]["place"]({s},{w},{n},{e});
        (
        """
        self._query_header_vast = """
        [out:json][timeout:60];
        (
            node["name"="{name}"]["place"]({s},{w},{n},{e}) -> .city_n;
            way["name"="{name}"]["place"]({s},{w},{n},{e}) -> .city_w;
            relation["name"="{name}"]["place"]({s},{w},{n},{e}) -> .city_r;
        );
        (
        """
        self._query_historic = """
        node(around:{radius})["historic"] -> .historic_n;
        way(around:{radius})["historic"] -> .historic_w;
        relation(around:{radius})["historic"] -> .historic_r;
        """
        self._query_leisure = """
        node(around:{radius})["leisure"] -> .leisure_n;
        way(around:{radius})["leisure"] -> .leisure_w;
        relation(around:{radius})["leisure"] -> .leisure_r;
        """

        self._query_tourism = """
        node(around:{radius})["tourism"] -> .tourism_n;
        way(around:{radius})["tourism"] -> .tourism_w;
        relation(around:{radius})["tourism"] -> .tourism_r;
        """
        self._query_hotel = """
        node(around:{radius})["building"="hotel"] -> .hotel_n;
        way(around:{radius})["building"="hotel"] -> .hotel_w;
        relation(around:{radius})["building"="hotel"] -> .hotel_r;
        """

        self._query_aerodrome = """
        node(around:{radius_x_2})["aeroway"="aerodrome"] -> .aerodrome_n;
        way(around:{radius_x_2})["aeroway"="aerodrome"] -> .aerodrome_w;
        relation(around:{radius_x_2})["aeroway"="aerodrome"] -> .aerodrome_r;
        """
        self._query_fin = """
        );
        out body;
        >;
        out skel qt;
        """

    def get_poi_cnt_for_city(self, name: str, lat_lng: {float, float}, radius: int):
        query = (self._query_header
                 + self._query_historic
                 + self._query_leisure
                 + self._query_tourism
                 + self._query_hotel
                 + self._query_aerodrome
                 + self._query_fin).format(name=name,
                                           n=lat_lng['lat'] + 1.0,
                                           s=lat_lng['lat'] - 1.0,
                                           w=lat_lng['lng'] - 1.0,
                                           e=lat_lng['lng'] + 1.0,
                                           radius=radius,
                                           radius_x_2=radius * 2)
        while True:
            try:
                result = self._api.query(query)
                cnt = OSM._count_results(result)
                if cnt == 0:
                    break
                return cnt
            except overpy.exception.OverpassTooManyRequests:
                print("Exception handled by API: OverpassTooManyRequests")
                time.sleep(20)

        return self._get_poi_cnt_for_city_low_memory(name, lat_lng, radius)

    @staticmethod
    def _count_results(api_query_result):
        return len(api_query_result.node_ids) + len(api_query_result.relation_ids) + len(api_query_result.way_ids)

    def _get_poi_cnt_for_city_low_memory(self, name: str, lat_lng: {float, float}, radius: int):
        queries = self._build_low_memory_queries_poi_cnt_for_city(name, lat_lng, radius)
        cnt = 0
        for q in queries:
            while True:
                try:
                    r = self._api.query(q)
                    cnt += OSM._count_results(r)
                except overpy.exception.OverpassTooManyRequests:
                    print("Exception handled by API: OverpassTooManyRequests")
                    time.sleep(20)
                    continue
                except overpy.exception.OverpassBadRequest:
                    print("Exception occurred: OverpassBadRequest")
                except overpy.exception.OverpassUnknownHTTPStatusCode:
                    print("Exception occurred: OverpassUnknownHTTPStatusCode")
                break
        return cnt

    def _build_low_memory_queries_poi_cnt_for_city(self, name: str, lat_lng: {float, float}, radius: int):
        queries = [self._query_header_vast + self._query_historic + self._query_fin,
                   self._query_header_vast + self._query_leisure + self._query_fin,
                   self._query_header_vast + self._query_tourism + self._query_fin,
                   self._query_header_vast + self._query_hotel + self._query_fin,
                   self._query_header_vast + self._query_aerodrome + self._query_fin]
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
