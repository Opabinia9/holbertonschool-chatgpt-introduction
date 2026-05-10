class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Display the current balance."""
        print("Current Balance: ${:.2f}".format(self.balance))

def get_valid_amount(prompt):
    """
    Get a valid positive amount from the user.
    
    Parameters:
        prompt (str): The message to display to the user.
    
    Returns:
        float: A valid positive amount, or None if invalid input is provided.
    """
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Error: Amount cannot be negative. Please try again.")
                continue
            return amount
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None

def main():
    cb = Checkbook()
    while True:
        try:
            action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
            
            if action == 'exit':
                print("Thank you for using Checkbook. Goodbye!")
                break
            elif action == 'deposit':
                amount = get_valid_amount("Enter the amount to deposit: $")
                if amount is not None:
                    cb.deposit(amount)
            elif action == 'withdraw':
                amount = get_valid_amount("Enter the amount to withdraw: $")
                if amount is not None:
                    cb.withdraw(amount)
            elif action == 'balance':
                cb.get_balance()
            else:
                print("Invalid command. Please try again. (deposit, withdraw, balance, exit)")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

