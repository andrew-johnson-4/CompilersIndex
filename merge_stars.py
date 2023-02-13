import os, time
from ghapi.all import GhApi
api = GhApi()

for _ in range(1):
    user = api.users.get_authenticated()
    print(user)
    print(res.keys())
