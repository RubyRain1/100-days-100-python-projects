class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following +=1

#__init__(self): (self is the object being initialized)
#initialise attributes

user_1 = User("001", "username")

print(user_1.id)
print(user_1.username)
# user_1.username = "username" #this is assigning an attribute

user_2 = User("002", "user2")

print(user_2.id)
print(user_2.username)
