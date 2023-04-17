cities_final = []

def get_cities():
    cities = [
        {"city": "Albuquerque", "state": "NM", "zip": "87102", "population": 559277},
        {"city": "Anaheim", "state": "CA", "zip": "92801", "population": 345012},
        {"city": "Anchorage", "state": "AK", "zip": "99501", "population": 291826},
        {"city": "Arlington", "state": "TX", "zip": "76010", "population": 398121},
        {"city": "Atlanta", "state": "GA", "zip": "30303", "population": 486290},
        {"city": "Aurora", "state": "CO", "zip": "80010", "population": 325078},
        {"city": "Austin", "state": "TX", "zip": "78701", "population": 931830},
        {"city": "Bakersfield", "state": "CA", "zip": "93301", "population": 372576},
        {"city": "Baltimore", "state": "MD", "zip": "21202", "population": 602495},
        {"city": "Boston", "state": "MA", "zip": "02108", "population": 667137},
        {"city": "Buffalo", "state": "NY", "zip": "14202", "population": 258959},
        {"city": "Charlotte", "state": "NC", "zip": "28202", "population": 872498},
        {"city": "Chicago", "state": "IL", "zip": "60602", "population": 2695598},
        {"city": "Cincinnati", "state": "OH", "zip": "45202", "population": 296943},
        {"city": "Cleveland", "state": "OH", "zip": "44113", "population": 390113},
        {"city": "Colorado Springs", "state": "CO", "zip": "80903", "population": 456568},
        {"city": "Columbus", "state": "OH", "zip": "43215", "population": 822553},
        {"city": "Dallas", "state": "TX", "zip": "75201", "population": 1345047},
        {"city": "Denver", "state": "CO", "zip": "80202", "population": 682545},
        {"city": "Detroit", "state": "MI", "zip": "48226", "population": 672662},
        {"city": "El Paso", "state": "TX", "zip": "79901", "population": 674433},
        {"city": "Fort Worth", "state": "TX", "zip": "76102", "population": 792727},
        {"city": "Fresno", "state": "CA", "zip": "93721", "population": 509924},
        {"city": "Houston", "state": "TX", "zip": "77002", "population": 2296224},
        {"city": "Indianapolis", "state": "IN", "zip": "46204", "population": 843393},
        {"city": "Jacksonville", "state": "FL", "zip": "32202", "population": 842583},
        {"city": "Kansas City", "state": "MO", "zip": "64102", "population": 467007},
        {"city": "Las Vegas", "state": "NV", "zip": "89101", "population": 603488},
        {"city": "Long Beach", "state": "CA", "zip": "90802", "population": 462257},
        {"city": "Los Angeles", "state": "CA", "zip": "90001", "population": 3971883},
        {"city": "Louisville", "state": "KY", "zip": "40202", "population": 609893},
        {"city": "Memphis", "state": "TN", "zip": "38103", "population": 653450},
        {"city": "Mesa", "state": "AZ", "zip": "85201", "population": 508958},
        {"city": "Miami", "state": "FL", "zip": "33128", "population": 463347},
        {"city": "Milwaukee", "state": "WI", "zip": "53202", "population": 594833},
        {"city": "Minneapolis", "state": "MN", "zip": "55402", "population": 410939},
        {"city": "Nashville", "state": "TN", "zip": "37203", "population": 654610},
        {"city": "New York", "state": "NY", "zip": "10007", "population": 8405837},
        {"city": "Newark", "state": "NJ", "zip": "07102", "population": 281944},
        {"city": "Oakland", "state": "CA", "zip": "94607", "population": 406253},
        {"city": "Oklahoma City", "state": "OK", "zip": "73102", "population": 631346},
        {"city": "Omaha", "state": "NE", "zip": "68102", "population": 434353},
        {"city": "Philadelphia", "state": "PA", "zip": "19107", "population": 1526006},
        {"city": "Phoenix", "state": "AZ", "zip": "85003", "population": 1445632},
        {"city": "Pittsburgh", "state": "PA", "zip": "15222", "population": 305841},
        {"city": "Portland", "state": "OR", "zip": "97201", "population": 609456},
        {"city": "Raleigh", "state": "NC", "zip": "27601", "population": 403892},
        {"city": "Sacramento", "state": "CA", "zip": "95814", "population": 479686},
        {"city": "San Antonio", "state": "TX", "zip": "78205", "population": 1327407},
        {"city": "San Diego", "state": "CA", "zip": "92101", "population": 1307402},
        {"city": "San Francisco", "state": "CA", "zip": "94102", "population": 805235},
        {"city": "San Jose", "state": "CA", "zip": "95113", "population": 998537},
        {"city": "Seattle", "state": "WA", "zip": "98101", "population": 608660},
        {"city": "St. Louis", "state": "MO", "zip": "63102", "population": 319294},
        {"city": "Tampa", "state": "FL", "zip": "33602", "population": 335709},
        {"city": "Tucson", "state": "AZ", "zip": "85701", "population": 520116},
        {"city": "Virginia Beach", "state": "VA", "zip": "23451", "population": 448479},
        {"city": "Washington", "state": "DC", "zip": "20001", "population": 601723},
    ]

    return cities

def prepare_cities(cities):

    total_population = 0 # 51,035,885
    for city in cities:
        total_population += city["population"]

    for city in cities:
        city["population_pcnt"] = (city["population"] / total_population)

    global cities_final
    cities_final = sorted(cities, key=lambda d: d["population"], reverse=True)

    running_total = 1
    for city in cities_final:
        running_total -= city["population_pcnt"]
        city["running_total"] = running_total


def get_city(rnd_value):

    for city in cities_final:
        if rnd_value >= city["running_total"]:
            return city

# 1x at start
cities = get_cities()
prepare_cities(cities)

print(get_city(0.950))