import datetime

class ATM:
    def __init__(self):
        # Initialize the ATM with a sample account
        self.account = {
            'balance': 10000,
            'pin': '1234',
            'transactions': []
        }

    def check_balance(self):
        # Return the current account balance
        return self.account['balance']

    def withdraw(self, amount):
        # Withdraw cash if sufficient balance is available
        if amount <= self.account['balance']:
            self.account['balance'] -= amount
            self.record_transaction('Withdrawal', amount)
            return f"Withdrawn ${amount}. New balance: ${self.account['balance']}"
        else:
            return "Insufficient funds"

    def deposit(self, amount):
        # Deposit cash into the account
        self.account['balance'] += amount
        self.record_transaction('Deposit', amount)
        return f"Deposited ${amount}. New balance: ${self.account['balance']}"

    def change_pin(self, new_pin):
        # Change the PIN for the account
        self.account['pin'] = new_pin
        return "PIN changed successfully"

    def get_transaction_history(self):
        # Return the list of transactions
        return self.account['transactions']

    def record_transaction(self, transaction_type, amount):
        # Record a new transaction
        transaction = {
            'type': transaction_type,
            'amount': amount,
            'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.account['transactions'].append(transaction)

def main():
    atm = ATM()
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            print(f"Your balance is ₹{atm.check_balance()}")
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            print(atm.withdraw(amount))
        elif choice == '3':
            amount = float(input("Enter amount to deposit: "))
            print(atm.deposit(amount))
        elif choice == '4':
            new_pin = input("Enter new PIN: ")
            print(atm.change_pin(new_pin))
        elif choice == '5':
            history = atm.get_transaction_history()
            for transaction in history:
                print(f"{transaction['date']} - {transaction['type']}: ${transaction['amount']}")
        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
