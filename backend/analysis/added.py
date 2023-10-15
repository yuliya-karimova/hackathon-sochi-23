import pandas as pd
from tqdm import tqdm
import requests
import folium
import overpy
import math

df = pd.read_excel('C:\\Users\\Денис\\Desktop\\python\\hackathon3\\7.xlsx')

objects_list_org = [
'amenity=university',
'building=university',
'building=college',
'amenity=college',
'amenity=school',
'building=school',
'amenity=kindergarten',
'building=kindergarten',
'amenity=language_school',
'amenity=music_school',
'leisure=swimming_pool',
'building=stadium',
'building=riding_hall',
'leisure=fitness_centre',
'building=sports_hall',
'cycleway=*',
'leisure=ice_rink',
'leisure=park',
'highway=footway',
'leisure=pitch',
'leisure=sports_centre',
'leisure=stadium',
'leisure=track',
'amenity=marketplace',
'shop=greengrocer',
'shop=farm',
'shop=e-cigarette',
'shop=tobacco ',
'amenity=bar',
'amenity=biergarten',
'amenity=pub',
'shop=alcohol',
'shop=beverages',
'amenity=fast_food',
'amenity=food_court',
'leisure=park',
'leisure=resort',
'leisure=nature_reserve',
'highway=pedestrian',
'highway=footway',
'leisure=track',
'highway=cycleway',
'cycleway=*',
'building=sports_hall',
'leisure=sports_hall',
'leisure=sports_centre',
'leisure=fitness_station',
'leisure=stadium',
'leisure=fitness_centre',
'leisure=pitch',
'leisure=dance',
'leisure=ice_rink',
'leisure=swimming_pool',
'leisure=swimming_area',
'leisure=sauna',
'leisure=amusement_arcade',
'leisure=adult_gaming_centre',
'leisure=water_park',
'amenity=arts_centre',
'amenity=cinema',
'amenity=community_centre',
'amenity=conference_centre',
'amenity=exhibition_centre',
'amenity=music_venue',
'amenity=planetarium',
'amenity=social_centre',
'amenity=theatre',
'building=museum',
'building=stadium',
'building=civic',
'building=cathedral',
'building=chapel',
'building=church',
'building=mosque',
'building=religious',
'building=synagogue',
'building=temple',
'amenity=library',
'amenity=bar',
'amenity=biergarten',
'amenity=fast_food',
'amenity=ice_cream',
'amenity=pub',
'amenity=cafe',
'amenity=food_court',
'amenity=restaurant',
'amenity=kindergarten',
'building=kindergarten',
'building=college',
'amenity=college',
'amenity=language_school',
'amenity=dancing_school',
'amenity=driving_school',
'amenity=music_school',
'amenity=school',
'building=school',
'amenity=university',
'building=university',
'amenity=training',
'building=hospital',
'amenity=clinic',
'amenity=dentist',
'amenity=doctors',
'amenity=hospital',
'amenity=nursing_home',
'amenity=pharmacy',
'amenity=social_facility',
'emergency=ambulance_station',
'building=dormitory',
'amenity=research_institute',
'amenity=courthouse',
'amenity=fire_station',
'amenity=police',
'amenity=post_office',
'amenity=townhall',
'building=government',
'amenity=gambling',
'amenity=nightclub',
'amenity=stripclub',
'amenity=prison',
'highway=bus_guideway',
'highway=bus_stop',
'amenity=taxi',
'railway=platform',
'public_transport=station',
'railway=station',
'railway=subway_entrance',
'railway=tram_stop',
'public_transport=stop_position',
'public_transport=platform',
'highway=street_lamp',
'highway=traffic_signals',
'highway=crossing',
'amenity=bbq',
'amenity=bench',
'amenity=dressing_room',
'amenity=drinking_water',
'amenity=toilets',
'amenity=water_point',
'amenity=waste_disposal',
'amenity=waste_basket',
'amenity=recycling',
'amenity=sanitary_dump_station',
'amenity=waste_transfer_station',
'building=train_station',
'building=transportation',
'railway=*',
'railway=rail',
'bridge=yes',
'cutting=yes',
'embankment=yes',
'landuse=railway',
'highway=trunk',
'highway=primary',
'highway=secondary',
'highway=tertiary',
'highway=motorway',
'highway=unclassified',
'highway=residential',
'highway=living_street',
'building=parking',
'building=garages',
'building=garage',
'aeroway=aerodrome',
'building=industrial',
'building=barn',
'building=service',
'building=transformer_tower',
'building=warehouse',
'building=hangar',
'electrified=contact_line',
'power=cable',
'power=generator',
'power=line',
'line=busbar',
'power=switchgear',
'power=transformer',
'power=plant',
'shop=deli',
'shop=dairy',
'shop=farm',
'shop=greengrocer',
'shop=health_food',
'shop=seafood',
'shop=water',
'shop=food',
'shop=supermarket',
'shop=mall',
'shop=general',
'shop=bicycle',
'shop=outdoor',
'shop=sports',
'shop=books',
'shop=alcohol',
'shop=tobacco',
'shop=beverages',
'shop=convenience',
'shop=frozen_food',
'shop=ice_cream',
'shop=kiosk',
'building=kiosk',
'shop=money_lender',
'shop=car_repair',
'shop=wholesale',
'landuse=construction',
'landuse=industrial',
'landuse=brownfield',
'landuse=cemetery',
'landuse=garages',
'landuse=landfill',
'landuse=greenfield',
'landuse=quarry',
'landuse=railway',
'landuse=recreation_ground',
'landuse=village_green',
'landuse=winter_sports'
]

objects_list_org = [
"amenity=university",
"building=university",
"building=college",
"amenity=college",
"amenity=school",
"building=school",
"amenity=kindergarten",
"building=kindergarten",
"amenity=language_school",
"amenity=music_school",
"leisure=swimming_pool",
"building=stadium",
"building=riding_hall",
"leisure=fitness_centre",
"building=sports_hall",
"cycleway=*",
"leisure=ice_rink",
"leisure=park",
"highway=footway",
"leisure=pitch",
"leisure=sports_centre",
"leisure=stadium",
"leisure=track",
"amenity=marketplace",
"shop=greengrocer",
"shop=farm",
"shop=e-cigarette",
"shop=tobacco",
"amenity=bar",
"amenity=biergarten",
"amenity=pub",
"shop=alcohol",
"shop=beverages",
"amenity=fast_food",
"amenity=food_court",
"shop=frozen_food",
"landuse=industrial",
"landuse=brownfield",
"building=parking",
"building=warehouse",
"shop=wholesale",
"amenity=nightclub",
"shop=bicycle",
"shop=sports",
"shop=outdoor",
"shop=seafood",
"leisure=track",
"landuse=recreation_ground",
"highway=bus_stop",
"highway=street_lamp",
"amenity=waste_basket",
"amenity=toilets",
"amenity=water_point",
"military=*",
"tourism=*"
]
tags_dict = {}
for tag in objects_list_org:
    key, value = tag.split("=")
    if key in tags_dict:
        tags_dict[key].append(value)
    else:
        tags_dict[key] = [value]


def save_to_excel():
    df.to_excel("4.xlsx", index=False)

def count_amenities_nearby(df, radius_meters=25000):
    api = overpy.Overpass()
    R = 6371000  # Радиус Земли в метрах

    def haversine(coord1, coord2):
        import math
        lat1, lon1 = map(math.radians, coord1)
        lat2, lon2 = map(math.radians, coord2)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c

    for key, values in tags_dict.items():
        for value in values:
            column_name = f"{key}_{value}"
            df[column_name] = 0  # Создаем новую колонку со значением 0

    for index, row in tqdm(df.iterrows(), total=df.shape[0], desc="Processing coordinates"):
        latitude, longitude = row['latitude'], row['longitude']
        for key, values in tags_dict.items():
            for value in tqdm(values, desc=f"Processing {key}", leave=False, position=1):
                column_name = f"{key}_{value}"
                query = f"""
                    node["{key}"="{value}"]
                        ({latitude - 0.03},{longitude - 0.03},{latitude + 0.03},{longitude + 0.03});
                    out;
                """
                result = api.query(query)
                nearby_amenities = [amenity for amenity in result.nodes if haversine((latitude, longitude), (amenity.lat, amenity.lon)) <= radius_meters]
                df.at[index, column_name] = len(nearby_amenities)
        save_to_excel()
        print(index)
    return df

result_df = count_amenities_nearby(df)

print(result_df)
