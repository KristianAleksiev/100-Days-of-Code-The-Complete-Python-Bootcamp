### Day 17 - Creating classes in python

### Creating a class in python

# class User: #Pascal case
#     pass
#
# user_1 = User()
# user_1.id = "001" # Adding an attribute to the object from class User
# user_1.username = "Kristian"
# print(user_1.username)

#Initializing an object -> setting starting value


# class Car:
#     def __init__(self, seats): #initialise attributes
#         self.seats = seats
#
# my_car = Car(5) # Passing in data in the parameter above => my_car.seats = 5

###
class User:
    def __init__(self, user_id, username): ## Every object created in the class needs to have user_id and username
        self.id = user_id
        self.username = username
        self.followers = 0 # => Setting a default value
        self.following = 0

    def follow(self, user): #Creating methods
        user.followers +=1
        self.following +=1

user_1 = User("001", "username1")
user_2 = User("002", "username2")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)








