from discount_service import DiscountService
from diwali import DiwaliStrategy
from holi import HoliStrategy




diwali_strategy = DiwaliStrategy(3762)
diwali_strategy.calculate_discount()


holi_strategy = HoliStrategy(500) 
holi_strategy.calculate_discount()

discount_service = DiscountService(diwali_strategy)
discount_service.process()

discount_service.set_strategy(holi_strategy)
discount_service.process()