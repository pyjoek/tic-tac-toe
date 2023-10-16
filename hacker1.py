dis = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
        ] 

for i in dis:
    print(i)

def load():
    first = input("Name of the first player < use x as mark > : ")
    second = input("Name of the second player < use o as mark > : ")
    print('LET THE CHALLENGE BEGIN')
    while True:
        user = input("Enter the location and the mark [O || X] >>> ")
        if len(user) > 3:
            print("example; 0 x")
        elif len(user) < 3:
            print("example; 0 x")
        elif user == "stop":
            break

        if int(user[0]) <= 3:
            if user[0] in dis[0]:
                dis[0][int(user[0]) - 1] = user[2]
        if int(user[0]) <= 6:
            if user[0] in dis[1]:
                dis[1][int(user[0]) - 4] = user[2]
        if int(user[0]) <= 9:
            if user[0] in dis[2]:
                dis[2][int(user[0]) - 7] = user[2]

        for i in dis:
            print(i)

        if dis[0][0] == dis[1][1] and dis[1][1] == dis[2][2]:
            if dis[0][0] == 'x':
                print(f"{first} WON!!")
                break
            elif dis[0][0] == 'o':
                print(f'{second} WON!!')
                break
        elif dis[0][0] == dis[0][1] and dis[0][1] == dis[0][2]:
            if dis[0][0] == 'x':
                print(f"{first} WON!!")
                break
            elif dis[0][0] == 'o':
                print(f'{second} WON!!')
                break
        elif dis[0][0] == dis[1][0] and dis[1][0] == dis[2][0]:
            if dis[0][0] == 'x':
                print(f"{first} WON!!")
                break
            elif dis[0][0] == 'o':
                print(f'{second} WON!!')
                break
        elif dis[0][2] == dis[1][1] and dis[1][1] == dis[2][0]:
            if dis[0][2] == 'x':
                print(f"{first} WON!!")
                break
            elif dis[0][2] == 'o':
                print(f'{second} WON!!')
                break
        elif dis[2][2] == dis[2][1] and dis[2][1] == dis[2][0]:
            if dis[2][2] == 'x':
                print(f"{first} WON!!")
                break
            elif dis[2][2] == 'o':
                print(f'{second} WON!!')
                break
        elif dis[0][2] == dis[1][2] and dis[1][2] == dis[2][2]:
            if dis[0][2] == 'x':
                print(f"{first} WON!!")
                break
            elif dis[0][2] == 'o':
                print(f'{second} WON!!')
                break
        elif dis[0][1] == dis[1][1] and dis[1][1] == dis[2][1]:
            if dis[0][1] == 'x':
                print(f"{first} WON!!")
                break
            elif dis[0][1] == 'o':
                print(f'{second} WON!!')
                break

load()
