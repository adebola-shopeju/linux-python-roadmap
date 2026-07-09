instance_ids = ["i-101", "i-102", "i-103"]
print(instance_ids[1])
print(instance_ids[0:2])

instance_ids.append("i-104")
print(instance_ids)

instance_ids.append("i-105")
instance_ids.append("i-106")
print(instance_ids)

instance_ids.remove("i-103")
print(instance_ids)

instance_ids.sort()
print(instance_ids)

instance_ids.append("i-100")
print(instance_ids)
instance_ids.sort()
print(instance_ids)

print(instance_ids[0:3])