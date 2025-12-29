# variables exercise

# # 1. The Tip Calculator
# bill = float(input("Enter the total bill amount: "))
# tip = int(input("Enter the percentage of bill you want to give: "))
# person = int(input("Total person eating: "))

# bill += bill * (tip / 100)
# print(bill)
# per_head = bill / person

# print(F"Each person should pay ${per_head:.2f}")


# 2. The Guessing Game

# secret_number = 9
# count = 0

# while count < 3:
#     guess = int(input("Guess: "))

#     if guess == secret_number:
#         print("You won!")
#         break
#     count += 1

#     if count == 2:
#         print("Last try remaining.")
# else:
#     print("Game over.")

# 2.1 Second method using for loop
# import random

# secret_number = random.randint(1, 20)

# for x in range(3):  # 0 1 2
#     guess = int(input("Guess: "))

#     if guess == secret_number:
#         print("You won!")
#         break

#     if x == 1:
#         print("Last try remaining.")
# else:
#     print(f"Game over. The secret number was {secret_number}.")


# 3. The Simple ATM

def choice_menu():
    print("\n1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. View Transaction History")
    print("5. Exit")


balance = 1000
history = []

while True:
    try:
        choice_menu()
        choice = int(input("\nWhich action you want to perform: "))
    except:
        print("Error! Non-integer not allowed!")
    else:
        if choice == 1:
            print(f"Current balance: ${balance}")

        elif choice == 2:
            if balance <= 0:
                print("Not able to withdraw. Please deposit first.")
            else:
                withdraw_amount = int(input("Enter the amount to withdraw: $"))
                if withdraw_amount > balance:
                    print("\nError! Can't process payment. Low funds")
                else:
                    balance -= withdraw_amount
                    history.append(f"Withdrew ${withdraw_amount}")
                    print(
                        f"Transaction of ${withdraw_amount} was successful!")

        elif choice == 3:
            deposit_amount = int(
                input("Enter the amount you wish to deposit: $"))
            if deposit_amount <= 0:
                print("Please enter a valid amount( > 0).")
            else:
                balance += deposit_amount
                history.append(f"Deposited ${deposit_amount}")
                print(f"${deposit_amount} deposited successfully.")

        elif choice == 4:
            if not history:
                print("Nothing to show.")
            else:
                print("Showing history: ")
                for record in history:
                    print(record)

        elif choice == 5:
            print("Thank you for using The ATM. Please visit us soon.")
            break

        else:
            print("\nError! Enter valid option number.")

# try / except
# x = 0

# try:
#     print(x)
# except NameError:
#     print("Variable x is not definned")
# else:
#     print("Nothing is wrong")
