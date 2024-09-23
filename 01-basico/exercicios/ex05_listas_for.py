my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list.remove(1)
my_list.pop(5)
print(my_list)
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Elemento encontrado no índice", i)
else:
    print("ausente")
