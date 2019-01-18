#!/usr/bin/python

import os  # required to call youtube-upload
import requests  # required for download direct links
from selenium import webdriver  # required for scrape inspect links
from bs4 import BeautifulSoup as bs  # required for scrape inspect links
import random  # reqiured for dynamic names
import re  # required for transform to download links
import json  # python integrated json database
import datetime  # select week number for title and upload timing control

# #global shit
week = datetime.date.today().strftime("%W")

day = datetime.date.today().strftime("%-j")

#dependacies are:
#   main script
#   thumbnail folders(manual creation)
#   other folder created automatically
#   creator database
#   fonts for imagemagic
#applications:
#   youtube-upload
#       youtube-upload config files
#   imagemagick
#   selemium-firefox
#   all other stuff from import list




def create_dependacies():
    try:
        os.mkdir("main-downloader-temp")
    except:
        print("dir 1 created")
    try:
        os.mkdir("main-downloader-temp/inspectlinks")
    except:
        print("dir 2 created")
    try:
        os.mkdir("main-downloader-temp/concat-list")
    except:
        print("dir 3 created")
    try:
        os.mkdir("main-downloader-temp/allcliprepo")
    except:
        print("dir 4 created")
    try:
        os.mkdir("main-downloader-temp/compiled-vids")
    except:
        print("dir 5 created")
    try:
        os.mkdir("main-downloader-temp/thumbnails")
    except:
        print("dir 6 created")
    try:
        os.mkdir("main-downloader-static")
        os.mkdir("main-downloader-static/thumbnails")
        #put all the thumbnails here /creator .capitalname
    except:
        print("dir 7 created")

    # try:
    #     os.mkdir("main-downloader-temp/allcliprepo2")
    #     os.mkdir("main-downloader-temp/compiled-vids2")
    # except:
    #     print("dir 8 created")

    
def scrape_get_links_from_twitch_inspect_html(scrapeurl):
    my_cwd = os.getcwd()
    dir1 = my_cwd + "/main-downloader-temp/inspectlinks/"

    # scrapeurl="https://www.twitch.tv/asmongold/clips?filter=clips&range=30d"
    options = webdriver.FirefoxOptions()
    options.headless = True
    browser = webdriver.Firefox(firefox_options=options)  # replace with .Firefox(), or with the browser of your choice
    url = str(scrapeurl)
    browser.get(url)  # navigate to the page
    uglyhtml = browser.page_source
    browser.close()

    soup = bs(uglyhtml, "html.parser")
    psoup = bs.prettify(soup)

    pritiname = (dir1 + "priti" + str(random.randint(10000, 99999)) + ".html")
    open(pritiname, "w").write(str(psoup.encode("utf8")))

    return (pritiname)


def scrape_transform_to_download_links(htmloftwitchinspect):
    beautifulscrape = htmloftwitchinspect
    read = open(beautifulscrape, "r").read()
    soup = bs(read, "html.parser")

    links1 = ""
    for link in soup.find_all("img"):
        links1 = str(links1) + str(link.get("src") + "\n")
    links1 = links1.splitlines()

    # scrapes links using regex:
    # . - any character that is not new line
    # * - repeat prievious option 0 or more times
    # ? - dont be greedy
    # 7C the start of constant strint
    # (.*) group1 collection inside () again select anything 0 or more times
    # \-p escape - key, follow up with p for a -p end of quirey
    # skip everything till the end line with .* as prieviously
    full_links = ""
    for link2 in links1:
        m = re.match(r".*?7C(.*)\-p.*", link2)
        if m != None:
            full_links = full_links + ("https://clips-media-assets2.twitch.tv/AT-cm%7C" + m.group(1) + "-360" + ".mp4\n")
    full_links = full_links.splitlines()

    return full_links
    # returns array of downloadable links


def download_clip_files_return_location(path_to_direct_video_download):
    # download file to the locala system
    # also to return download location and file_title for the next command

    url = path_to_direct_video_download
    print(url)
    file_title = (url.split('/')[-1])
    # list = (os.popen("pwd").read())
    my_cwd = os.getcwd()
    # listmod = (list[:-1] + "/")
    local_filename = (my_cwd + "/main-downloader-temp/allcliprepo/" + file_title)
    r = requests.get(url)
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024):
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
    f.close()

    return local_filename, file_title
    # download files from specified links to curdir, and returms fullpath and title
    # mabye create option to ignore returning file title in output??
    # mabye send a variable parameter to create individual dir name


def transform_multiple_video_files_same_creator(videos_to_concat, who_im_scraping="twitchuser"):
    # MANDAORY requires all files as a list in order
    my_cwd = os.getcwd()
    dir2 = my_cwd + "/main-downloader-temp/concat-list/"
    dir3 = my_cwd + "/main-downloader-temp/compiled-vids/"

    concat_outputfile = dir3 + who_im_scraping + str(random.randint(1000, 9999)) + ".mp4"
    cononccc = (dir2 + "concat_list" + str(random.randint(10000, 99999)) + ".txt")  # ffmpeg script required file

    line_for_line = ""
    for video in videos_to_concat:
        line_for_line = line_for_line + ("file " + video + "\n")
    open(cononccc, "w").write(line_for_line)

    cmd = ("ffmpeg -f concat -safe 0 -i " + cononccc + " -c copy " + concat_outputfile)
    os.system(cmd) 

    return concat_outputfile


def multicreator_transform_multiple_video_files_same_creator(videos_to_concat,who_im_scraping=""): # takes array of videos
    my_cwd = os.getcwd()
    dir2 = my_cwd + "/main-downloader-temp/concat-list/"
    dir3 = my_cwd + "/main-downloader-temp/compiled-vids/"
    dir4 = my_cwd + "/main-downloader-temp/allcliprepo/"

        
    cononccc = (dir2 + "convert_and_concat_list" + str(random.randint(1000, 9999)) + ".txt")  # ffmpeg script required file
    concat_outputfile = (dir3 + "multi_converted" + who_im_scraping + str(random.randint(1000, 9999)) + ".mp4")
    tempvidfileconstant = (dir4 + "temp"+ str(random.randint(1000, 9999)) +".mp4")

    line_for_line = ""
    for video in videos_to_concat:
        line_for_line = line_for_line + ("file " + video + "\n")
    open(cononccc, "w").write(line_for_line) # this is the main output file to pass to next function


    for video in videos_to_concat: # this standartizes sected videos to uniform defined parameters
        print("formating "+video)
        out = video # output end result path has to be same as input
        os.rename(video,tempvidfileconstant)
        tempvideo = tempvidfileconstant #buffer file renames in the same dir
        height="360"
        width="640"
        cmd1=(
            "ffmpeg -y " + #Overwrite output files without asking.
            " -i " + tempvideo + # input 
            " -filter:v "+ #Create the filtergraph specified by filtergraph and use it to filter the stream
             " \" " +
             " scale=iw*min("+width+"/iw\,"+height+"/ih):ih*min("+width+"/iw\,"+height+"/ih)," + 
             " pad="+width+":"+height+":("+width+"-iw*min("+width+"/iw\,"+height+"/ih))/2:("+height+"-ih*min("+width+"/iw\,"+height+"/ih))/2" +
             " \" " +
            #" -c:v libx264" + # video encoder legacy
            " -c:v h264 " + # < use this normaly
            #" -c:v copy" + #test codec
            " -crf 22 " + 
            " -preset slow " + 
            " -pix_fmt yuv420p " + 
            " -c:a libmp3lame " + # audiot encoder <<<<<<  # use this normaly out for testing purposes
            " -vbr 3 " + 
            " -ac 2 " + #Set the number of audio channels. 
            " -ar 44100 " +  #Set the audio sampling frequency.
            " " + out # output file
        )
        print(cmd1)
        os.system(cmd1)
    cmd2 = ("ffmpeg -f concat -safe 0 -i " + cononccc + " -c copy " + concat_outputfile)
    os.system(cmd2)

    return concat_outputfile


def upload_final_product_to_youtube(path_to_local_video, video_title="notitle", description="",playlist="",thumnail_location=""):
    cmd = ("youtube-upload " + path_to_local_video +
           " --title=" + video_title +
           " --description=" + description +
           " --category=Entertainment" +
           " --playlist="+ playlist +
           " --thumbnail=" + thumnail_location
           )
    print(cmd)
    os.system(cmd)
    # use os.system to call youtube-upload
    # asuming youtube-upload is configured


def check_for_disabled_videos():
    # this will be ran after creating a full list of videos to concatenate,
    # before initialising the download
    # will accept integers and add a coment on the list of vide that caused the claim#
    print("hello world")


def glue_everything_and_upload(twitch_clip_page_link="https://something???", video_title="thitchvideo", description="",creatorusername="", titleorig=""):
    func_link = str(twitch_clip_page_link)
    func_steamer = video_title

    out1 = scrape_get_links_from_twitch_inspect_html(func_link)
    out2 = scrape_transform_to_download_links(out1)
    hold_my_concat_list = ""
    for link in out2:
        file_location = download_clip_files_return_location(link)
        print("downloading " + link)
        hold_my_concat_list = hold_my_concat_list + (str(file_location[0]) + "\n")
    videos_to_concat = hold_my_concat_list.splitlines()


    path_to_vide_location = transform_multiple_video_files_same_creator(videos_to_concat, func_steamer)

    print(path_to_vide_location)

    thumnail_location = make_thumbnail(creatorusername, titleorig, week)
    print(thumnail_location)
    upload_final_product_to_youtube(path_to_vide_location, video_title, description, creatorusername,thumnail_location)

    # if concat file more than 0 return success
    #not int(videos_to_concat)

    #actually it compares the variable and does not run a terminal command. additional escape  chars onyl required if used within os.system
    #individualy replaced string back to orig. to pass the check correctly
    if os.path.exists(path_to_vide_location.replace("\\ "," ")):
        return("completed")
    else:
        return("fail")


def multicreator_glue_everything_and_upload(twitch_clip_page_link="https://something???", video_title="thitchvideo", description="",creatorusername="", titleIMG="", creator=""):
    func_link = str(twitch_clip_page_link)

    out1 = scrape_get_links_from_twitch_inspect_html(func_link)
    out2 = scrape_transform_to_download_links(out1)
    hold_my_concat_list = ""
    for link in out2:
        file_location = download_clip_files_return_location(link)
        print("downloading " + link)
        hold_my_concat_list = hold_my_concat_list + (str(file_location[0]) + "\n")
    videos_to_concat = hold_my_concat_list.splitlines()


    path_to_vide_location = multicreator_transform_multiple_video_files_same_creator(videos_to_concat, creatorusername)

    print(path_to_vide_location)

    thumnail_location = make_thumbnail(creator, titleIMG, day, "75")
    print(thumnail_location)
    upload_final_product_to_youtube(path_to_vide_location, video_title, description, creator ,thumnail_location)

    # if concat file more than 0 return success
    #not int(videos_to_concat)

    #actually it compares the variable and does not run a terminal command. additional escape  chars onyl required if used within os.system
    #individualy replaced string back to orig. to pass the check correctly
    if os.path.exists(path_to_vide_location.replace("\\ "," ")):
        return("completed")
    else:
        return("fail")


def make_thumbnail(creatorUsername, titletext="notitle", weeknumber="" , fontsize1="95"):
    thumbnailpathexist=os.path.exists("main-downloader-static/thumbnails/" + creatorUsername)
    if thumbnailpathexist != True:
        return("")
    #variables mag for magickimage
    colors=["red", "blue", "magenta", "orchid", "teal", "yellow", "tomato", "forestgreen", "azure", "aqua", "blueviolet", "crimson", "fuchsia"]
    mag_bgcolor =random.choice(colors)
    mag_font = "Candice"
    mag_main_text=titletext
    mag_weeknumber=weeknumber
    mag_outputname1="main-downloader-temp/thumbnails/" + "thumbnail" + str(random.randint(10000, 99999))+ creatorUsername + weeknumber +".jpg"
    thumbdir=("main-downloader-static/thumbnails/" + creatorUsername)
    thumbdirlist=os.listdir(thumbdir)
    mag_faceimage=(thumbdir + "/" + random.choice(thumbdirlist))

    command0=("convert" +
        " -size 1280x720 " +
        " xc:" + mag_bgcolor +
        " -draw \"line 1,1 1,1\"" +
        " main-downloader-temp/tempsave1.jpg"
        )

    command1 =(
        "convert" +
        " -font " + mag_font +
        " -fill white " +
        #attempt at merging image same command
        " -composite " + "main-downloader-temp/tempsave1.jpg" +  # generated bg
        " " + mag_faceimage +        # face clip
        " -geometry 1280x720+150+75" +  # offset of face clip
        " -depth 8" +
        " -write main-downloader-temp/tempsave1.jpg" +
        #first draw name
        " -pointsize "+fontsize1+" " + 
        " -stroke black " +
        " -strokewidth 15 " +
        " -draw " + "'text 25,129 \"" + mag_main_text + "\"'" +
        " -stroke none " +
        " -draw " + "'text 25,129 \"" + mag_main_text + "\"'" +
        #second draw week number
        " -pointsize 320" +
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



########################### CREATE A ONE OFF THUMBNAIL: FIRST CREATE A DIRECTORY IN STATIC/THUMBNAILS AND ADD IMAGE, PASS DIRECTORY NAME AS FIRST PARAM, TEXT TO BE WRITEN IN SECOND PARAM, MORE TEXT IN 3RD PARAM 

# if __name__ == '__main__':
#     json_attachement_db="compilationdatabase.json"
#     databasefile = open(json_attachement_db,"r").read()
#     my_DB = json.loads(databasefile)
#     for creator, creatordata in my_DB.items():
#         imagetext = creatordata["capsname"] + "best clips of the day"
#         imagetext.replace(" ", "\\ ")
#         print(make_thumbnail(creator, imagetext, day, "75" ))

# ####print(make_thumbnail("CSGO", "CS:GO best clips of the day", "15", "75" )) # single individual create requires directory to exist
# ####################################################


############################### this is for compilation ###################################
if __name__ == '__main__':
    create_dependacies()
    #week name move out to be global

    json_attachement_db="compilationdatabase.json"
    databasefile = open(json_attachement_db,"r").read()

    #using database file structure
    #simiral as objects
    #but instead of drilling deeper using "." you use []
    #and data is provided in key value pairs
    #asmongold, asmongoldDATA(<datahere>)
    #to access this data use asmongoldDATA[description]

    my_DB = json.loads(databasefile)

    for creator, creatordata in my_DB.items():
        print(creator,creatordata)
    

        if creatordata["last_day_update"] < day:
            generic_description = " best  of asd"
            clip=("https://www.twitch.tv/directory/game/" + creatordata["gamename"] + "/clips?range=24hr")
            #/clips?range=24hr&tl=2 tl2 means english
            titleIMG=(creatordata["capsname"] + " best clips of the day ")
            title2=(creatordata["capsname"] + " best clips of the day " + day)
            playlist=creatordata["capsname"]
            title=title2.replace(" ","\\ ")
            description=("top twitch clips daily " + creatordata["description"] + generic_description)
            description=description.replace(" ","\\ ")
            print(clip+"\n"+title+"\n"+description+"\n")

            uploadresult=multicreator_glue_everything_and_upload(clip,title,description, creatordata["gamename"], titleIMG, creator)
            if (uploadresult == "completed"):
                creatordata["last_day_update"]=day
                JSON_update = json.dumps(my_DB, ensure_ascii=False)
                open(json_attachement_db, "w").write(JSON_update)
            
            
            #uncomment bellow to start deleting old downloaded video files

            # for a in os.listdir("main-downloader-temp/allcliprepo"):
            #     os.remove("main-downloader-temp/allcliprepo/" + a)
            # for b in os.listdir("main-downloader-temp/compiled-vids"):
            #     os.remove("main-downloader-temp/compiled-vids/" + b)


# ############################### this is main ###################################
# if __name__ == '__main__':
#     create_dependacies()
#     #week name move out to be global

#     json_attachement_db="database.json"
#     databasefile = open(json_attachement_db,"r").read()
#     #using database file structure
#     #simiral as objects
#     #but instead of drilling deeper using "." you use []
#     #and data is provided in key value pairs
#     #asmongold, asmongoldDATA(<datahere>)
#     #to access this data use asmongoldDATA[description]

#     my_DB = json.loads(databasefile)

#     for creator, creatordata in my_DB.items():
#         if creatordata["last_update_week"] < week:
#             generic_description = " best  harve"
#             clip=("https://www.twitch.tv/" + creatordata["username"] + "/clips?filter=clips&range=7d")
#             titleIMG=(creatordata["capsname"] + " best moments ")
#             title2=(creatordata["capsname"] + " best moments " + week)
#             title=title2.replace(" ","\\ ")
#             description=("top twitch clips daily " + creatordata["description"] + generic_description)
#             description=description.replace(" ","\\ ")
#             print(clip+"\n"+title+"\n"+description+"\n")

#             uploadresult=glue_everything_and_upload(clip,title,description, creatordata["username"], titleIMG)
#             if (uploadresult == "completed"):
#                 creatordata["last_update_week"]=week
#                 JSON_update = json.dumps(my_DB, ensure_ascii=False)
#                 open(json_attachement_db, "w").write(JSON_update)
            
            
#             #uncomment bellow to start deleting old downloaded video files

#             # for a in os.listdir("main-downloader-temp/allcliprepo"):
#             #     os.remove("main-downloader-temp/allcliprepo/" + a)
#             # for b in os.listdir("main-downloader-temp/compiled-vids"):
#             #     os.remove("main-downloader-temp/compiled-vids/" + b)


#     # JSON_update = json.dumps(my_DB, ensure_ascii=False)
#     # open(json_attachement_db,"w").write(JSON_update)

# ###################### below this lane is trash and templates ########################
#
# """
#     "empty": {
#       "username": "namegoeshere",
#       "description": "description goes here",
#       "capsname":"<++>",
#       "thumbnailtext":"",
#       "thumbnailexist":"n"
#     }
# """
#       ADDING VALUES TO THE DATABASE
#     for key, value in my_DB.items():
#         print(key,value)
#         value["last_update_week"]="-1"
#         value.get("last_update_week", "none")
#
#
# for key,value in my_DB.items():
#     print(key,value.get("thumbnailexist", "empty"))
#
#
# my_DB["montanablack88"]["thumbnailexist"]=1
#
# for key, value in my_DB.items():
#     if value["thumbnailexist"] == "":
#         print(key)
# missing lines 23-24 40-41


#memes compilation v4 best memes compilation v21 lil tay  obunga gamecube memes best vines vines funny vines alia memes car salesman memes pewdiepie best memes compilation v24 dancing alien meme metal alien memes phil swift flex tape memes ninja  dame tu cosita memes despacito 2 tekashi 6ix9ine tekashi 6ix9ine memes momo zoom challenge zoom memes despacito memes minecraft memes super smash bros meme 6ix9ine ligma ligma ninja meme ligma memes  i came i saw meme ligma balls  in my feelings dance challenge keke challenge drake keke memes astroworld memes fefe roblox funny moments roblox memes smash memes supreme patty ksi deji memesjohny johny memes johny johny eating sugar blah blah blah memes Best Memes Compilation v26 Johny johny yes papa memes johny johnny yes papa best memes compilation v32 Thanos car johny johny memeselon musk lil pump kanye west roblox lil pump i love it memes thanos car memesspiderman memes eu memesbongo cat bongo cat memes tiktok cringe  moth memes  monky im monky  tiktok memes moth sans undertale memes spooky memes halloween memes tiktok cringe  tiktok memes best memes compilation v37 undertalebest memes compilation v38 steve



