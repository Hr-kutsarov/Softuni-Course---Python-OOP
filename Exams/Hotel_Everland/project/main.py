from appliances.fridge import Fridge
from appliances.laptop import Laptop
from appliances.stove import Stove
from appliances.tv import TV
from people.child import Child
from rooms.room import Room

fridge = Fridge()
print(fridge.get_monthly_expense())
laptop = Laptop()
print(laptop.get_monthly_expense())
stove = Stove()
print(stove.get_monthly_expense())
tv = TV()
print(tv.get_monthly_expense())
print('= end of appliances =')
# child1 = Child(5)
child1 = Child(5, 3, 4, 11, 12)
print(child1.cost)

print('--room')
room = Room('Flintstones', 100, 3)
room.expenses = -1