from city_function import city_country

def test_city_country():
    cities = city_country('changsha', 'china')
    assert cities == 'Changsha，China。'

def test_city_country_population():
    cities = city_country('shanghai', 'china', 15_000_000)
    assert cities == 'Shanghai，China-population 15000000。'