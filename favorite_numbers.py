favorite_numbers = {
    'prince' : [2, 3],
    'priyanshu' : [6, 10],
    'anuj' : [30, 35],
    'ajay' : [80, 85],
    'rahul' : [100, 101],

}
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
