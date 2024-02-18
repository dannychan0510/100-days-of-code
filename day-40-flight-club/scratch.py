search_params = {
            "fly_from": "city:TYO",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 21,
            "min_stopovers": 0,
            "curr": "JPY",
            "one_for_city": 1,
        }

search_params['min_stopovers'] = 100

for k, i in search_params.items():
    print(f'{k}, {i}')