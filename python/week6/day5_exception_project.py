try:
    servers = int(input("How many servers do you want to deploy? "))

    if servers == 0:
        raise Exception("Cannot deploy with zero servers")

except ValueError:
    print("Please enter a number")

except Exception as error:
    print(error)

else:
    print("Deploying", servers, "servers")

finally:
    print("Deployment check complete")