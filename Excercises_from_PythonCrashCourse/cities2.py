def describe_city(city_name, country_name= 'india'):
    """Display information about a city"""
    print(f"{city_name.title()} is in {country_name.title()}")


describe_city('chandigarh')
describe_city('behror')
describe_city('new york', 'america')