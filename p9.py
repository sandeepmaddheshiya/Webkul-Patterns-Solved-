# n=3

#               *
#               **
#       ****eeee***
#       ****    **
#  *eeee****    *
# **
#***
# **
#  *

# n=5
#                      *
#                      **
#                      ***
#          ******eeeeee****
#          ******      ***
#          ******      **
#   *eeeeee******      *
#  **
# ***
#****
# ***
#  **
#   *

n=7
#                              *
#                              **
#                              ***
#                              ****
#              ********eeeeeeee*****
#              ********        ****
#              ********        ***
#              ********        **
#     *eeeeeeee********        *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *


for i in range(n//2+1):
    for j in range(n//2+2+3*(n+1)):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()
print(' '*((n//2+2)+(n+1))+'*'*(n+1)+'e'*(n+1)+'*'*(n//2+2))
for i in range(n//2):
    for j in range(n//2+2+n+1):
        print(' ',end='')
    for j in range(n+1):
        print('*',end='')
    for j in range(n+1):
        print(' ',end='')
    for j in range(n//2+1-i):
        print('*',end='')
    print()
print(' '*(n//2+1)+'*'+'e'*(n+1)+'*'*(n+1)+' '*(n+1)+'*')
for i in range(n//2+1):
    for j in range(n//2-i):
        print(' ',end='')
    for j in range(2+i):
        print('*',end='')
    print()
for i in range(n//2+1):
    for j in range(i+1):
        print(' ',end='')
    for j in range(n//2+1-i):
        print('*',end='')
    print()
        