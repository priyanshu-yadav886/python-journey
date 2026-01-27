message = input("How many people are in your group: ")
print(message)

message = int(message)

if message > 8:
    print("Sir you will have to wait for a table.")

else:
    print("You can have your seat sir.")