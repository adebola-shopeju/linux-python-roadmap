aws_services = {
    "EC2": "Virtual servers",
    "S3": "Object storage",
    "IAM": "Permissions",
    "VPC": "Private networking",
    "RDS": "Managed database",
}

print("Entire dictionary:")
print(aws_services)

print()

print("Single values:")
print(aws_services["EC2"])
print(aws_services["S3"])
print(aws_services["VPC"])
print(aws_services["RDS"])
print()

print("Looping through keys and values:")
for service, description in aws_services.items():
    print(service, "→", description)