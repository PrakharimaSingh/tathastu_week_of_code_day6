num = int(input("Enter number of lists:"))
size =int(input("Enter size of each list:"))
lists=[]
for i in range(num):
    print("Enter elements in list",i+1)
    li=[]
    for j in range(size):
        li.append(int(input("Enter element:")))
    lists.append(sorted(li))

print("The sorted sub lists are:")
for i in range(num):
    print(lists[i])


sorted_list=[]
for i in range(num):
    for j in range(size):
        sorted_list.append(lists[i][j])


print("The sorted final list is:",sorted(sorted_list))
