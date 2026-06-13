class Server:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def __setattr__(self, key, value):
        if key == "port" and not 0 <= value <= 65535:
            raise ValueError("Port must be between 0 and 65535")
        else:
            object.__setattr__(self, key, value)


    def __getattr__(self, key):
        return None

s = Server("localhost", 8080)
print(s.port)      # 8080
print(s.database)  # None
