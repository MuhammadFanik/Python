# Create a Class Atm
class Atm:
    # Constructor
    # Self --> It refers to the current object(in this case person1). So self.pin means "this objects pin". It's how all the variables
    # and methods stay connected to the same object
    def __init__(self):
        self.pin = None
        self.balance = None
        print("Executed automatically")
        self.menu()

    def menu(self):
        user_input = int(input("""
        Hi, how can I help you?
        1. Press 1 to create PIN
        2. Press 2 to change PIN
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit
        """))
        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.change_pin()
        elif user_input == 3:
            self.check_balance()
        elif user_input == 4:
            self.withdrawal()
        else:
            pass

    def create_pin(self):
        user_pin = int(input("Enter your PIN: "))
        self.pin = user_pin

        user_balance = int(input("Enter your balance: "))
        self.balance = user_balance

        print("PIN created successfully")
        self.menu()

    def change_pin(self):
        old_pin = int(input("Enter old PIN"))
        if old_pin == self.pin:
            new_pin = int(input("Enter new PIN"))
            self.pin = new_pin
            print("PIN changed successfully")
            self.menu()
        else:
            print("PIN does not match")
            self.menu()

    def check_balance(self):
        user_pin = int(input("Enter your PIN"))
        if user_pin == self.pin:
            print("Your balance is:", self.balance)
        else:
            print("PIN does not match")
        self.menu()

    def withdrawal(self):
        user_pin = int(input("Enter your PIN"))
        if user_pin == self.pin:
            withdraw_amount = int(input("How much amount you want to withdraw?"))
            if withdraw_amount <= self.balance:
                self.balance = self.balance - withdraw_amount
                print(f"{withdraw_amount} has been successfully withdrawn")
            else:
                print("You don't have sufficient balance")
        else:
            print("PIN does not match")
        self.menu()


# Python will automatically call the constructor (__init__). It sets PIN and balance to None and then immediately calls self.menu() to show the ATM menu
person1 = Atm()
print(type(person1))

# How this works
# 1- You call person1 = Atm() and python runs the __init__() method
# 2- Inside the constructor, it sets PIN and balance to None, and shows the self.menu(). Python pauses __init__() and jumps to menu()
# 3. You press 1 → `menu()` calls `self.create_pin()` → Python **pauses** `menu()` and jumps into `create_pin()`
# 4. You enter your PIN and balance
# 5. At the end of `create_pin()`, it calls `self.menu()` again → the menu shows up again
# 6. This keeps looping until you press anything other than 1–4