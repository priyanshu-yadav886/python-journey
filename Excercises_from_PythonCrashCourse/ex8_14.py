def build_car(manifacturar, model_name, **car_info):
    """Build a car with the info user wants to."""
    car_info['manifacturar'] = manifacturar
    car_info['model_name'] = model_name
    return car_info

car = car = build_car('subaru', 'outback', color='blue', tow_package=True)

print(car)