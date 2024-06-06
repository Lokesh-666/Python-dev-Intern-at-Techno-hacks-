import random
import string

# Function to generate a password of given length.
def generate_password(password_length): 
    
    password = ""
    for i in range(password_length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password 

def main():
    print("Do you want to generate a password?")
    answer = input("Y/N? ")
    if answer.upper() == "Y":
        password_length = int(input("How long do you want your password to be? ")) 
        password = generate_password(password_length) 
        print("The Password with length "+ str(password_length) +" is:")
        print() 
        print(password)
        print() 
    elif answer.upper() =="N":
        print("Okay, goodbye!")
        exit()
    else:
        print("Sorry, I didn't understand that. Goodbye!")
        exit()

if __name__ == '__main__':
    main()