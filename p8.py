



# n=4                  *    
#                      * *
#              ****eeee* * *
#         *    ****    * *
#       * *    ****    *
#     * * *eeee****
#       * *
#         *
        

n=8

for i in range(n//2):
    for j in range(3*n+n//2+1):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()

for i in range(1):
    for j in range(n+n//2+1):
        print(' ',end='')
    for j in range(n):
        print('*',end='')
    for j in range(n):
        print('e',end='')
    print('*',end='')
    for j in range(n//2-1):
        print('*',end='')
    print('*')
    
for i in range(n//2):
    for j in range(n//2-i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    for j in range(n):
        print(' ',end='')
    for j in range(n):
        print('*',end='')
    for j in range(n):
        print(' ',end='')
    for j in range(n//2-i):
        print('*',end='')
    print()
    
for i in range(1):
    print('*',end='')
    for j in range(n//2-1):
        print('*',end='')
    print('*',end='')
    for j in range(n):
        print('e',end='')
    for j in range(n):
        print('*',end='')
    print()

for i in range(n//2):
    for j in range(i+1):
        print(' ',end='')
    for j in range(n//2-i):
        print('*',end='')
    print()







