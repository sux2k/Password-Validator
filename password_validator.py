#Password Validator

numbers = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
while True:
   
    password = input("Enter Password: ")

    if len(password) < 10:
        print("Error, the password must be at least 10 characters")
        continue
    elif " " in password:
        print("Error, the password must not contain spaces ")
        continue
    elif  not any(char in numbers for char in password):
        print("Error, the password must contain at least one number")
        continue
        print("Your password is: ", password)
    
    changePassword = input("Do you want to change password? ").lower()
    if changePassword == "yes":
        continue
    else:
        break
print("Your password is: ", password)
