
# while True:
#     inpute = input("enter phone number(Must start with 9 or 8) ")
#     if inpute.startswith('8') or inpute.startswith('9'):
#         print("Phone Number accepted")
#         break
#     else:
#         print("Phone number invalid")
####################################################
#Usage of List
# planets = ["mercury","venus","earth","mars","jupiter","saturn","uranus","neptune"]
# #How to retrieve values from the list
# print(planets[4])
# #How to change value ina list
# planets[3] = "Axlland"
# print(planets)
# # How to add a new value to the list .append()
# planets.append("pluto")
# print(planets)
# #How to add a new value to the list in any position .insert()
# planets.insert(0,"Planet")
# print(planets)
# # #How to remove items from a list del()
# # del(planets[0])
# # print(planets)
# #remove() is another way to remove stuff
# planets.remove("pluto")
# print(planets)
# #How to remove the last item pop()
# planets.pop()
# print(planets)
# #len() to check length of a list
# numplanets = len(planets)
# print("There are" ,numplanets,"in the solar system")
# #How to loop through each item in the list
# for p in planets:
#     print("someday i will visit",p)
# #Second method to loop
# for i in range(len(planets)):
#     print(planets[i])
#     planets[i] = "new" + planets[i]
# print(planets)
##################################################
#Introduction to dictionaries
# shop_price = {"hamburger":7.5,"pasta":15,"pizza":25,"cheeseburger":10}

# #How to retrieve the value of an item
# print(shop_price["hamburger"])
# #How to change the value of an item
# shop_price["hamburger"]
# print(shop_price)

# #How to add a new key/ value to dictionary
# shop_price["spaggeti"] = 18
# print(shop_price)
# #How to delete a key value from dictionary
# del(shop_price["hamburger"])
# print(shop_price)
# #Loop through all the keys in dictionary
# for item in shop_price:
#     print(item)

##########################
#Scenario
#check if something exist in dictionary
# if "char kway teow" in shop_price:
#     print("yes i selll char kway teow")
# else:
#     print("sorry no char kway teow")
#Shop to sell food
# shop_price = {"hamburger":7.5,"pasta":15,"pizza":25,"cheeseburger":10}
# Choice = input("What do you want to eat? ")
# if Choice in shop_price:
#     print("We will be getting your food ready")
# else:
#     print("We do not serve that food here")
#SHOP with money usage as well
# Wallet = 8
# shop_price = {"hamburger":7.5,"pasta":15,"pizza":25,"cheeseburger":10}
# Choice = input("What do you want to eat? ")
# if Choice in shop_price:
#     print("We will be getting your food ready")
#     Wallet = Wallet - shop_price[Choice]
# else:
#     print("We do not serve that food here")
# print("You have $",Wallet,"left")