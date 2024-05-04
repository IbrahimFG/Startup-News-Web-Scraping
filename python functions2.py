def greet(name):
    print(f"hi {name}")

def get_greeting(name):
    return f"hi {name}"

message = get_greeting("ibrahim")
file = open("content.txt", "w")
file.write(message)