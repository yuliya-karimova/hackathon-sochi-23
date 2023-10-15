import pandas as pd
from tqdm import tqdm
import overpy

data3 = pd.read_excel('C:\\Users\\Денис\\Desktop\\python\\hackathon3\\7.xlsx')

tags_park = {
'leisure': ['park']
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
        for key, values in tags_park.items():
            for value in values:
                objs = LocationAnalysis.get_objects_nearby(latitude, longitude, radius_city, {key: value})
                obr_objects.extend(objs)

    @staticmethod
    def analyze_nearby_objects_for_coords(latitude, longitude):
        # Собираем все объекты tags_obr в радиусе 25км
        obr_objects = []
        for key, values in tags_park.items():
            for value in values:
                objs = LocationAnalysis.get_objects_nearby(latitude, longitude, radius_city, {key: value})
                obr_objects.extend(objs)

        # Для каждого объекта tags_obr находим ближайшие объекты tags_neg
        result = {}
        for obj in tqdm(obr_objects, desc=f"Analyzing for {latitude}, {longitude}"):
            for key, values in tags_neg.items():
                for value in values:
                    nearby_objects = LocationAnalysis.get_objects_nearby(obj.lat, obj.lon, radius_nearby, {key: value})
                    description = f"{key} - {value}_shcol"
                    if description not in result:
                        result[description] = 0
                    result[description] += len(nearby_objects)

        return result

# Примените функцию к каждой строке вашего датафрейма
for index, row in tqdm(data3.iterrows(), desc="Processing dataframe rows"):
    results = LocationAnalysis.analyze_nearby_objects_for_coords(row['latitude'], row['longitude'])
    for key, value in results.items():
        if key not in data3.columns:
            data3[key] = 0
        data3.at[index, key] = value

print(data3)

columns_to_sum = [
    'amenity - bar_shcol', 'amenity - biergarten_shcol',
    'amenity - pub_shcol', 'amenity - fast_food_shcol',
    'amenity - food_court_shcol', 'shop - e-cigarette_shcol',
    'shop - tobacco_shcol', 'shop - alcohol_shcol',
    'shop - beverages_shcol'
]

data3['total_sum_neg_park'] = data3[columns_to_sum].sum(axis=1)
# Список текущих названий столбцов
current_columns = [
    'amenity - bar_shcol', 'amenity - biergarten_shcol',
    'amenity - pub_shcol', 'amenity - fast_food_shcol',
    'amenity - food_court_shcol', 'shop - e-cigarette_shcol',
    'shop - tobacco_shcol', 'shop - alcohol_shcol',
    'shop - beverages_shcol', 'total_sum_shcol'
]

# Создаем словарь с новыми названиями
rename_dict = {col: col.replace('_shcol', '_park') for col in current_columns}

# Применяем изменения к датафрейму
data3.rename(columns=rename_dict, inplace=True)

data3['total_sum_neg_park_1000'] = data3['total_sum_neg_park'] / data3['people_count']
data3.to_excel('6.xlsx')