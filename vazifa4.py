import random
from decimal import Decimal, InvalidOperation
from datetime import datetime, timedelta
# 1-masala
# class TemperatureDescriptor:
#     def __init__(self, name):
#         self.name = name
#         self._value = None

#     def __get__(self, instance, owner):
#         return self._value

#     def __set__(self, instance, value):
#         try:
#             value = Decimal(value)
#         except InvalidOperation:
#             raise ValueError("Temperature must be a decimal number.")
        
#         if not (-50 <= value <= 50):
#             raise ValueError("Temperature must be between -50°C and 50°C.")
        
#         self._value = value

# class Temperature:
#     temperature = TemperatureDescriptor('temperature')

#     def __init__(self, temperature, timestamp):
#         self.temperature = temperature
#         self.timestamp = timestamp

#     def __str__(self):
#         return f"Harorat: {self.temperature}°C ({self.timestamp.strftime('%Y-%m-%d')})"

# def generate_random_temperature():
#     temperature = random.uniform(-10, 40)
#     timestamp = datetime.now() - timedelta(days=random.randint(0, 365))
#     return Temperature(temperature, timestamp)

# for _ in range(2):
#     temp = generate_random_temperature()
#     print(temp)

# ------------------------------------------------------------------------------------------------------

# 2-masala

# class InsufficientFundsError(Exception):
#     pass

# class TransactionDescriptor:
#     def __init__(self, name):
#         self.name = name
#         self._value = None

#     def __get__(self, instance, owner):
#         return self._value

#     def __set__(self, instance, value):
#         try:
#             value = Decimal(value)
#         except InvalidOperation:
#             raise ValueError("Transaction amount must be a decimal number.")
        
#         self._value = value

# class BankAccount:
#     transaction = TransactionDescriptor('transaction')

#     def __init__(self, initial_balance):
#         self.balance = Decimal(initial_balance)
#         self.transactions = []

#     def deposit(self, amount):
#         self.transaction = amount
#         self.balance += self.transaction
#         timestamp = datetime.now() - timedelta(days=random.randint(0, 365))
#         self.transactions.append((self.transaction, timestamp))
#         print(f"Deposited: {self.transaction} UZS on {timestamp.strftime('%Y-%m-%d')}. New balance: {self.balance} UZS")

#     def withdraw(self, amount):
#         self.transaction = amount
#         if self.balance - self.transaction < 0:
#             raise InsufficientFundsError("Xatolik: Balans yetarli emas!")
#         self.balance -= self.transaction
#         timestamp = datetime.now() - timedelta(days=random.randint(0, 365))
#         self.transactions.append((-self.transaction, timestamp))
#         print(f"Withdrew: {self.transaction} UZS on {timestamp.strftime('%Y-%m-%d')}. New balance: {self.balance} UZS")

#     def __str__(self):
#         return f"Hisobingiz: {self.balance} UZS"

# account = BankAccount(Decimal('500000'))

# try:
#     account.deposit(Decimal('200000'))
#     account.withdraw(Decimal('600000'))
#     account.withdraw(Decimal('200000'))  
# except InsufficientFundsError as e:
#     print(e)

# print(account)

# ------------------------------------------------------------------------------------------------------

# 3-masala

# class PriceDescriptor:
#     def __init__(self, name):
#         self.name = name
#         self._value = None

#     def __get__(self, instance, owner):
#         return self._value

#     def __set__(self, instance, value):
#         try:
#             value = Decimal(value)
#         except InvalidOperation:
#             raise ValueError("Price must be a decimal number.")
        
#         self._value = value

# class Ticket:
#     price = PriceDescriptor('price')

#     def __init__(self, price):
#         self.price = price
#         self.sale_date = datetime.now() - timedelta(days=random.randint(0, 365))

#     def __str__(self):
#         return f"Chipta narxi: {self.price} UZS. Sotish sanasi: {self.sale_date.strftime('%Y-%m-%d')}."

# try:
#     ticket1 = Ticket(Decimal('150000'))
#     print(ticket1)
    
#     ticket2 = Ticket('not a decimal') 
#     print(ticket2)
# except ValueError as e:
#     print(e)

# ------------------------------------------------------------------------------------------------------

# 4-masala

# class SalaryDescriptor:
#     def __init__(self, name):
#         self.name = name
#         self._value = None

#     def __get__(self, instance, owner):
#         return self._value

#     def __set__(self, instance, value):
#         try:
#             value = Decimal(value)
#         except InvalidOperation:
#             raise ValueError("Salary must be a decimal number.")
        
#         self._value = value

# class Employee:
#     salary = SalaryDescriptor('salary')

#     def __init__(self, salary):
#         self.salary = salary
#         self.payment_date = datetime.now() - timedelta(days=random.randint(0, 365))

#     def __str__(self):
#         return f"Ishchi oyligi: {self.salary} UZS. To'lov sanasi: {self.payment_date.strftime('%Y-%m-%d')}."

# try:
#     employee1 = Employee(Decimal('3200000'))
#     print(employee1)
    
#     employee2 = Employee('not a decimal')  
#     print(employee2)
# except ValueError as e:
#     print(e)


