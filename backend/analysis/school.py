import pandas as pd
from tqdm import tqdm
import overpy
import requests
import folium
import overpy
import math

data3 = pd.read_excel('C:\\Users\\Денис\\Desktop\\python\\hackathon3\\7.xlsx')

class LocationInfo:
    @staticmethod
    def haversine(coord1, coord2):
        R = 6371000  # Radius of the Earth in meters
        lat1, lon1 = map(math.radians, coord1)
        lat2, lon2 = map(math.radians, coord2)

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return R * c

    @staticmethod
    def get_city_polygon(city_name):
        url = f"https://nominatim.openstreetmap.org/search?city={city_name}&format=json&polygon_geojson=1"
        response = requests.get(url)
        data = response.json()

        for item in data:
            if item.get("geojson", {}).get("type") in ["Polygon", "MultiPolygon"]:
                return item["geojson"]
        return None

    @staticmethod
    def get_parks_nearby(latitude, longitude, radius_meters):
        api = overpy.Overpass()
        popr = radius_meters / 100000
        bounds = (latitude - popr, longitude - popr, latitude + popr, longitude + popr)
        query = f"""
            way["leisure"="park"]{bounds};
            (._;>;);
            out body;
        """
        result = api.query(query)

        nearby_parks = []
        for way in result.ways:
            nodes = way.get_nodes()
            coords = [(node.lat, node.lon) for node in nodes]
            centroid_lat = sum(node.lat for node in nodes) / len(nodes)
            centroid_lon = sum(node.lon for node in nodes) / len(nodes)
            if LocationInfo.haversine((latitude, longitude), (centroid_lat, centroid_lon)) <= radius_meters:
                nearby_parks.append(coords)
        return nearby_parks

    @staticmethod
    def get_cafes_nearby(latitude, longitude, radius_meters):
        api = overpy.Overpass()
        popr = radius_meters / 100000
        bounds = (latitude - popr, longitude - popr, latitude + popr, longitude + popr)
        query = f"""
            node["amenity"="cafe"]{bounds};
            out;
        """
        result = api.query(query)
        nearby_cafes = [cafe for cafe in result.nodes if LocationInfo.haversine((latitude, longitude), (cafe.lat, cafe.lon)) <= radius_meters]
        return nearby_cafes

    @staticmethod
    def get_city_center_coordinates(city_name):
        """Возвращает координаты центра города по его имени"""
        url = f"https://nominatim.openstreetmap.org/search?city={city_name}&format=json"
        response = requests.get(url)
        data = response.json()

        if data:
            return float(data[0]['lat']), float(data[0]['lon'])
        return None

    @staticmethod
    def get_objects_nearby(latitude, longitude, radius_meters, obj_type):
        api = overpy.Overpass()
        popr = radius_meters / 100000
        bounds = (latitude - popr, longitude - popr, latitude + popr, longitude + popr)
        query = f"""
            node["{next(iter(obj_type))}"="{obj_type[next(iter(obj_type))]}"]{bounds};
            out;
        """
        result = api.query(query)
        return result.nodes


tags_obr = {
    'amenity': ['university', 'college', 'school'],
    'building': ['university', 'college', 'school']
}

tags_neg = {
    'amenity': ['bar', 'biergarten', 'pub', 'fast_food', 'food_court'],
    'shop': ['e-cigarette', 'tobacco', 'alcohol', 'beverages']
}

radius_city = 25000
radius_nearby = 100

class LocationAnalysis:
    @staticmethod
    def get_objects_nearby(latitude, longitude, radius_meters, obj_type):
        api = overpy.Overpass()
        popr = radius_meters / 100000
        # bounds = (latitude - popr, longitude - popr, latitude + popr, longitude + popr)
        bounds = (float(latitude) - popr, float(longitude) - popr, float(latitude) + popr, float(longitude) + popr)

        query = f"""
            node["{next(iter(obj_type))}"="{obj_type[next(iter(obj_type))]}"]{bounds};
            out;
        """
        result = api.query(query)
        return result.nodes

    @staticmethod
    def analyze_nearby_objects(city_name):
        latitude, longitude = LocationInfo.get_city_center_coordinates(city_name)

        # Собираем все объекты tags_obr в радиусе 25км
        obr_objects = []
        for key, values in tags_obr.items():
            for value in values:
                objs = LocationAnalysis.get_objects_nearby(latitude, longitude, radius_city, {key: value})
                obr_objects.extend(objs)

        # Для каждого объекта tags_obr находим ближайшие объекты tags_neg
        result = {}
        for obj in tqdm(obr_objects, desc="Analyzing positive objects"):
            for key, values in tags_neg.items():
                for value in values:
                    nearby_objects = LocationAnalysis.get_objects_nearby(obj.lat, obj.lon, radius_nearby, {key: value})
                    description = f"{key} - {value}"
                    if description not in result:
                        result[description] = 0
                    result[description] += len(nearby_objects)

        return result

results = LocationAnalysis.analyze_nearby_objects("Екатеринбург")
print(results)
