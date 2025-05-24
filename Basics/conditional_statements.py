age = 5

if age>18:
    print("Yes, you can vote...")
else:
    print("No you are too young, you can not vote....")

if age>18:
    print("you can drive car...")
elif age<18 and age>15:
    print("you can learn driving....")
else:
    print("you are a child, drive toy car not real one...")


order = 'cheese-bust pizza'

if 'pizza' in order:
    if order == 'cheese-bust pizza':
        print("Bring cheese-bust pizza with extra cheese...")
    elif order == 'pizza with coke':
        print("Bring pizza with extra sauce and coke")
    else:
        print("What else do you have...")
else:
    print("Bring pizza")

order2 = 'coke'
response = "Bring pizza" if order2 == 'pizza' else "Bring something else"
print(response)
