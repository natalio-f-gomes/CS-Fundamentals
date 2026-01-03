

def file_handling():

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

   

    print("*** Simple Substitution Cipher Tool ***")
    
    origin_file = input("Please enter the name of file including the plain text: ")
    
    encrypted_file = input("Please enter the name of file including encrypted text: ")
    decrypted_file =  input("Please enter the name of file including decrypted text: ")
    
    try:
        with open(origin_file,"r") as origin_file :
            origin_file = origin_file.read()
        with open(encrypted_file,"r") as encrypted_file_readable :
            encrypted_file_readable = encrypted_file_readable.read()
            
        encrypted_file = open(encrypted_file, "a")
        decrypted_file = open(decrypted_file, "a")
        
        for letter in origin_file:
            if letter == " ":
                encrypted_file.write(" ")
            else:
                encrypted_file.write(key_dict_encrpyt[letter])
        for letter in encrypted_file_readable:
            if letter == " ":
                decrypted_file.write(" ")
            else:
                decrypted_file.write(key_dict_decrypt[letter])
        print("Encrypted and decrypted texts have been written to encrypted.txt and decrypted.txt respectively.")
       
               
    except Exception as err:
        print(err)
   

   
     

    
file_handling()


   

