import os

class BankAccount:
    def __init__(self, balance_file='balance.txt', initial_balance=0):
        # Use an absolute path for balance.txt inside the current script folder
        self.balance_file = os.path.join(os.path.dirname(__file__), balance_file)
        self.__account_balance = self._load_balance(initial_balance)

    def _load_balance(self, default):
        try:
            with open(self.balance_file, 'r') as f:
                balance = float(f.read())
                return balance
        except FileNotFoundError:
            return default
        except Exception as e:
            print(f"Error reading balance file: {e}")
            return default

    def _save_balance(self):
        with open(self.balance_file, 'w') as f:
            f.write(str(self.__account_balance))

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            self._save_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            self._save_balance()
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")
