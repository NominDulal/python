#Q1. star pattern
# rows=5
# for i in range(1,rows+1)
# print("*"*i)

#Q2. opposite star pattern
# data=5
# for i in range(1,6):
#     print("*"*data)
#     data=data-1

#Q3. right star pattern 
# space=4
# for i in range(1,6):
#     print(" "*space + "*"*i)
#     space=space-1

#Q4. 1111
# 2222
# 3333
# 4444
 
# for i in range(1,5):
#     print(str(i)*5)

# Q.5 pattern problem
# A
# AB
# ABC
# ABCD
# ABCDE
# ABCDEF
# char(65)->A

# for i in range(6):
#     character=65
#     for j in range(i+1):
#         print(chr(character),end="")
#         character+=1
#     print()

# Q.6
# A
# BB
# CCC
# DDDD
# EEEEE
# FFFFFF
# for i in range(6):
#     character=65
#     rows=i+1
#     print(chr(65+i)*rows)

# Q.7
# AAAAAA
# BBBBB
# CCCC
# DDD
# EE
# F
# character=65
# i=6
# for j in range(1,7):
#     print(chr(character)*i)
#     i-=1
#     character+=1

# Q.no 8 
#     1
#    222
#   33333
#  4444444
# 555555555
# space=4
# number=1
# for i in range(1,6):
#     print(" "*space + str(i)*number)
#     space-=1
#     number+=2

# Q.no 9
#    1
#   22
#  333
# 4444
#55555
# icount=1
# for i in range(1,6):
#     space=5-i
#     print(" " * space + f"{i}"*icount)
#     icount+=1

# q no.10
# 1
# 23
# 456
# 78910
# 1112131415
# count=1
# for i in range(1,6):
#     for j in range(i):
#         print(count,end="")
#         count+=1
#     print()