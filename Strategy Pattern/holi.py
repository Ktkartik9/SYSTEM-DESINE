from discount_strategy import DiscountStrategy

class HoliStrategy(DiscountStrategy):

    def __init__(self, value):
        self.value = value

    def calculate_discount(self):
        print(f"Final price: {self.value * 0.9}")
        print("Applying holi discount of 10%")