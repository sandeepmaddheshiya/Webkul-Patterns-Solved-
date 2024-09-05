
# n=3

# @       
# @@      @@@
# @@@*****@@@
# @@      @@@
# @       


# n=5

# @          
# @@         @@@@@
# @@@        @@@@@
# @@@@*******@@@@@
# @@@        @@@@@
# @@         @@@@@
# @     

n=5
for i in range(n//2+2):
    for j in range(i+1):
        print("@",end='')
    for j in range(n//2+1-i):
        print(' ',end='')
    for j in range(n+2):
        if(i==n//2+1):
            print('*',end='')
        else:
            print(' ',end='')
    for j in range(n):
        if(i>0):
            print('@',end='')
        else:
            print(' ',end='')
    print()
for i in range(n//2+1):
    for j in range(n//2-i+1):
        print('@',end='')
    for j in range(i+1):
        print(' ',end='')
    for j in range(n+2):
        print(' ',end='')
    for j in range(n):
        if(i<n//2):
            print('@',end='')
        else:
            print(' ',end='')
    
    print()