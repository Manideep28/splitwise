
from models.user import User
from services.user_service_interface import UserServiceInterface


class UserService(UserServiceInterface):
    userDetails = {}
    def addUser(self,id,name):
        user = User()
        user.setId(id)
        user.setName(name)
        self.__class__.userDetails[id] = user
        return user