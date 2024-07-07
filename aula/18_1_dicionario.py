dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
phone_numbers = {'chefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

for key in dictionary:
    print(key, "->", dictionary[key])

for key in phone_numbers:
    print(key, "->", phone_numbers[key])
