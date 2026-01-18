cities = {
    'pawai' : {
        'country' : 'india',
        'population' : '40m',
        'fact' : 'It is a large city'
    },


    'madero' : {
        'country' : 'mexico',
        'population' : '5m',
        'fact' : 'It is a small city'
    },


    'arriach' : {
        'country' : 'austria',
        'population' : '20m',
        'fact' : 'It is a medium city'
    },
}

for city, info in cities.items():
    print(f"\n{city.title()}")
    for abouts, real_info in info.items():
        print(f"\t{abouts.title()} : {real_info.title()}")