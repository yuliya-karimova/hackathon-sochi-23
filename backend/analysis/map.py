import pandas as pd
from tqdm import tqdm
import overpy
import requests
import folium
import overpy
import math

data2 = pd.read_excel('C:\\Users\\Денис\\Desktop\\python\\hackathon3\\7.xlsx')

def convert_to_dict(tags_list):
    return [dict([tag.split('=')]) for tag in tags_list]
yellow_objects = [
    "amenity=university", "building=university", "building=college", "amenity=college", "amenity=school",
    "building=school", "amenity=kindergarten", "building=kindergarten", "amenity=language_school", "amenity=music_school"
]
green_objects = [
    "leisure=swimming_pool", "building=stadium", "building=riding_hall", "leisure=fitness_centre", 
    "building=sports_hall", "cycleway=*", "leisure=ice_rink", "leisure=park", "highway=footway", 
    "leisure=pitch", "leisure=sports_centre", "leisure=stadium", "leisure=track", "amenity=marketplace",
    "shop=greengrocer", "shop=farm"
]
red_objects = [
    "shop=e-cigarette", "shop=tobacco", "amenity=bar", "amenity=biergarten", "amenity=pub", 
    "shop=alcohol", "shop=beverages", "amenity=fast_food", "amenity=food_court"
]

yellow_dict = convert_to_dict(yellow_objects)
green_dict = convert_to_dict(green_objects)
red_dict = convert_to_dict(red_objects)

print(yellow_dict)
print(green_dict)
print(red_dict)
descriptions_dict = {
"amenity - bar": "<b>Бар, общественное питание</b><br><span style='color: red'>Негативное влияние - продажа алкогольных напитков</span>",
    "amenity - biergarten": "<b>Паб, общественное питание</b><br><span style='color: red'>Негативное влияние - продажа алкогольных напитков</span>",
    "amenity - college": "<b>Колледж, техникум </b><br><span style='color: darkyellow'>Учебное заведение </span>",
    "amenity - fast_food": "<b>Общественное питание, фаст-фуд</b><br><span style='color: red'>Негативное влияние - изменение баланса основных нутриентов </span>",
    "amenity - food_court": "<b>Общественное питание, фуд-корт</b><br><span style='color: red'>Негативное влияние - изменение баланса основных нутриентов </span>",
    "amenity - kindergarten": "<b>Детский сад</b><br><span style='color: darkyellow'>Детское дошкольное учреждение</span>",
    "amenity - language_school": "<b>Языковая школа</b><br><span style='color: darkyellow'>Учреждение дополнительного образования</span>",
    "amenity - marketplace": "<b>Рынок</b><br><span style='color: darkyellow'>Рынок, базар или иная торговая площадка</span>",
    "amenity - music_school": "<b>Музыкальная школа</b><br><span style='color: darkyellow'>Учреждение дополнительного образования</span>",
    "amenity - pub": "<b>Паб, общественное питание</b><br><span style='color: red'>Негативное влияние - продажа алкогольных напитков</span>",
    "amenity - school": "<b>Школа</b><br><span style='color: darkyellow'>Учебное заведение</span>",
    "amenity - university": "<b>Университет</b><br><span style='color: darkyellow'>Учебное заведение</span>",
    "leisure - fitness_centre": "<b>Фитнесс-центр</b><br><span style='color: darkyellow'>Положительное влияние - место занятий спортом</span>",
  "leisure - ice_rink": "<b>Каток</b><br><span style='color: darkyellow'>Положительное влияние - место занятий спортом и активного отдыха</span>",
  "leisure - park": "<b>Парк</b><br><span style='color: darkyellow'>Положительное влияние - место занятий спортом и активного отдыха</span>",
  "leisure - pitch": "<b>Спортивная площадка</b><br><span style='color: darkyellow'>Положительное влияние - место занятий спортом</span>",
    "leisure - sports_centre": "<b>Спортивный центр</b><br><span style='color: darkyellow'>Положительное влияние - место занятий спортом</span>",
  #  leisure - sports_centre
    "leisure - stadium": "<b>Стадион</b><br><span style='color: darkyellow'>Положительное влияние - место занятий спортом</span>",
    "leisure - swimming_pool": "<b>Бассейн</b><br><span style='color: darkyellow'>Положительное влияние - место занятий спортом</span>",
    "leisure - track": "<b>Спортивная дорожка</b><br><span style='color: darkyellow'>Положительное влияние - место занятий спортом (бега, велосипеда)</span>",
    "shop - alcohol": "<b>Алкогольный магазин</b><br><span style='color: red'>Негативное влияние - продажа алкогольных напитков</span>",
    "shop - beverages": "<b>Магазин напитков</b><br><span style='color: red'>Негативное влияние - продажа напитков, в том числе алкогольных</span>",
    "shop - e-cigarette": "<b> Магазин электронных сигарет</b><br><span style='color: red'>Негативное влияние - продажа электронных сигарет и комплектующих к ним</span>",
    "shop - farm": "<b>Натуральные продукты</b><br><span style='color: darkyellow'>Положительное влияние - место продажи натуральных фермерских продуктов</span>",
    "shop - greengrocer": "<b>Свежие фрукты и овощи</b><br><span style='color: darkyellow'>Положительное влияние - место продажи свежих фруктов и овощей</span>",
    "shop - tobacco": "<b>Табачный магазин</b><br><span style='color: red'>Негативное влияние - продажа табачной продукции</span>",

}

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


def create_map(city_name):
    latitude, longitude = LocationInfo.get_city_center_coordinates(city_name)

    # Если координаты не найдены, задаем значения по умолчанию
    if not latitude or not longitude:
        latitude, longitude = 56.8386, 60.6055

    city_polygon = LocationInfo.get_city_polygon(city_name)
    parks = LocationInfo.get_parks_nearby(latitude, longitude, radius_meters)
    cafes = LocationInfo.get_cafes_nearby(latitude, longitude, radius_meters)
    
    m = folium.Map(location=[latitude, longitude], zoom_start=10)

    # Добавляем городской полигон
    folium.GeoJson(city_polygon, style_function=lambda x: {'fillColor': '#FFFFED', 'color': '#FFFFED'}).add_to(m)



    for obj_type in yellow_dict:
        objs = LocationInfo.get_objects_nearby(latitude, longitude, radius_meters, obj_type)
        for obj in objs:
            description = f"{next(iter(obj_type))} - {obj_type[next(iter(obj_type))]}"
            key = f"{next(iter(obj_type))} - {obj_type[next(iter(obj_type))]}"
            description = descriptions_dict.get(key, key)  # Если описание не найдено, используем ключ
        
            folium.Marker([obj.lat, obj.lon], 
                        icon=folium.Icon(color='lightblue'), 
                        popup=description).add_to(m)
            

    for obj_type in green_dict:
        objs = LocationInfo.get_objects_nearby(latitude, longitude, radius_meters, obj_type)
        for obj in objs:
            description = f"{next(iter(obj_type))} - {obj_type[next(iter(obj_type))]}"
            key = f"{next(iter(obj_type))} - {obj_type[next(iter(obj_type))]}"
            description = descriptions_dict.get(key, key)  # Если описание не найдено, используем ключ
            folium.Marker([obj.lat, obj.lon], 
                        icon=folium.Icon(color='green'), 
                        popup=description).add_to(m)

    for obj_type in red_dict:
        objs = LocationInfo.get_objects_nearby(latitude, longitude, radius_meters, obj_type)
        for obj in objs:
            description = f"{next(iter(obj_type))} - {obj_type[next(iter(obj_type))]}"
            key = f"{next(iter(obj_type))} - {obj_type[next(iter(obj_type))]}"
            description = descriptions_dict.get(key, key)  # Если описание не найдено, используем ключ
            folium.Marker([obj.lat, obj.lon], 
                        icon=folium.Icon(color='red'), 
                        popup=description).add_to(m)


    # Add parks
    for park in parks:
        folium.Polygon(locations=park, color='green', fill=True, fill_color='green').add_to(m)

    return m

radius_meters = 20000
for i in tqdm(range(152)):
    print(data2.loc[i, 'name'])
    city_name = data2.loc[i, 'name']
    map_object = create_map(city_name)
    map_object.save(f'map/{i}.html')
# map_object
