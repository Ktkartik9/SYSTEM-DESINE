from user import User
from user_repository import UserRepository


user_obj = User("kartik ", 22, "info@cyx.com")
user_repo = UserRepository("userDB", "root", "root")

user_obj.get_user_info()

user_repo.save_to_database(user_obj)