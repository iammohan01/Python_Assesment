
password = input()

if password :
    print('Logged in ..!')
    password = bool(input())
    print(type(password))
else :
    print("Wrong Password . Try Again !")
   