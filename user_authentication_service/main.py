from db import DB
from user import User

my_db = DB()

for n in range(1000):
    user = my_db.add_user(str(n), str(n))
    assert user.id == n + 1

