# Dictionary containing usernames and passwords  
users = {  
    "user1": "pass1",  
    "user2": "pass2",  
    "user3": "pass3",  
    "user4": "pass4",  
    "user5": "pass5",  
    "user6": "pass6",  
    "user7": "pass7",  
    "user8": "pass8",  
    "user9": "pass9",  
    "user10": "pass10"  
}  

# Ask for username and password  
username = input("Enter your username: ")  
password = input("Enter your password: ")  

# Check if the username exists  
if username not in users:  
    print("You are not a valid user of the system.")  
else:  
    # Check if the password is correct  
    if users[username] == password:  
        print("You are now logged in to the system.")  
    else:  
        print("The password is invalid.")  
