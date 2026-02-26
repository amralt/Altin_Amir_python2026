def plus_one(l):
    for i in range(len(l)-1, 0, -1) :
        if l[i] !=9:
            l[i] += 1
            break
    print(l)

plus_one([4,3,2,1])