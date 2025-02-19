for i in range(7,0,-2):
    print(" "*(7-i),end=" ");
    for j in range(i):
        if(j%2==0):
            print(1,end=" ");
        else:
            print(0,end=" ");
    print();