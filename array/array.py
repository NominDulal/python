listodd=[]
list1=[21,34,54,56,78]
list2=[43,65,213,667,76]
list3=[65,56,231,5,67]
list4=[list1,list2,list3]
for x in range(len(list4)):
    for y in range(len(list4[x])):
        if (list4[x])[y]%2!=0:
            listodd.append((list4[x])[y])
            # listodd+=(list4[x])[y]

print(listodd)



