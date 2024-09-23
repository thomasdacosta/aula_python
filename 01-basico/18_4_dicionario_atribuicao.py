dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}

dictionary['swan'] = 'cygne'
print(dictionary)

dictionary.update({"pato": "canard"})
print(dictionary)

del dictionary['cachorro']
print(dictionary)

pol_eng_dictionary = {"kwiat": "flor"}

pol_eng_dictionary.update({"gleba": "solo"})
print(pol_eng_dictionary)  # saídas: {'kwiat': 'flor', 'gleba': 'solo'}

pol_eng_dictionary.popitem()
print(pol_eng_dictionary)  # saídas: {'kwiat': 'flor'}

