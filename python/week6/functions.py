def gb_to_mb(gb):
    mb = gb * 1024
    return mb

server_storage = gb_to_mb(20)

print(server_storage)

def check_server(status):
    return status

server_status = check_server("Running")