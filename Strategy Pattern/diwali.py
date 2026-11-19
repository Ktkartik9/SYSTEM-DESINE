from discount_strategy import DiscountStrategy

class DiwaliStrategy(DiscountStrategy):

    def __init__(self, value):
        self.value = value

    def calculate_discount(self):
        print(f"Final price: {self.value * 0.8}")
        print("Applying diwali discount of 20%")