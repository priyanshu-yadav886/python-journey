sandwich_orders = ['club', 'grilled', 'cheese']
finished_sandwhiches = []

while sandwich_orders:
    sandwhich = sandwich_orders.pop()

    print(f"\nI made you a {sandwhich} sandwich.")
    finished_sandwhiches.append(sandwhich)

print("\n--List of finished sandwiches--")
for finished in finished_sandwhiches:
    print(f"\t{finished}")