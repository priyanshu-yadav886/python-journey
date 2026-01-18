def make_sandwich(*sandwichs):
    """Print the list of sandwiches that has been requested"""
    print("The sandwich that has been requested")
    for sandwich in sandwichs:
        print(f"\t-{sandwich}")

make_sandwich('cheese', 'grilled', 'capcicum')