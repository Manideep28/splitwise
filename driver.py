import sys
sys.path.append('C:\\Users\\\\sman\\Documents\\store\\vscode')

from controllers.user_controller import UserController
from controllers.group_controller import GroupController
from controllers.bill_controller import BillController

from services.bill_service import BillService
from services.group_service import GroupService
from services.user_service import UserService

userController = UserController(UserService())
groupController = GroupController(GroupService())
billController = BillController(BillService())

user1 = userController.addUser('user1','pawan')
user2 = userController.addUser('user2','gyan')
user3 = userController.addUser('user2','abhi')
user4 = userController.addUser('user2','nishant')
user5 = userController.addUser('user2','ns')

members = [user1,user2,user3,user4,user5]
group1 = groupController.addGroup('group1','avengers',members)

# print( group1.getMembers() ) 

paidBy = {'user1':200,'user2':100,'user3':50,'user4':50,'user5':100,}
contribution = {'user1':100,'user2':100,'user3':100,'user4':100,'user5':100}

bill = billController.addBill('bill1','group1',500,contribution,paidBy)

balance = billController.getUserBalance('user1')
print(balance)