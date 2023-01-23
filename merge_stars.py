import os, time
from ghapi.all import GhApi
api = GhApi()

for page in range(0,1):
    user = api.users.get_authenticated()
    print(user)
    print(res.keys())
