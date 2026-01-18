glossary = {
  'nile' : 'egypt',
  'sindhu' : 'india',
  'amazon' : 'america'  
}
for river, country in glossary.items():
    print(f"the {river.title()} runs through {country.title()}")

for river in glossary.keys():
    print(river.title())

for country in glossary.values():
    print(country.title())