
print("This program will build a glossary of your choice.")
word_intro = input("Enter a word: ")
definition_intro = input("Enter the definition: ")

dictionary = {}
dictionary[word_intro]=definition_intro
while True:
    choice = input("Press 'c' to continue with another entry, or a different key to quit. ")
    if choice =="c":
        word = input("Enter a word: ")
        definition = input("Enter the definition: ")
        dictionary[word]=definition
    else:
        break
 print("Your glossary is: )
for key, value in dictionary.items():

    print(f"{key} : {value}")
