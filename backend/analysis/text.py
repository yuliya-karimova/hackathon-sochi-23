import pandas as pd
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

interpretations = {
    'total_point': {
        'above': "Общая оценка выше чем средняя по Российской Федерации",
        'below': "Общая оценка ниже чем средняя по Российской Федерации"
    },
    'result_point': {
        'above': "Отношение количества положительных точек к отрицательным выше чем средняя по Российской Федерации",
        'below': "Отношение количества положительных точек к отрицательным ниже чем средняя по Российской Федерации"
    },

    'total_sum_neg_shcol': {
        'above': "В данном городе расстояние между точками продажи табака, алкоголя и фастфуда вблизи образовательных учреждений выше среднего по российским городам. Это может свидетельствовать о потенциальной угрозе для молодежи и учащихся. Рекомендация: Провести ревизию точек продажи вблизи образовательных учреждений и, возможно, ужесточить регуляции для такого рода торговых точек, находящихся рядом со школами и университетами.",
        'below': "В данном городе расстояние между точками продажи табака, алкоголя и фастфуда в радиусе образовательных учреждений ниже среднего по российским городам, что свидетельствует о соблюдении регуляций и заботе о безопасности молодежи."
    },

    'total_sum_neg_park': {
        'above': "В данном городе количество отрицательных точек в радиусе 200 метров от парка выше среднего по российским городам. Это может свидетельствовать о недостаточной безопасности или комфорте вблизи парковых зон. Рекомендация: Провести ревизию парков и прилегающих к ним территорий, улучшить благоустройство и установить дополнительное освещение.",
        'below': "В данном городе количество отрицательных точек в радиусе 200 метров от парка ниже среднего, что свидетельствует о хорошем благоустройстве и безопасности прилегающих к парковым зонам территорий."
    },
    'life_expectancy': {
        'above': "Продолжительность жизни в этом городе выше среднего по России. Это может говорить о качественной медицинской помощи, доступности спортивных и отдыхающих зон, а также качестве питания. Рекомендация: Продолжать вкладываться в развитие медицинских учреждений, спортивных объектов и просвещение населения о правильном питании и здоровом образе жизни.",
        'below': "Продолжительность жизни в данном городе ниже среднего по России, что требует анализа состояния здравоохранения и факторов, которые могут влиять на здоровье горожан. Рекомендация: Уделить внимание развитию медицинских учреждений, повысить доступность спортивных объектов, провести кампании по просвещению населения о правильном питании и важности здорового образа жизни."
    },
    'athlete': {
        'above': "Доля людей, регулярно занимающихся спортом, в данном городе превышает средний показатель по России. Это свидетельствует о высокой культуре физической активности среди горожан. Рекомендация: Продолжать развитие спортивной инфраструктуры и просвещение о важности регулярных физических нагрузок для здоровья.",
        'below': "Доля горожан, занимающихся спортом, ниже среднего. Это может говорить о недоступности спортивной инфраструктуры или недостаточной информированности о важности физической активности. Рекомендация: Построить или модернизировать спортивные комплексы, а также провести образовательные мероприятия о пользе спорта."
    },
    'leisure_park_per_people':{
        'above': "Площадь городских парков и зеленых зон в данном городе превышает средний показатель по России. Это способствует улучшению экологии и обеспечивает комфортное пространство для отдыха горожан. Рекомендация: Поддерживать и развивать существующие парки, а также создавать новые зеленые зоны в районах с их дефицитом.",
        'below': "В городе недостаточно парковых и зеленых зон по сравнению со средним показателем по России. Рекомендация: Рассмотреть возможность создания новых парковых зон и зеленых насаждений, что позволит улучшить экологию и создать дополнительные зоны для отдыха."
    },
    'amenity_bar_per_people':{
        'above': "Количество баров на 1.000 человек в данном городе выше среднего. Это может свидетельствовать о развитом ночном жизни и культуре отдыха. Рекомендация: Следить за качеством предоставляемых услуг и соблюдением правил безопасности в данных заведениях.",
        'below': "В городе меньше баров на душу населения по сравнению со средним показателем. Рекомендация: Рассмотреть возможность поддержки малого и среднего бизнеса в сфере гостеприимства для развития этого направления."
    },
    'leisure_pitch_per_people': {
        'above': "В вашем городе количество спортивных площадок на тысячу жителей превышает средний показатель по России. Это отражает активное внимание к физическому развитию и здоровью населения. Рекомендация: Уделяйте внимание поддержанию и обновлению существующих спортивных объектов. Продолжайте развивать инфраструктуру в районах, где она еще недостаточно представлена.",
        'below': "Уровень доступности спортивных площадок в вашем городе ниже среднего по стране. Рекомендация: Рассмотрите возможность создания новых спортивных площадок и комплексов, возможно, с привлечением инвестиций или в партнерстве с частным сектором."
    },
    'shop_alcohol_per_people': {
        'above': "В вашем городе количество магазинов, торгующих алкоголем, превышает средний показатель по России. Рекомендация: Удостоверьтесь, что все магазины соблюдают лицензионные требования и закон о продаже алкогольной продукции. Возможно, стоит разработать программы по профилактике алкоголизма.",
        'below': "В вашем городе меньше магазинов алкоголя на душу населения в сравнении со средним по стране. Рекомендация: Поддержите местные инициативы, направленные на продвижение здорового образа жизни и просвещение о вреде алкоголя."
    },
    'shop_greengrocer_per_people': {
        'above': "В вашем городе количество овощных магазинов на тысячу жителей выше среднего показателя по России. Рекомендация: Поддерживайте и стимулируйте деятельность местных фермеров и производителей, чтобы обеспечивать качественные продукты для горожан.",
        'below': "В вашем городе доступность овощных магазинов ниже среднего уровня по России. Рекомендация: Рассмотрите возможность создания фермерских рынков или поддержки местных овощеводческих предприятий для улучшения ситуации."
    }
}

def describe_city_data(row_index, data2, interpretations):
    city_data = data2.iloc[row_index]
    
    descriptions = []
    for var, name in zip(variables, variable_names):
        mean_val = data2[var].mean()
        city_val = city_data[var]
        
        if city_val > mean_val:
            description = interpretations[var]['above']
        else:
            description = interpretations[var]['below']
            
        descriptions.append(f"{name}: {description}")
    
    return "\n\n".join(descriptions)
def save_description_to_file(description, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(description)

for i in range(169):
    row_index = i
    description = describe_city_data(row_index, data2, interpretations)
    save_description_to_file(description, f'text/{row_index+1}.txt')
