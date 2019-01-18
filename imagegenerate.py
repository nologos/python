import os
import random
def make_thumbnail(creatorUsername, titletext="demonamew2", weeknumber="14"):
    thumbnailpathexist=os.path.exists("main-downloader-static/thumbnails/" + creatorUsername)
    if thumbnailpathexist != True:
        return("")
    #variables mag for magickimage
    colors=["red", "blue", "magenta", "orchid", "teal", "yellow", "tomato", "forestgreen", "azure", "aqua", "blueviolet", "crimson", "fuchsia"]
    mag_bgcolor =random.choice(colors)
    mag_font = "Candice"
    mag_main_text=titletext
    mag_weeknumber=weeknumber
    mag_outputname1="main-downloader-temp/thumbnails/" + "thumbnail" + str(random.randint(10000, 99999))+".jpg"
    thumbdir=("main-downloader-static/thumbnails/" + creatorUsername)
    thumbdirlist=os.listdir(thumbdir)
    mag_faceimage=(thumbdir + "/" + random.choice(thumbdirlist))

    command0=("convert" +
        " -size 1280x720 " +
        " xc:" + mag_bgcolor +
        " -draw \"line 1,1 1,1\"" +
        " tempsave1.jpg"
        )

    command1 =(
        "convert" +
        " -font " + mag_font +
        " -fill white " +
        #attempt at merging image same command
        " -composite " + "tempsave1.jpg" +  # generated bg
        " " + mag_faceimage +        # face clip
        " -geometry 1280x720+150+75" +  # offset of face clip
        " -depth 8" +
        " -write tempsave2.jpg" +
        #first draw name
        " -pointsize 72 " +
        " -stroke black " +
        " -strokewidth 15 " +
        " -draw " + "'text 25,129 \"" + mag_main_text + "\"'" +
        " -stroke none " +
        " -draw " + "'text 25,129 \"" + mag_main_text + "\"'" +
        #second draw week number
        " -pointsize 310" +
        " -stroke black " +
        " -strokewidth 15 " +
        " -draw " + "'text 800,320 \"" + mag_weeknumber + "\"'" +
        " -stroke none " +
        " -draw " + "'text 800,320 \"" + mag_weeknumber + "\"'" +
        " " + mag_outputname1
        )
    mag_return1=(os.getcwd()+"/"+mag_outputname1)


    os.system(command0)
    os.system(command1)
    return(mag_return1)




#

name2=make_thumbnail("Sweet anita tpo clips11111","52")
print(name2)
openit=("feh "+ name2)
os.system(openit)


