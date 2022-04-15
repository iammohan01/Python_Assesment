from asyncio.windows_events import NULL


print('\n\nHello mohan !\n \ndo you want to add todo ? \nif yes enter 1 . else 0 \n'.title()  )
x = int(input('Enter here : '))
todo = []

user_input = x
while user_input == 1 :
        if x==1 :
            todo.append(input("Enter todo Here : "))
            print('Want to add more ? Enter 1 for add 0 for exit')
            user_input = int(input())
        
        elif x==0 :
            user_input == 0
            print()

if todo.__len__() != 0:
    print('Your todo list : ' )
    for i in range(0,todo.__len__()) :
        print('     * ' + todo[i])
else :
    print('Your To List Was Empty....!')
d 