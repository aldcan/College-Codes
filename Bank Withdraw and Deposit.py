def deposit(account, amount):
    account_number, balance = account
    balance += amount
    return balance

def withdraw(account, amount):
    account_number, balance = account
    balance -= amount
    return balance

account = (123456, 1000.0)
updated_account = deposit(account, 200.0)
print(updated_account)
updated_account = withdraw(account, 150.0)
print(updated_account)



