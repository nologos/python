#================================
#
#copy this to main scrip and execute to generate download lists for azure processing
#
#
#================================

randd = random.randint(1000, 9999)
twitch_clip_page_link = "https://www.twitch.tv/directory/game/Hearthstone/clips?range=30d"
whos_the_streamer = "HearthstonePP"
func_link = str(twitch_clip_page_link)
func_steamer = whos_the_streamer
try:
    os.mkdir("allcliprepo")
except:
    print("dir already exist all ok")

out1 = scrape_get_links_from_twitch_inspect_html(func_link)
out2 = scrape_transform_to_download_links(out1)
out3 = ""
for item in out2:
    out3 = out3 + item + "\n"
filename = ("movetocloud" + func_steamer + str(randd))
open(filename, "w").write(out3)
# hold_my_concat_list = ""
# for link in out2:
#     file_location = download_clip_files_return_location(link)
#     print("downloading " + link)
#     hold_my_concat_list = hold_my_concat_list + (str(file_location[0]) + "\n")
# videos_to_concat = hold_my_concat_list.splitlines()
#
# finalresult = transform_multiple_video_files(videos_to_concat, func_steamer)
# print(finalresult)
#
# upload_final_product_to_youtube(finalresult, func_steamer)