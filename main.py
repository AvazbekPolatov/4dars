from decimal import Decimal
import random
from datetime import datetime, timedelta

class Product:
    def __init__(self, price):
        self.price = price
        self.discount = Decimal(random.randint(1, 50))
        self.purchase_date = self.generate_random_date()
        self.validate_price()
        self.validate_discount()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Narx manfiy bo'lishi mumkin emas.")
        self._price = Decimal(value)

    def generate_random_date(self):
        start_date = datetime.now()
        end_date = start_date + timedelta(days=30)
        random_date = start_date + (end_date - start_date) * random.random()
        return random_date

    def validate_price(self):
        if self.price < 0:
            raise ValueError("Narx manfiy bo'lishi mumkin emas.")

    def validate_discount(self):
        if not (1 <= self.discount <= 50):
            raise ValueError("Chegirma noto'g'ri hisoblangan.")

    def calculate_discounted_price(self):
        discount_amount = self.price * (self.discount / Decimal(100))
        discounted_price = self.price - discount_amount
        return discounted_price

    def __str__(self):
        discounted_price = self.calculate_discounted_price()
        return f"Mahsulot narxi: {self.price} UZS, chegirma: {self.discount}%. Yangi narx: {discounted_price} UZS (Sana: {self.purchase_date.date()})."

try:
    product = Product(Decimal('45000'))
    print(product)
except ValueError as e:
    print(f"Xatolik: {e}")


# --------------------------------------------------------------------------------------------------------

# class Currencyconverter:
#     def __init__(self,rate):
#         self.rate = rate
        
#     @property
#     def rate(self):
#         return self._rate
    
#     @rate.setter
#     def rate(self,value):
#         if not isinstance(value,Decimal):
#             raise ValueError("koeffitsient Decimal formatida bolishi kerak")
#         self._rate = value

#     def convert(self,amount):
#         if not isinstance(amount,Decimal):
#             raise ValueError("Qiymat Decimal formatida bolishi kerak")
#         converted_amount = amount * self.rate
#         conversion_date=self.generate_random_date()
#         return converted_amount,conversion_date

#     def generate_random_date(self):
#         start_date=datetime.now() - timedelta(days=30)
#         end_date=datetime.now() + timedelta(days=30)
#         random_date = start_date + (end_date - start_date) * random.random()
#         return random_date
    
# usd_to_uzs_converter=Currencyconverter(Decimal('12600'))
# amount_in_usd=Decimal('10')
# converted_amount,conversion_date=usd_to_uzs_converter.convert(amount_in_usd)
# print(f"{amount_in_usd} USD = {converted_amount} UZS (Sana: {conversion_date.date()})")

