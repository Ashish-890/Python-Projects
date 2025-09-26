from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key() 
fer = Fernet(key)

# Here "passcode" is the variable that stores the user's input for the master password
# Here "mode" is the variable that stores the user's input for choosing to add or view passwords

def view():
    with open("passwords.txt", "r") as f:
         for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split(" | ")
            print("User:", user, ", Password:", fer.decrypt(passw.encode()).decode())
           

            
            # def stand for define
            # it is used to create a function(a block of code that only runs when it is called)
            # here "view" is the name of the function
            # view() is used to call the function, calling the function will execute the code inside the function
   

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open("passwords.txt", "a") as f:  # r is for read, w is for write, a is for append
        
        # open("passwords.txt", 'a') is used to open or create a file named "passwords.txt" in append mode
        # 'a'append mode means that new data will be added to the end of the file without deleting existing data
        # f is just a variable name You can name it anything, like file, myfile, etc. 
        # This variable represents the open file, so you can read or write to it.
        # with is used to ensure that the file is properly closed after its suite finishes, even if an exception is raised

        f.write(name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")

            # "f" is the variable that represents the open file
            # Whatever string you put inside the write() function will be written to the file
            # name + " | " + pwd + "\n" here : name is the account name, 
                                             # " | " is just a separator for better readability,
                                             #  pwd is the password, and 
                                             # "\n" is used to add a new line after writing the entry to the file
                                             # + means concatenate or join together




while True :                                
    mode = input("Would you like to add a new password or view existing passwords? (add/view), press 'q' to quit! ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode. Please choose 'add' or 'view'.")
        continue