dis = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
        ] 

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