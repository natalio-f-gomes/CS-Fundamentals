Username: natalio| Password: 1234
Username: dfkmf| Password: 132e
    
    
def add():
    user = input("Enter the username: ")
    pwd = input("Enter the password: ")
    with open("database.txt", "a") as f:
        f.write("Username: " + user + "| Password: " + pwd+ "\n" )
def view():
    with open("database.txt", "r") as r:
        for i in r.readlines():
            print(i.rstrip())
def loop():
    while True:
        print("Hello. Would you like to add password or view existent ones?")
        choice = input("Valid  Options:\nadd\nview\n'q' for quit the program:\n")
        if choice == "q":
            break
        if choice == "add":
            add()
        elif choice == 'view':
            view()
        
        else:
            continue

print(loop())
