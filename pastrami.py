sandwich_orders = ['pastrami', 'club', 'pastrami', 'grilled', 'cheese', 'pastrami']
finished_orders = []
print("The Deli has run out of Pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"\nI made a {sandwich} sandwich for you.")
    finished_orders.append(sandwich)

print("--finished orders--")
for sandwhich in finished_orders:
    print(f"\t{sandwhich}")