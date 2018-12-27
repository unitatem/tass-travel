import time

import overpy


class OSM:
    def __init__(self):
        self._api = overpy.Overpass()

    def get_poi_cnt_for_city(self, name: str, lat_lng: {float, float}, radius: int):
        query = """
        [out:json][timeout:60];
        node
          ["name"="{name}"]
          ["place"]
          ({s},{w},{n},{e});
        (
          node(around:{radius})["historic"] -> .historic_n;
          way(around:{radius})["historic"] -> .historic_w;
          relation(around:{radius})["historic"] -> .historic_r;
          
          node(around:{radius})["leisure"] -> .leisure_n;
          way(around:{radius})["leisure"] -> .leisure_w;
          relation(around:{radius})["leisure"] -> .leisure_r;
          
          node(around:{radius})["tourism"] -> .tourism_n;
          way(around:{radius})["tourism"] -> .tourism_w;
          relation(around:{radius})["tourism"] -> .tourism_r;
          
          node(around:{radius})["building"="hotel"] -> .hotel_n;
          way(around:{radius})["building"="hotel"] -> .hotel_w;
          relation(around:{radius})["building"="hotel"] -> .hotel_r;
          
          node(around:{radius_x_2})["aeroway"="aerodrome"] -> .aerodrome_n;
          way(around:{radius_x_2})["aeroway"="aerodrome"] -> .aerodrome_w;
          relation(around:{radius_x_2})["aeroway"="aerodrome"] -> .aerodrome_r;
        );
        out body;
        >;
        out skel qt;
        """.format(name=name,
                   n=lat_lng['lat'] + 1.0,
                   s=lat_lng['lat'] - 1.0,
                   w=lat_lng['lng'] - 1.0,
                   e=lat_lng['lng'] + 1.0,
                   radius=radius,
                   radius_x_2=radius * 2)
        while True:
            try:
                result = self._api.query(query)
                return len(result.node_ids) + len(result.relation_ids) + len(result.way_ids)
            except overpy.exception.OverpassTooManyRequests:
                print("Exception handled by API: OverpassTooManyRequests")
                time.sleep(20)
