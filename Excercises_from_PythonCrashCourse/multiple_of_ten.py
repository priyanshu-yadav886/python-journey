message = input("Enter you number: ")

print(message)
message = int(message)

if message % 10 == 0:
    print(f"The number {message} is a multiple of 10.")

else:
    print(f"The number {message} is not a multiple of 10.")