class ATM:
    def __init__(self, balance=1000, pin="1234"):
        self.balance = balance
        self.pin = pin
        print("WELCOME TO THE ATM")
        
    def check_balance(self):
        print("your current balance is", self.balance)
        return self.balance
        
    def deposit(self, amount):
        self.balance=self.balance+amount
        print("deposit successful")
        print("your current balance is" , self.balance)
        return self.balance

    def withdraw(self, amount):
        if amount>self.balance:
          print("insufficient balance")
          return none
        else:
            self.balance=self.balance-amount
            print("withdraw successful")
            print("your current balance is",self.balance)
            return self.balance

def main():
    atm = ATM()
    
    pin_attempts = 0
    max_pin_attempts = 3

    while pin_attempts < max_pin_attempts:
        user_pin = input("Enter your PIN: ")

        if user_pin == atm.pin:
            print("PIN accepted. You have access.")
            break
        else:
            pin_attempts =  pin_attempts + 1
            remaining_attempts = max_pin_attempts - pin_attempts
            if remaining_attempts > 0:
                print(f"Incorrect PIN. {remaining_attempts} attempts remaining.")
            else:
                print("Too many incorrect PIN attempts. Your card is blocked.")
                return  # Exit the program

    

    while True:
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            balance = atm.check_balance()
            print(f"Your balance is ${balance}")
        elif choice == 2:
            amount = float(input("Enter the amount to deposit: $"))
            result = atm.deposit(amount)
            print(result)
        elif choice == 3:
            amount = float(input("Enter the amount to withdraw: $"))
            result = atm.withdraw(amount)
            print(result)
        elif choice == 4:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
chirantanlonkar8879@gmail.com
