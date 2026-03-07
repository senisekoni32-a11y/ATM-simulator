# Building a simple ATM simulator
print("Hii Welcome to Jojo Bank! ")
A = input("What is Your name? ")
Pin = int(input("Type in your pin: "))
Balance = 10000
if A == "Jojo":
    print("Ahhhh, youre namesakes with the owner")
    Balance = 100000
def options():
    print("1: View Balance")
    print("2: Withdraw Money")
    print("3: Deposit Money")
    print("4: Exit")
while True:
    options()
    Reason = input("Okay "+ A + " What brings you here today? ")
    if Reason == "1":
        print(Balance)
    elif Reason == "2":
        Amount = int(input("How much do you want to withdraw? "))
        if Amount > Balance:
            print("Insufficient Funds ")
        else:
            Confirm = int(input("Enter pin "))
            if Confirm == Pin:
                print("Withdraw confirmed ")
                Balance = Balance - Amount
            else:
                print("Pin is wrong!")
                exit()
    elif Reason == "3":
        Dep = int(input("How much do you want to deposit? "))
        Balance = Balance + Dep
        print("Deposit successful! New balance: ", Balance)
    elif Reason == "4":
        print("Good bye " + A)
        exit()
    else:
        print("Invalid input. Try again!")
        
        
