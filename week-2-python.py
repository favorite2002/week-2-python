my_list = []                                 #empty list

my_list.append(10)
print(my_list)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)                               #[10,20,30,40]

my_list.insert(1,15)                         #15 is inserted in position 2(index 1)
print(my_list)

my_list.extend([50,60,70])
print(my_list)                               #[10,15,20,30,40,50,60,70]

my_list.pop()                                #remove last element
print(my_list)

my_list.sort()                               #sort list in ascending order
print(my_list)

print(my_list.index(30))                     #3

