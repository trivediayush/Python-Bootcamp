a = 31

for i in range(1,51,2):
    if i == a:
        break
    print(i)

while True:
    a = "hello...."
    print(a)
    user_input = input("Type 'stop' to end: ")
    if user_input.lower() == "stop":
        break
