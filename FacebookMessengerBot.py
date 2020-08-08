from fbchat import Client
from fbchat.models import Message
from fbchat.models import *
from fbchat import models

username = "nicholasmonteirovital@hotmail.com"
password = "nmv256"

client = Client(username, password)
client.logout()

client.send(Message(text="Message"),
            thread_id="friend_user_id",
            thread_type=models.ThreadType.USER)

client.send(Message(text="Message"),
            thread_id="group_id",
            thread_type=models.ThreadType.GROUP)

users = client.searchForUsers("name of users")
for user in users:
    print(user)

users = client.searchForUsers("name of users")
user = users[0]

print(f"user id: {user.uid}")
print(f"user name: {user.name}")
print(f"user profile pic: {user.photo}")
print(f"user url: {user.url}")