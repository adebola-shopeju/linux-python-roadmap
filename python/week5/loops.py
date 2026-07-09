for number in range(5):
    print(number)

for number in range(1, 6):
    print(number)
print("Start")

for number in range(3):
    print(number)

print("Finished")

services = ["EC2", "S3", "Lambda", "RDS"]

for service in services:
    print(service)

services = ["EC2", "S3", "Lambda", "RDS"]

for service in services:
    print("I am learning", service)

for number in range(1, 21):
    print(number)

for number in range(1, 21):
    print("Checking server", number)

print(4 % 2)

print(5 % 2)

for number in range(1, 11):
    if number % 2 != 0:
        print(number)

count = 1
while count <= 5:
    print(count)
    count = count + 1

count = 1
while count <= 10:
    if count == 5:
        break
    print(count)
    count = count + 1

count = 0
while count < 10:
    count = count +1
    if count % 2 == 0:
        continue
    print(count)