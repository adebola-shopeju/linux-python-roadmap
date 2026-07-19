try:
    servers = 0

    if servers == 0:
        raise Exception("No servers available")

    print("Deployment started")

except Exception as error:
    print(error)