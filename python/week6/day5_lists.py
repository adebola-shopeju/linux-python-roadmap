aws_services = ["EC2", "S3", "Lambda", "RDS"]

print(aws_services)

print(aws_services[2])

aws_services[3] = "DynamoDB"
print(aws_services)

aws_services.append("CloudFront")
print(aws_services)

aws_services.remove("CloudFront")
print(aws_services)

aws_services = ["EC2", "S3", "Lambda", "DynamoDB"]
print(len(aws_services))

servers = ["web-server-1", "web-server-2", "api-server-1"]
print(servers)

servers.append("database-server-1")
print(servers)

servers[1] = "web-server-prod"
print(servers)