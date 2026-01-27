def city_country(city_name, country_name):
    """Return a pair of city and country"""
    city = f"\"{city_name}, {country_name}\""
    return city.title()

result = city_country('jaipur', 'india')
print(result)