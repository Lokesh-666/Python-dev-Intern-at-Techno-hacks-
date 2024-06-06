import time
Accounts = {'1': {'pin':1111, 'Name':'A','Balance': 0}, 
            '2': {'pin':2222, 'Name':'B','Balance': 0},
            '3': {'pin':3333, 'Name':'C','Balance': 0},
            '4': {'pin':4444, 'Name':'D','Balance': 0},
            '5': {'pin':5555, 'Name':'E','Balance': 0},
            }

def AccountNumberValidity(accountNumber):
    # validity = False
    if accountNumber in Accounts:
        validity = True
    else:
        validity = False
    return validity

def PinValidity(accountNumber, UserGivenPin):
    validity = False
    if Accounts[str(accountNumber)]['pin'] == UserGivenPin:
        validity = True
    return validity

def printAllFunctionality():
    print("1. Check Balance (C)")
    print("2. Withdraw (W)")
    print("3. Deposit (D)")
    print("4. Quit (Q)")

def CheckBalance(accountNumber):
    return Accounts[str(accountNumber)]['Balance']

def Withdraw(accountNumber):
    print("Your Bank Balance is $", CheckBalance(accountNumber))
    amountToWithdraw = int(input("How much do you wish to withdraw?"))
    if CheckBalance(accountNumber) >= amountToWithdraw:
        print("Here you go Dear Customer!!")
        Accounts[str(accountNumber)]['Balance'] = Accounts[str(accountNumber)]['Balance']-amountToWithdraw
        print("Your Account has now balance of $", Accounts[str(accountNumber)]['Balance'])
    else:
        print("You do not have enough balance!!")
        print("Sorry :(")

def Deposit(accountNumber):
    print("Your Bank Balance is $", CheckBalance(accountNumber))
    amountToDeposit = int(input("How much do you wish to Deposit? "))
    if amountToDeposit >0:
        Accounts[str(accountNumber)]['Balance'] = Accounts[str(accountNumber)]['Balance']+amountToDeposit
        print("Your Bank Balance after deposition is $", CheckBalance(accountNumber))

    else:
        print("You can not deposit negative amount of money!!")

def DoAccountFunctions(accountNumber):
    while(1):
        printAllFunctionality()
        choice = str(input("What do you choose (w/c/d/q)"))
        if choice.upper() == 'W':
            Withdraw(accountNumber)
        elif choice.upper() == 'C':
            print("Your Bank Balance is $", CheckBalance(accountNumber))
        elif choice.upper() == 'D':
            Deposit(accountNumber)
        elif choice.upper() == 'Q':
            quit()
        else:
            print("Choose from the options given (W/w/C/c/D/d/Q/q) next time")
            continue

def main():
    print("--------------Welcome to ATM of Bank XYZ---------")
    while(1):
        userAccountPresent = str(input("Do you have an account at our Bank XYZ?(Y/N)"))
        if userAccountPresent.upper() =='Y':
            WrongPinAttempts = 0
            while(1):
                print("What is your bank account number? ")
                accountNumber = str(input())
                if AccountNumberValidity(accountNumber) == True:
                    UserGivenPin = int(input("What is the 4 digit pin?"))
                    if PinValidity(accountNumber, UserGivenPin) == True:
                        DoAccountFunctions(accountNumber)
                    else:
                        WrongPinAttempts +=1
                        print("Invalid Pin! Try Again(Try ", WrongPinAttempts, " out of 3)")
                    if WrongPinAttempts >=3:
                        print("You have exceeded the pin try limit, retry in 60 seconds")
                        time.sleep(60)
                else:
                    print("Please enter valid account Number!!")
        elif userAccountPresent.upper() == 'N':
            print("Please open account at our Bank")
            print(" Contact us at +01 00000-00000")

if __name__ == "__main__":
    main()