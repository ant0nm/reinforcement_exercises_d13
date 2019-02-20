# pick three names
names = ["Mia", "Francis", "Eva"]

# propmpt user for his/her name
print("Please enter your name:")
user_name = input()
if user_name in names:
    print("Hi there, {}!".format(user_name))
else:
    print("Who goes there?")
