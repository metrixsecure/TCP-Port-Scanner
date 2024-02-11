import time
print(".................................Welcome To The ATM simulation........................... \n")
Account_Name = str(input("Please enter your Account Name: "))
Account_User_PIN = int(input("Please  enter your PIN: "))
User_PIN = 1234
User_Balance = 0
User_Balance = round(User_Balance,2)

if Account_User_PIN != User_PIN:
    print("Incorrect PIN. Please enter your PIN again...")
    atm_on = False
else:
    atm_on = True

while atm_on:
    print(F"Welcome To {Account_Name} Account Main Menu: \n")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = (input("Please enter your choice: "))
    if choice == '1':
        print("Please wait while your balance is processing.... \n")
        time.sleep(3)
        print(f"{Account_Name} your Account Balance is: ${User_Balance}\n")
    elif choice == '2':
        Deposit = float(input("Please enter the amount: $"))
        User_Balance += Deposit
        time.sleep(3)
        print(f" Deposit Successfully, Your current balance is ${User_Balance}")
    elif choice == '3':
        withdraw = float(input("Please enter the amount you want to withdraw: $"))
        if withdraw > User_Balance:
            print(f"{Account_Name} you don't have enough money in your account balance to withdraw.....")
        else:
            User_Balance -= withdraw
            time.sleep(3)
            print(f"Your withdraw was successfully....")
    elif choice == '4':
        print(f"Thanks {Account_Name} for banking with us. Have a nice day. \n")
        atm_on = False
    elif choice > '4' or choice != '4':
        print("invalid choice. Please try selecting a different choice again..\n")
else:
        print("Access Denied. Please try again later... \n")