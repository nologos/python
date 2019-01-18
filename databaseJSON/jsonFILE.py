import json  # python integrated json database
from collections import namedtuple  # python integrated json database


ext_databasefile="databaseJSON/database.json"
ext_databasewritetest="databaseJSON/databaseWriteTest.json"
file=open(ext_databasefile, "r")
databasefile=file.read()
# file.close()


my_DB = json.loads(databasefile, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))


for creator in my_DB:
    print(creator)

file2=open(ext_databasewritetest,"w")
file2.write(databasefile)
file2.close()

# open(ext_databasefile, "w").write(databasefile)

print(my_DB.anita.username)
my_DB.boaty.username=my_DB.boaty(username="two")
users.append(str(user))
my_DB.boaty.username.append(str("hi"))
print(my_DB.anita.username



def default(self, o):
   try:
       iterable = iter(o)
   except TypeError:
       pass
   else:
       return list(iterable)
   # Let the base class default method raise the TypeError
   return JSONEncoder.default(self, o)

json.encoder

JSONEncoder().encode({"foo": ["bar", "baz"]})
'{"foo": ["bar", "baz"]}'