const regions = [
  {
      "id": 514,
      "name": "Алтайский край",
      "city_count": 12,
      "people_count": 1232.2,
      "people_unit": "млн чел.",
      "min_point": 164,
      "max_point": 208,
      "avg_point": 183,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/514/thumb_3001_altaisky_kray.jpg",
      "federal_district": "Сибирский федеральный округ",
      "favorable_count": 25,
      "dynamiс": 8
  },
  {
      "id": 515,
      "name": "Амурская область",
      "city_count": 10,
      "people_count": 455.9,
      "people_unit": "тыс. чел.",
      "min_point": 161,
      "max_point": 209,
      "avg_point": 179,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/515/thumb_3002_murskaya_oblast.png",
      "federal_district": "Дальневосточный федеральный округ",
      "favorable_count": 40,
      "dynamiс": 10
  },
  {
      "id": 516,
      "name": "Архангельская область",
      "city_count": 13,
      "people_count": 767.2,
      "people_unit": "тыс. чел.",
      "min_point": 154,
      "max_point": 200,
      "avg_point": 180,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/516/thumb_3003_arkhangelskaya_oblast.jpg",
      "federal_district": "Северо-Западный федеральный округ",
      "favorable_count": 38,
      "dynamiс": 7
  },
  {
      "id": 517,
      "name": "Астраханская область",
      "city_count": 6,
      "people_count": 623.2,
      "people_unit": "тыс. чел.",
      "min_point": 172,
      "max_point": 198,
      "avg_point": 184,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/517/thumb_3004_astrakhanskaya_oblast.png",
      "federal_district": "Южный федеральный округ",
      "favorable_count": 50,
      "dynamiс": 17
  },
  {
      "id": 518,
      "name": "Белгородская область",
      "city_count": 11,
      "people_count": 872.6,
      "people_unit": "тыс. чел.",
      "min_point": 180,
      "max_point": 235,
      "avg_point": 206,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/518/thumb_3005_belgorodskaya_oblast.png",
      "federal_district": "Центральный федеральный округ",
      "favorable_count": 82,
      "dynamiс": 9
  },
  {
      "id": 519,
      "name": "Брянская область",
      "city_count": 16,
      "people_count": 682.9,
      "people_unit": "тыс. чел.",
      "min_point": 157,
      "max_point": 223,
      "avg_point": 187,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/519/thumb_3006_bryanskaya_oblast.png",
      "federal_district": "Центральный федеральный округ",
      "favorable_count": 38,
      "dynamiс": 7
  },
  {
      "id": 520,
      "name": "Владимирская область",
      "city_count": 23,
      "people_count": 983.2,
      "people_unit": "млн чел.",
      "min_point": 163,
      "max_point": 236,
      "avg_point": 200,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/520/thumb_3007_vladimirskaya_oblast.png",
      "federal_district": "Центральный федеральный округ",
      "favorable_count": 48,
      "dynamiс": 9
  },
  {
      "id": 521,
      "name": "Волгоградская область",
      "city_count": 19,
      "people_count": 1761.1,
      "people_unit": "млн чел.",
      "min_point": 167,
      "max_point": 215,
      "avg_point": 186,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/521/thumb_3008_volgogradskaya_oblast.png",
      "federal_district": "Южный федеральный округ",
      "favorable_count": 42,
      "dynamiс": 10
  },
  {
      "id": 522,
      "name": "Вологодская область",
      "city_count": 15,
      "people_count": 778.3,
      "people_unit": "тыс. чел.",
      "min_point": 163,
      "max_point": 226,
      "avg_point": 192,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/522/thumb_3009_vologodskaya_oblast.png",
      "federal_district": "Северо-Западный федеральный округ",
      "favorable_count": 47,
      "dynamiс": 7
  },
  {
      "id": 523,
      "name": "Воронежская область",
      "city_count": 15,
      "people_count": 1436.2,
      "people_unit": "млн чел.",
      "min_point": 167,
      "max_point": 225,
      "avg_point": 195,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/523/thumb_3010_voronezhskaya_oblast.gif",
      "federal_district": "Центральный федеральный округ",
      "favorable_count": 53,
      "dynamiс": 13
  },
  {
      "id": 524,
      "name": "Еврейская автономная область",
      "city_count": 2,
      "people_count": 77.2,
      "people_unit": "тыс. чел.",
      "min_point": 155,
      "max_point": 180,
      "avg_point": 168,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/524/thumb_3011_evreiskaya_avtonomnaya_oblast.png",
      "federal_district": "Дальневосточный федеральный округ",
      "favorable_count": 0,
      "dynamiс": 0
  },
  {
      "id": 525,
      "name": "Забайкальский край",
      "city_count": 10,
      "people_count": 513,
      "people_unit": "тыс. чел.",
      "min_point": 116,
      "max_point": 190,
      "avg_point": 154,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/525/thumb_3012_zabaikalsky_kray.png",
      "federal_district": "Дальневосточный федеральный округ",
      "favorable_count": 20,
      "dynamiс": 0
  },
  {
      "id": 526,
      "name": "Ивановская область",
      "city_count": 17,
      "people_count": 757,
      "people_unit": "тыс. чел.",
      "min_point": 178,
      "max_point": 216,
      "avg_point": 197,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/526/thumb_3013_ivanovskaya_oblast.jpg",
      "federal_district": "Центральный федеральный округ",
      "favorable_count": 65,
      "dynamiс": 6
  },
  {
      "id": 527,
      "name": "Иркутская область",
      "city_count": 22,
      "people_count": 1642.5,
      "people_unit": "млн чел.",
      "min_point": 109,
      "max_point": 203,
      "avg_point": 165,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/527/thumb_3014_irkutskaya_oblast.png",
      "federal_district": "Сибирский федеральный округ",
      "favorable_count": 23,
      "dynamiс": 9
  },
  {
      "id": 528,
      "name": "Калининградская область",
      "city_count": 22,
      "people_count": 793.4,
      "people_unit": "тыс. чел.",
      "min_point": 164,
      "max_point": 250,
      "avg_point": 207,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/528/thumb_3015_kaliningradskaya_oblast.jpg",
      "federal_district": "Северо-Западный федеральный округ",
      "favorable_count": 64,
      "dynamiс": 5
  },
  {
      "id": 529,
      "name": "Калужская область",
      "city_count": 22,
      "people_count": 730.3,
      "people_unit": "тыс. чел.",
      "min_point": 180,
      "max_point": 226,
      "avg_point": 198,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/529/thumb_3016_kaluzhskaya_oblast.png",
      "federal_district": "Центральный федеральный округ",
      "favorable_count": 55,
      "dynamiс": 10
  },
  {
      "id": 530,
      "name": "Камчатский край",
      "city_count": 3,
      "people_count": 242.5,
      "people_unit": "тыс. чел.",
      "min_point": 179,
      "max_point": 190,
      "avg_point": 183,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/530/thumb_3017_kamchatsky_kray.png",
      "federal_district": "Дальневосточный федеральный округ",
      "favorable_count": 33,
      "dynamiс": 0
  },
  {
      "id": 531,
      "name": "Кемеровская область",
      "city_count": 20,
      "people_count": 2068.1,
      "people_unit": "млн чел.",
      "min_point": 148,
      "max_point": 212,
      "avg_point": 179,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/531/thumb_3018_kemerovskaya_oblast.png",
      "federal_district": "Сибирский федеральный округ",
      "favorable_count": 25,
      "dynamiс": 10
  },
  {
      "id": 532,
      "name": "Кировская область",
      "city_count": 18,
      "people_count": 811.3,
      "people_unit": "тыс. чел.",
      "min_point": 160,
      "max_point": 203,
      "avg_point": 180,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/532/thumb_3019_kirovskaya_oblast.png",
      "federal_district": "Приволжский федеральный округ",
      "favorable_count": 39,
      "dynamiс": 11
  },
  {
      "id": 533,
      "name": "Костромская область",
      "city_count": 12,
      "people_count": 417,
      "people_unit": "тыс. чел.",
      "min_point": 165,
      "max_point": 214,
      "avg_point": 190,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/533/thumb_3020_kostromskaya_oblast.png",
      "federal_district": "Центральный федеральный округ",
      "favorable_count": 50,
      "dynamiс": 8
  },
  {
      "id": 534,
      "name": "Краснодарский край",
      "city_count": 26,
      "people_count": 3011.9,
      "people_unit": "млн чел.",
      "min_point": 164,
      "max_point": 243,
      "avg_point": 192,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/534/thumb_3021_krasnodarsky_kray.jpg",
      "federal_district": "Южный федеральный округ",
      "favorable_count": 38,
      "dynamiс": 3
  },
  {
      "id": 535,
      "name": "Красноярский край",
      "city_count": 23,
      "people_count": 2045.4,
      "people_unit": "млн чел.",
      "min_point": 140,
      "max_point": 223,
      "avg_point": 185,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/535/thumb_3022_krasnoyarsky_kray.png",
      "federal_district": "Сибирский федеральный округ",
      "favorable_count": 39,
      "dynamiс": 4
  },
  {
      "id": 536,
      "name": "Курганская область",
      "city_count": 9,
      "people_count": 462.1,
      "people_unit": "тыс. чел.",
      "min_point": 140,
      "max_point": 201,
      "avg_point": 169,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/536/thumb_3023_kurganskaya_oblast.png",
      "federal_district": "Уральский федеральный округ",
      "favorable_count": 33,
      "dynamiс": 11
  },
  {
      "id": 537,
      "name": "Курская область",
      "city_count": 10,
      "people_count": 663.3,
      "people_unit": "тыс. чел.",
      "min_point": 180,
      "max_point": 218,
      "avg_point": 197,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/537/thumb_3024_kurskaya_oblast.png",
      "federal_district": "Центральный федеральный округ",
      "favorable_count": 70,
      "dynamiс": 30
  },
  {
      "id": 538,
      "name": "Ленинградская область",
      "city_count": 33,
      "people_count": 1008.2,
      "people_unit": "тыс. чел.",
      "min_point": 168,
      "max_point": 261,
      "avg_point": 208,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/538/thumb_3025_leningradskaya_oblast.png",
      "federal_district": "Северо-Западный федеральный округ",
      "favorable_count": 70,
      "dynamiс": 6
  },
  {
      "id": 539,
      "name": "Липецкая область",
      "city_count": 8,
      "people_count": 718.9,
      "people_unit": "тыс. чел.",
      "min_point": 188,
      "max_point": 224,
      "avg_point": 204,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/539/thumb_3026_lipetskaya_oblast.png",
      "federal_district": "Центральный федеральный округ",
      "favorable_count": 100,
      "dynamiс": 25
  },
  {
      "id": 540,
      "name": "Магаданская область",
      "city_count": 2,
      "people_count": 95.6,
      "people_unit": "тыс. чел.",
      "min_point": 174,
      "max_point": 191,
      "avg_point": 183,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/540/thumb_3027_magadanskaya_oblast.png",
      "federal_district": "Дальневосточный федеральный округ",
      "favorable_count": 50,
      "dynamiс": 0
  },
  {
      "id": 512,
      "name": "Москва",
      "city_count": 1,
      "people_count": 12635.5,
      "people_unit": "млн чел.",
      "min_point": 299,
      "max_point": 299,
      "avg_point": 299,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/512/thumb_777_moskva.png",
      "federal_district": "Центральный федеральный округ",
      "favorable_count": 100,
      "dynamiс": 0
  },
  {
      "id": 541,
      "name": "Московская область",
      "city_count": 74,
      "people_count": 5727.9,
      "people_unit": "млн чел.",
      "min_point": 180,
      "max_point": 268,
      "avg_point": 224,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/541/thumb_3029_moskovskaya_oblast.png",
      "federal_district": "Центральный федеральный округ",
      "favorable_count": 95,
      "dynamiс": 4
  },
  {
      "id": 542,
      "name": "Мурманская область",
      "city_count": 16,
      "people_count": 608.1,
      "people_unit": "тыс. чел.",
      "min_point": 162,
      "max_point": 243,
      "avg_point": 209,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/542/thumb_3030_murmanskaya_oblast.png",
      "federal_district": "Северо-Западный федеральный округ",
      "favorable_count": 81,
      "dynamiс": 6
  },
  {
      "id": 543,
      "name": "Ненецкий автономный округ",
      "city_count": 1,
      "people_count": 25.8,
      "people_unit": "тыс. чел.",
      "min_point": 199,
      "max_point": 199,
      "avg_point": 199,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/543/thumb_3031_nenetsky_avtonomny_okrug.png",
      "federal_district": "Северо-Западный федеральный округ",
      "favorable_count": 100,
      "dynamiс": 0
  },
  {
      "id": 544,
      "name": "Нижегородская область",
      "city_count": 28,
      "people_count": 2278,
      "people_unit": "млн чел.",
      "min_point": 175,
      "max_point": 235,
      "avg_point": 199,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/544/thumb_3032_nizhegorodskaya_oblast.png",
      "federal_district": "Приволжский федеральный округ",
      "favorable_count": 54,
      "dynamiс": 11
  },
  {
      "id": 545,
      "name": "Новгородская область",
      "city_count": 10,
      "people_count": 372.5,
      "people_unit": "тыс. чел.",
      "min_point": 180,
      "max_point": 253,
      "avg_point": 211,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/545/thumb_3033_novgorodskaya_oblast.png",
      "federal_district": "Северо-Западный федеральный округ",
      "favorable_count": 80,
      "dynamiс": 30
  },
  {
      "id": 546,
      "name": "Новосибирская область",
      "city_count": 14,
      "people_count": 2018.1,
      "people_unit": "млн чел.",
      "min_point": 141,
      "max_point": 204,
      "avg_point": 171,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/546/thumb_3034_novosibirskaya_oblast.png",
      "federal_district": "Сибирский федеральный округ",
      "favorable_count": 29,
      "dynamiс": 15
  },
  {
      "id": 547,
      "name": "Омская область",
      "city_count": 6,
      "people_count": 1218.9,
      "people_unit": "млн чел.",
      "min_point": 148,
      "max_point": 185,
      "avg_point": 166,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/547/thumb_3035_omskaya_oblast.png",
      "federal_district": "Сибирский федеральный округ",
      "favorable_count": 33,
      "dynamiс": 16
  },
  {
      "id": 548,
      "name": "Оренбургская область",
      "city_count": 12,
      "people_count": 1175.4,
      "people_unit": "млн чел.",
      "min_point": 168,
      "max_point": 206,
      "avg_point": 184,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/548/thumb_3036_orenburgskaya_oblast.png",
      "federal_district": "Приволжский федеральный округ",
      "favorable_count": 33,
      "dynamiс": 16
  },
  {
      "id": 549,
      "name": "Орловская область",
      "city_count": 7,
      "people_count": 401.9,
      "people_unit": "тыс. чел.",
      "min_point": 177,
      "max_point": 226,
      "avg_point": 202,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/549/thumb_3037_orlovskaya_oblast.png",
      "federal_district": "Центральный федеральный округ",
      "favorable_count": 86,
      "dynamiс": 43
  },
  {
      "id": 550,
      "name": "Пензенская область",
      "city_count": 11,
      "people_count": 783.9,
      "people_unit": "тыс. чел.",
      "min_point": 163,
      "max_point": 229,
      "avg_point": 188,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/550/thumb_3038_penzenskaya_oblast.png",
      "federal_district": "Приволжский федеральный округ",
      "favorable_count": 45,
      "dynamiс": 9
  },
  {
      "id": 551,
      "name": "Пермский край",
      "city_count": 25,
      "people_count": 1830.6,
      "people_unit": "млн чел.",
      "min_point": 170,
      "max_point": 224,
      "avg_point": 188,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/551/thumb_3039_permsky_kray.png",
      "federal_district": "Приволжский федеральный округ",
      "favorable_count": 36,
      "dynamiс": 12
  },
  {
      "id": 552,
      "name": "Приморский край",
      "city_count": 12,
      "people_count": 1296.2,
      "people_unit": "млн чел.",
      "min_point": 137,
      "max_point": 205,
      "avg_point": 174,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/552/thumb_3040_primorsky_kray.png",
      "federal_district": "Дальневосточный федеральный округ",
      "favorable_count": 42,
      "dynamiс": 9
  },
  {
      "id": 553,
      "name": "Псковская область",
      "city_count": 14,
      "people_count": 393.1,
      "people_unit": "тыс. чел.",
      "min_point": 164,
      "max_point": 224,
      "avg_point": 192,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/553/thumb_3041_pskovskaya_oblast.png",
      "federal_district": "Северо-Западный федеральный округ",
      "favorable_count": 50,
      "dynamiс": 7
  },
  {
      "id": 554,
      "name": "Республика Адыгея",
      "city_count": 2,
      "people_count": 152,
      "people_unit": "тыс. чел.",
      "min_point": 198,
      "max_point": 221,
      "avg_point": 210,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/554/thumb_3042_respublika_adygeya.png",
      "federal_district": "Южный федеральный округ",
      "favorable_count": 100,
      "dynamiс": 0
  },
  {
      "id": 555,
      "name": "Республика Алтай",
      "city_count": 1,
      "people_count": 64.6,
      "people_unit": "тыс. чел.",
      "min_point": 198,
      "max_point": 198,
      "avg_point": 198,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/555/thumb_3043_respublika_altai.png",
      "federal_district": "Сибирский федеральный округ",
      "favorable_count": 100,
      "dynamiс": 0
  },
  {
      "id": 556,
      "name": "Республика Башкортостан",
      "city_count": 21,
      "people_count": 2476.1,
      "people_unit": "млн чел.",
      "min_point": 180,
      "max_point": 215,
      "avg_point": 199,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/556/thumb_3044_respublika_bashkortostan.png",
      "federal_district": "Приволжский федеральный округ",
      "favorable_count": 76,
      "dynamiс": 9
  },
  {
      "id": 557,
      "name": "Республика Бурятия",
      "city_count": 6,
      "people_count": 519.1,
      "people_unit": "тыс. чел.",
      "min_point": 151,
      "max_point": 185,
      "avg_point": 169,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/557/thumb_3045_respublika_buryatiya.png",
      "federal_district": "Дальневосточный федеральный округ",
      "favorable_count": 17,
      "dynamiс": 0
  },
  {
      "id": 558,
      "name": "Республика Дагестан",
      "city_count": 10,
      "people_count": 1271.2,
      "people_unit": "млн чел.",
      "min_point": 147,
      "max_point": 202,
      "avg_point": 181,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/558/thumb_3046_respublika_dagestan.gif",
      "federal_district": "Северо-Кавказский федеральный округ",
      "favorable_count": 40,
      "dynamiс": 10
  },
  {
      "id": 559,
      "name": "Республика Ингушетия",
      "city_count": 5,
      "people_count": 292.2,
      "people_unit": "тыс. чел.",
      "min_point": 137,
      "max_point": 201,
      "avg_point": 163,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/559/thumb_3047_respublika_ingushetia.png",
      "federal_district": "Северо-Кавказский федеральный округ",
      "favorable_count": 20,
      "dynamiс": 0
  },
  {
      "id": 560,
      "name": "Республика Кабардино-Балкария",
      "city_count": 8,
      "people_count": 452.7,
      "people_unit": "тыс. чел.",
      "min_point": 164,
      "max_point": 236,
      "avg_point": 189,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/560/thumb_3048_respublika_kabardino_balkariya.png",
      "federal_district": "Северо-Кавказский федеральный округ",
      "favorable_count": 50,
      "dynamiс": 12
  },
  {
      "id": 561,
      "name": "Республика Калмыкия",
      "city_count": 3,
      "people_count": 124.3,
      "people_unit": "тыс. чел.",
      "min_point": 161,
      "max_point": 189,
      "avg_point": 177,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/561/thumb_3049_respublika_kalmykiya.gif",
      "federal_district": "Южный федеральный округ",
      "favorable_count": 67,
      "dynamiс": 0
  },
  {
      "id": 562,
      "name": "Республика Карачаево-Черкесия",
      "city_count": 4,
      "people_count": 183,
      "people_unit": "тыс. чел.",
      "min_point": 138,
      "max_point": 189,
      "avg_point": 167,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/562/thumb_3050_karachaevo_cherkesiya.png",
      "federal_district": "Северо-Кавказский федеральный округ",
      "favorable_count": 50,
      "dynamiс": 0
  },
  {
      "id": 563,
      "name": "Республика Карелия",
      "city_count": 13,
      "people_count": 456.5,
      "people_unit": "тыс. чел.",
      "min_point": 157,
      "max_point": 220,
      "avg_point": 187,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/563/thumb_3051_respublika_kareliya.png",
      "federal_district": "Северо-Западный федеральный округ",
      "favorable_count": 46,
      "dynamiс": 8
  },
  {
      "id": 564,
      "name": "Республика Коми",
      "city_count": 10,
      "people_count": 538.9,
      "people_unit": "тыс. чел.",
      "min_point": 170,
      "max_point": 235,
      "avg_point": 196,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/564/thumb_3052_respublika_komi.png",
      "federal_district": "Северо-Западный федеральный округ",
      "favorable_count": 50,
      "dynamiс": 10
  },
  {
      "id": 565,
      "name": "Республика Крым",
      "city_count": 16,
      "people_count": 962.2,
      "people_unit": "тыс. чел.",
      "min_point": 146,
      "max_point": 239,
      "avg_point": 187,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/565/thumb_3053_respublika_krym.png",
      "federal_district": "Южный федеральный округ",
      "favorable_count": 44,
      "dynamiс": 6
  },
  {
      "id": 566,
      "name": "Республика Марий Эл",
      "city_count": 4,
      "people_count": 361.8,
      "people_unit": "тыс. чел.",
      "min_point": 179,
      "max_point": 224,
      "avg_point": 202,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/566/thumb_3054_respublika_mariy_el.png",
      "federal_district": "Приволжский федеральный округ",
      "favorable_count": 75,
      "dynamiс": 25
  },
  {
      "id": 567,
      "name": "Республика Мордовия",
      "city_count": 7,
      "people_count": 408.6,
      "people_unit": "тыс. чел.",
      "min_point": 155,
      "max_point": 200,
      "avg_point": 178,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/567/thumb_3055_respublika_mordoviya.png",
      "federal_district": "Приволжский федеральный округ",
      "favorable_count": 43,
      "dynamiс": 0
  },
  {
      "id": 568,
      "name": "Республика Саха (Якутия)",
      "city_count": 13,
      "people_count": 545,
      "people_unit": "тыс. чел.",
      "min_point": 120,
      "max_point": 185,
      "avg_point": 143,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/568/thumb_3056_respublika_sakha.png",
      "federal_district": "Дальневосточный федеральный округ",
      "favorable_count": 15,
      "dynamiс": 0
  },
  {
      "id": 569,
      "name": "Республика Северная Осетия - Алания",
      "city_count": 6,
      "people_count": 426,
      "people_unit": "тыс. чел.",
      "min_point": 160,
      "max_point": 209,
      "avg_point": 181,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/569/thumb_3057_respublika_severnaya_osetiya.png",
      "federal_district": "Северо-Кавказский федеральный округ",
      "favorable_count": 50,
      "dynamiс": 17
  },
  {
      "id": 570,
      "name": "Республика Татарстан",
      "city_count": 24,
      "people_count": 2843.3,
      "people_unit": "млн чел.",
      "min_point": 180,
      "max_point": 248,
      "avg_point": 204,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/570/thumb_3058_respublika_tatarstan.png",
      "federal_district": "Приволжский федеральный округ",
      "favorable_count": 88,
      "dynamiс": 13
  },
  {
      "id": 571,
      "name": "Республика Тыва",
      "city_count": 5,
      "people_count": 162.6,
      "people_unit": "тыс. чел.",
      "min_point": 136,
      "max_point": 188,
      "avg_point": 157,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/571/thumb_3059_respublika_tyva.png",
      "federal_district": "Сибирский федеральный округ",
      "favorable_count": 20,
      "dynamiс": 0
  },
  {
      "id": 573,
      "name": "Республика Хакасия",
      "city_count": 5,
      "people_count": 332.8,
      "people_unit": "тыс. чел.",
      "min_point": 170,
      "max_point": 214,
      "avg_point": 188,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/573/thumb_3061_respublika_khakasiya.png",
      "federal_district": "Сибирский федеральный округ",
      "favorable_count": 40,
      "dynamiс": 20
  },
  {
      "id": 576,
      "name": "Ростовская область",
      "city_count": 23,
      "people_count": 2787.4,
      "people_unit": "млн чел.",
      "min_point": 154,
      "max_point": 234,
      "avg_point": 186,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/576/thumb_3064_rostovskaya_oblast.png",
      "federal_district": "Южный федеральный округ",
      "favorable_count": 43,
      "dynamiс": 8
  },
  {
      "id": 577,
      "name": "Рязанская область",
      "city_count": 12,
      "people_count": 699.9,
      "people_unit": "тыс. чел.",
      "min_point": 170,
      "max_point": 221,
      "avg_point": 189,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/577/thumb_3065_ryazanskaya_oblast.png",
      "federal_district": "Центральный федеральный округ",
      "favorable_count": 42,
      "dynamiс": 9
  },
  {
      "id": 578,
      "name": "Самарская область",
      "city_count": 11,
      "people_count": 2356.2,
      "people_unit": "млн чел.",
      "min_point": 159,
      "max_point": 211,
      "avg_point": 184,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/578/thumb_3066_samarskaya_oblast.png",
      "federal_district": "Приволжский федеральный округ",
      "favorable_count": 45,
      "dynamiс": 18
  },
  {
      "id": 513,
      "name": "Санкт-Петербург",
      "city_count": 1,
      "people_count": 5377.5,
      "people_unit": "млн чел.",
      "min_point": 264,
      "max_point": 264,
      "avg_point": 264,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/513/thumb_778_sankt_peterburg.png",
      "federal_district": "Северо-Западный федеральный округ",
      "favorable_count": 100,
      "dynamiс": 0
  },
  {
      "id": 579,
      "name": "Саратовская область",
      "city_count": 18,
      "people_count": 1631.4,
      "people_unit": "млн чел.",
      "min_point": 169,
      "max_point": 233,
      "avg_point": 193,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/579/thumb_3068_saratovskaya_oblast.png",
      "federal_district": "Приволжский федеральный округ",
      "favorable_count": 50,
      "dynamiс": 11
  },
  {
      "id": 580,
      "name": "Сахалинская область",
      "city_count": 14,
      "people_count": 358.5,
      "people_unit": "тыс. чел.",
      "min_point": 170,
      "max_point": 205,
      "avg_point": 188,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/580/thumb_3069_sakhalinskaya_oblast.png",
      "federal_district": "Дальневосточный федеральный округ",
      "favorable_count": 57,
      "dynamiс": 36
  },
  {
      "id": 581,
      "name": "Свердловская область",
      "city_count": 47,
      "people_count": 3475.1,
      "people_unit": "млн чел.",
      "min_point": 163,
      "max_point": 233,
      "avg_point": 195,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/581/thumb_3070_sverdlovskaya_oblast.png",
      "federal_district": "Уральский федеральный округ",
      "favorable_count": 60,
      "dynamiс": 20
  },
  {
      "id": 511,
      "name": "Севастополь",
      "city_count": 1,
      "people_count": 522.1,
      "people_unit": "тыс. чел.",
      "min_point": 195,
      "max_point": 195,
      "avg_point": 195,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/511/thumb_582_sevastopol.png",
      "federal_district": "Южный федеральный округ",
      "favorable_count": 100,
      "dynamiс": 0
  },
  {
      "id": 582,
      "name": "Смоленская область",
      "city_count": 15,
      "people_count": 613.7,
      "people_unit": "тыс. чел.",
      "min_point": 163,
      "max_point": 223,
      "avg_point": 190,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/582/thumb_3072_smolenskaya_oblast.png",
      "federal_district": "Центральный федеральный округ",
      "favorable_count": 53,
      "dynamiс": 6
  },
  {
      "id": 583,
      "name": "Ставропольский край",
      "city_count": 19,
      "people_count": 1535.3,
      "people_unit": "млн чел.",
      "min_point": 163,
      "max_point": 226,
      "avg_point": 186,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/583/thumb_3073_stavropolsky_kray.png",
      "federal_district": "Северо-Кавказский федеральный округ",
      "favorable_count": 47,
      "dynamiс": 5
  },
  {
      "id": 584,
      "name": "Тамбовская область",
      "city_count": 8,
      "people_count": 535,
      "people_unit": "тыс. чел.",
      "min_point": 175,
      "max_point": 227,
      "avg_point": 203,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/584/thumb_3074_tambovskaya_oblast.png",
      "federal_district": "Центральный федеральный округ",
      "favorable_count": 75,
      "dynamiс": 25
  },
  {
      "id": 585,
      "name": "Тверская область",
      "city_count": 23,
      "people_count": 836.9,
      "people_unit": "тыс. чел.",
      "min_point": 171,
      "max_point": 223,
      "avg_point": 191,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/585/thumb_3075_tverskaya_oblast.png",
      "federal_district": "Центральный федеральный округ",
      "favorable_count": 43,
      "dynamiс": 8
  },
  {
      "id": 586,
      "name": "Томская область",
      "city_count": 6,
      "people_count": 763.4,
      "people_unit": "тыс. чел.",
      "min_point": 172,
      "max_point": 208,
      "avg_point": 190,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/586/thumb_3076_tomskaya_oblast.png",
      "federal_district": "Сибирский федеральный округ",
      "favorable_count": 50,
      "dynamiс": 17
  },
  {
      "id": 587,
      "name": "Тульская область",
      "city_count": 19,
      "people_count": 1851.6,
      "people_unit": "млн чел.",
      "min_point": 167,
      "max_point": 223,
      "avg_point": 194,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/587/thumb_3077_tulskaya_oblast.gif",
      "federal_district": "Центральный федеральный округ",
      "favorable_count": 53,
      "dynamiс": 11
  },
  {
      "id": 588,
      "name": "Тюменская область",
      "city_count": 5,
      "people_count": 1056.7,
      "people_unit": "тыс. чел.",
      "min_point": 180,
      "max_point": 240,
      "avg_point": 220,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/588/thumb_3078_tyumenskaya_oblast.png",
      "federal_district": "Уральский федеральный округ",
      "favorable_count": 80,
      "dynamiс": 0
  },
  {
      "id": 572,
      "name": "Удмуртская Республика",
      "city_count": 6,
      "people_count": 984.1,
      "people_unit": "тыс. чел.",
      "min_point": 171,
      "max_point": 220,
      "avg_point": 191,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/572/thumb_3060_respublika_udmurtiya.png",
      "federal_district": "Приволжский федеральный округ",
      "favorable_count": 50,
      "dynamiс": 17
  },
  {
      "id": 589,
      "name": "Ульяновская область",
      "city_count": 6,
      "people_count": 785.3,
      "people_unit": "тыс. чел.",
      "min_point": 179,
      "max_point": 215,
      "avg_point": 191,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/589/thumb_3079_ulianovskaya_oblast.png",
      "federal_district": "Приволжский федеральный округ",
      "favorable_count": 67,
      "dynamiс": 34
  },
  {
      "id": 590,
      "name": "Хабаровский край",
      "city_count": 7,
      "people_count": 960.4,
      "people_unit": "тыс. чел.",
      "min_point": 157,
      "max_point": 215,
      "avg_point": 187,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/590/thumb_3080_khabarovsky_kray.png",
      "federal_district": "Дальневосточный федеральный округ",
      "favorable_count": 43,
      "dynamiс": 0
  },
  {
      "id": 591,
      "name": "Ханты-Мансийский автономный округ",
      "city_count": 16,
      "people_count": 1403.6,
      "people_unit": "млн чел.",
      "min_point": 180,
      "max_point": 247,
      "avg_point": 204,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/591/thumb_3081_khanty_mansiisky_avtonomny_okrug.png",
      "federal_district": "Уральский федеральный округ",
      "favorable_count": 69,
      "dynamiс": 6
  },
  {
      "id": 592,
      "name": "Челябинская область",
      "city_count": 30,
      "people_count": 2742.5,
      "people_unit": "млн чел.",
      "min_point": 153,
      "max_point": 227,
      "avg_point": 193,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/592/thumb_3082_chelyabinskaya_oblast.png",
      "federal_district": "Уральский федеральный округ",
      "favorable_count": 47,
      "dynamiс": 7
  },
  {
      "id": 574,
      "name": "Чеченская Республика",
      "city_count": 6,
      "people_count": 566,
      "people_unit": "тыс. чел.",
      "min_point": 149,
      "max_point": 241,
      "avg_point": 175,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/574/thumb_3062_respublika_chechya.png",
      "federal_district": "Северо-Кавказский федеральный округ",
      "favorable_count": 33,
      "dynamiс": 0
  },
  {
      "id": 575,
      "name": "Чувашская Республика",
      "city_count": 9,
      "people_count": 769.2,
      "people_unit": "тыс. чел.",
      "min_point": 180,
      "max_point": 227,
      "avg_point": 208,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/575/thumb_3063_respublika_chuvashia.png",
      "federal_district": "Приволжский федеральный округ",
      "favorable_count": 89,
      "dynamiс": 22
  },
  {
      "id": 593,
      "name": "Чукотский автономный округ",
      "city_count": 3,
      "people_count": 25.5,
      "people_unit": "тыс. чел.",
      "min_point": 174,
      "max_point": 215,
      "avg_point": 190,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/593/thumb_3083_chukotsky_avtonomny_okrug.png",
      "federal_district": "Дальневосточный федеральный округ",
      "favorable_count": 33,
      "dynamiс": 0
  },
  {
      "id": 594,
      "name": "Ямало-Ненецкий автономный округ",
      "city_count": 8,
      "people_count": 445.2,
      "people_unit": "тыс. чел.",
      "min_point": 180,
      "max_point": 245,
      "avg_point": 211,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/594/thumb_3084_yamalo_nenetsky_avtonomny_okrug.png",
      "federal_district": "Уральский федеральный округ",
      "favorable_count": 75,
      "dynamiс": 12
  },
  {
      "id": 595,
      "name": "Ярославская область",
      "city_count": 11,
      "people_count": 957.4,
      "people_unit": "тыс. чел.",
      "min_point": 180,
      "max_point": 243,
      "avg_point": 214,
      "emblem_url": "https://api.индекс-городов.рф/uploads/region/emblem/595/thumb_3085_yaroskavskaya_oblast.png",
      "federal_district": "Центральный федеральный округ",
      "favorable_count": 91,
      "dynamiс": 27
  }
]