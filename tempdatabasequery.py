import os 
import json

json_attachement_db="compilationdatabase.json"
databasefile = open(json_attachement_db,"r").read()

my_DB = json.loads(databasefile)

for creator, creatordata in my_DB.items():
    print(creator)
    print("https://www.twitch.tv/directory/game/" + creatordata["gamename"] + "/clips?range=24hr")


#https://www.twitch.tv/directory/game/poker/clips?range=24hr
#https://www.twitch.tv/directory/game/poker/clips?filter=clips&range=24hr



for creator, creatordata in my_DB.items():
    print(creator)

    direcotry = "main-downloader-static/thumbnails/"+creator

    os.mkdir(direcotry)


