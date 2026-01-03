def dictionaries():
    name = "defend the east wall of the castle"
    encrypted_name = ''
    decrypted_name = ''
    key_dict_decrypt = {"a": "z",
                        "b": "a",
                        "c": "b",
                        "d": "c",
                        "e": "d",
                        "f": "e",
                        "g": "f",
                        "h": "g",
                        "i": "h",
                        "j": "i",
                        "k": "j",
                        "l": "k",
                        "m": "l",
                        "n": "m",
                        "o": "n",
                        "p": "o",
                        "q": "p",
                        "r": "q",
                        "s": "r",
                        "t": "s",
                        "u": "t",
                        "v": "u",
                        "w": "v",
                        "x": "w",
                        "y": "x",
                        "z": "y",
                        " ": " "}

    key_dict_encrpyt = {"a": "b",
                        "b": "c",
                        "c": "d",
                        "d": "e",
                        "e": "f",
                        "f": "g",
                        "g": "h",
                        "h": "i",
                        "i": "j",
                        "j": "k",
                        "k": "l",
                        "l": "m",
                        "m": "n",
                        "n": "o",
                        "o": "p",
                        "p": "q",
                        "q": "r",
                        "r": "s",
                        "s": "t",
                        "t": "u",
                        "u": "v",
                        "v": "w",
                        "w": "x",
                        "x": "y",
                        "y": "z",
                        "z": "a"}

    # print(key_dict_encrpyt["l"]) # How to index a dictionary

    for letter in name:
        # print(letter, end="")
        # print(key_dict_encrpyt[letter])
        if letter == " ":
            encrypted_name += " "
        else:
            encrypted_name += key_dict_encrpyt[letter]
        print(name)
        print(encrypted_name)
    for letter in encrypted_name:
        # spaces are handled inside the dictionary
        decrypted_name += key_dict_decrypt[letter]
    print(encrypted_name)
    print(decrypted_name)
    # for key in key_dict_encrpyt:
    #     print(key, key_dict_encrpyt[key])


dictionaries()
