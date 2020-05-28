size = int(input("Enter size of list:"))
print("Enter list elements(0/1):")
list=[]
for i in range(size):
    list.append(int(input()))

print("Original list={} Sorted List={}".format(list,sorted(list)))
