## Zip function

user_id = ["user1", "user2", "user3"]
names= ["Anoop", "Shalini", "Pi"]
last_name = ["Sheoran", "Mitra", "MitraSheoran"]

print(list(zip(user_id, names, last_name)))
print(dict(zip(user_id, names)))
print(tuple(zip(user_id, names)))




l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]

l = [(1, 2), (3, 4), (5, 6), (7, 8)]

new_list= []
new_list1= []
l3, l4 = list(zip(*l))
print(list(l3))
print(list(l4))

for i in zip(l1, l2):
    new_list.append(max(i))
print(new_list)



for i in zip(l1, l2):
    new_list1.append(min(i))
print(new_list1)