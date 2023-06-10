class User:
    users = []
    __total_balance = 0
    __total_loan = 0

    def __init__(self, name, email, password, amount):
        self.name = name
        self.email = email
        self.password = password
        self.balance = amount
        self.users.append(name)
        self.transaction_history = []
        User.__total_balance += amount

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
        User.__total_balance += amount

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            print("Invalid amount.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: {amount}")
            User.__total_balance -= amount

    def transfer_money(self, recipient, amount):
        if recipient.name not in self.users:
            print("No account found.")
        elif amount > self.balance or self.balance == 0:
            print("Not enough balance.")
        else:
            self.balance -= amount
            recipient.deposit(amount)
            self.transaction_history.append(f"Transferred: {amount}")
            print(f"{amount} transferred to {recipient.name}")

    def take_loan(self, admin, amount):
        if not admin.loan_permission(self):
            print("Sorry, loan denied.Bank has reached loan limit")
        elif amount > self.balance * 2:
            print("Max loan limit reached.")
        else:
            print(f"Here is your loan: {amount}")
            self.balance += amount
            self.transaction_history.append(f"Loan taken: {amount}")
            User.__total_loan += amount

    def show_transactions(self):
        print(f"All previous transactions of : {self.name}")
        for transaction in self.transaction_history:
            print(transaction)

    def check_balance(self):
        return f"Current balance of {self.name}: {self.balance}"

    @staticmethod
    def show_total_balance(admin):
        if isinstance(admin, Admin):
            return User.__total_balance
        else:
            print("Access denied.")

    @staticmethod
    def show_total_loan(admin):
        if isinstance(admin, Admin):
            return User.__total_loan
        else:
            print("Access denied.")


class Admin:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def loan_permission(self, user):
        if User.show_total_balance(self) < User.show_total_loan(self):
            return False
        else:
            return True


user1 = User("maki", "maki@example.com", "123", 2000)
user2 = User("rafi", "raf@example.com", "456", 400)

user1.deposit(500)
user1.withdraw(200)
print("\n")

user1.transfer_money(user2, 300)
print("\n")

print(user1.check_balance())
print("\n")
print(user2.check_balance())
print("\n")

admin = Admin("admin", "890")
user1.take_loan(admin, 1500)

user1.show_transactions()
print("\n")
user2.show_transactions()
print("\n")

print(f"Total Balance: {User.show_total_balance(admin)}")
print(f"Total Loan: {User.show_total_loan(admin)}")