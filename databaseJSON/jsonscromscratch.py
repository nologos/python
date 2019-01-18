import json

# folder="databaseJSON/database.json"
# = open(folder, "w").read()

ext_databasewritetest="databaseJSON/databaseWriteTest.json"
json_input =open(ext_databasewritetest, "r").read()
database = json.loads(json_input)

#=========================all crazy code below============================
for creator, creatordata in database.items():
    print(creator)
    print(creatordata["username"])
    print(creatordata["capsname"])
    print(creatordata["description"])

database["asmongold"]["description"]=database["asmongold"]["description"][:-35]

for creator, creatordata in database.items():
    print(creatordata["username"] + "|||" + creatordata["capsname"] + "|||" + creatordata["description"])

database["asmongold"]["description"]=database["asmongold"]["description"]+"this trash humans is dumb as fuck"
#=========================all crazy code above============================

JSON_update = json.dumps(database, ensure_ascii=False)
open(ext_databasewritetest,"w").write(JSON_update)



"""

    {
        "anita": {
          "username": "sweet_anita",
          "description": "Tourette legendary tic sweet anita dick fuck my bisquit dick banna overwatch ",
          "capsname":"Sweet Anita",
          "thumbnailtext":"",
          "thumbnailexist":""
          }
        ,

        "boaty":{
            "username":"b0aty",
            "description":"runescape deadman feminist warrior thick glasses dyed hair gay family friendly ",
            "capsname":"Gingerscaper B0ary",
            "thumbnailtext":"",
            "thumbnailexist":""
            }
        ,

        "asmongold": {
          "username": "asmongold",
          "description": "wow dark souls big dick twitch thot redneck bald stupid epic gamer meme review offensive dank meme compilation hilarious ",
          "capsname":"Asmongold",
          "thumbnailtext":"",
          "thumbnailexist":""
        }
    }


"""
#https://www.youtube.com/watch?v=daefaLgNkw0