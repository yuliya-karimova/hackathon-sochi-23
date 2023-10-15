import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data2 = pd.read_excel('C:\\Users\\Денис\\Desktop\\python\\hackathon3\\7.xlsx')
bad = ['amenity_bar', 
'amenity_biergarten', 
'amenity_fast_food', 
'amenity_food_court', 
'amenity_language_school', 
'amenity_nightclub', 
'amenity_pub', 
'leisure_track', 
'shop_alcohol', 
'shop_beverages', 
'shop_e-cigarette', 
'shop_tobacco']
good = [
'building_sports_hall', 
'building_stadium',  
'cycleway_*', 
'landuse_recreation_ground', 
'leisure_fitness_centre', 
'leisure_ice_rink', 
'leisure_park', 
'leisure_pitch', 
'leisure_sports_centre', 
'leisure_stadium', 
'leisure_swimming_pool', 
'shop_farm', 
'shop_greengrocer', 
'shop_sports', 
]
# Создаем новые столбцы "bad_point" и "good_point", вычисляя сумму по указанным столбцам
data2['bad_point'] = data2[bad].sum(axis=1)
data2['good_point'] = data2[good].sum(axis=1)
data2['bad_point_otn'] = data2['bad_point'] / data2['people_count']
data2['good_point_otn'] = data2['good_point'] / data2['people_count']
data2['result_point'] = (data2['good_point'] / data2['bad_point'])
data2['result_status'] = (data2['good_point'] > 1.5 * data2['bad_point']).astype(int)
# data2[data2['result_status'] == 1]
# data2

# data2 = pd.read_excel('7.xlsx')
# data2 = data2.fillna(0)
variables = [
    'total_point',
    'result_point', 'total_sum_neg_shcol',
    'total_sum_neg_park', 'life_expectancy',
    'athlete', 'leisure_park_per_people', 'amenity_bar_per_people', 'leisure_pitch_per_people',
    'shop_alcohol_per_people', 'shop_greengrocer_per_people'
]

data2['total_sum_neg_shcol2'] = data2['total_sum_neg_shcol'].apply(lambda x: 1 if x != 0 else 0)
data2['total_point'] = data2['result_point'] * 0.6 + data2['total_sum_neg_shcol2'] * 0.4
data2['leisure_park_per_people'] = data2['leisure_park'] / data2['people_count'] * 2
data2['amenity_bar_per_people'] = data2['amenity_bar'] / data2['people_count']
data2['leisure_pitch_per_people'] = data2['leisure_pitch'] / data2['people_count']
data2['shop_alcohol_per_people'] = data2['shop_alcohol'] / data2['people_count']
data2['shop_greengrocer_per_people'] = data2['shop_greengrocer'] / data2['people_count']

variable_names = [
    
    'Общая оценка по методике из ТЗ',
    'Отношение положительных точек к отрицательным',
    'Число точек продажи алкоголя, табака или фастфуда менее 100 м от образовательных учреждений',
    'Количество отрицательных точек менее 200 м от парка',
    'Продолжительность жизни',
    'Доля людей, занимающихся спортом',
    'Средняя доля парков на площадь города',
    'Среднее количество баров на 1.000 населения',
    'Количество спортивных площадок на 1.000 населения',
    'Количество магазинов по продаже алкоголя на 1.000 населения',
    'Количество овощных магазинов на 1.000 населения'
]

colors_condition_1 = [True, True, False,
    False, True, True, True, False, True, False, True]

def plot_city_data(row_index, data2):
    city_data = data2.iloc[row_index]

    fig, axes = plt.subplots(nrows=11, ncols=1, figsize=(5, 9))
    fig.suptitle(f"Данные по городу: {city_data['name']}", fontsize=16, y=1.03)

    for ax, var, name, color_cond in zip(axes, variables, variable_names, colors_condition_1):
        mean_val = data2[var].mean()
        city_val = city_data[var]
        max_val = data2[var].max()

        if not np.isfinite(max_val):
            continue
        
        ax.set_xlim(0, max_val)
        
        colors = ['#B9F0EB' if (city_val > mean_val) == color_cond else '#DD3163']
        sns.barplot(x=[city_val], y=[''], palette=colors, ax=ax, orient="h")
        ax.axvline(mean_val, color='#3B3B3B', linestyle='--')
        ax.set_title(name)

    plt.tight_layout()
    fig.text(0.1, -0.01, '* Пунктирные линии представляют средние значения по российским городам.', fontsize=10)
    filename = f"plot/{row_index+1}.jpg"
    fig.savefig(filename, bbox_inches='tight', dpi=300)


for i in range(170):
    plot_city_data(i, data2)