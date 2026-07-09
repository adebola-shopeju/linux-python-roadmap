number = input("Give me a number: ")
number = int(number)
if number > 0:
    print("That's a positive number!")
elif number < 0:
    print("That's a negative number!")
else:
    print("That's zero!")
region = input("What is your AWS region? (e.g. us-east-1): ")
print(f"Your endpoint is: https://ec2.{region}.amazonaws.com")