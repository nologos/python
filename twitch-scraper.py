import subprocess
import wget
import requests
import os, uuid, sys
from azure.storage.blob import BlockBlobService, PublicAccess
from azure.storage.blob import AppendBlobService
import random


def download_direct_file(url):
url="https://clips-media-assets2.twitch.tv/AT-cm%7C339423030-360.mp4"
urlmod=(url.split('/')[-1])
list=(os.popen("pwd").read())
listmod=(list[:-1]+ "/")
curent_file=(listmod+urlmod)
out=subprocess.check_output("pwd", shell=True)

local_filename =("/home/admin/PycharmProjects/two/" + )
r = requests.get(url)
f = open(local_filename, 'wb')
for chunk in r.iter_content(chunk_size=512 * 1024):
    if chunk:  # filter out keep-alive new chunks
        f.write(chunk)
f.close()
    return




def upload_to_blob_from_pc(just_add_sample):
        AccountName="downloaderstoragetables"
        AccountKey="u2QfPKgaSBPZmRBSkbfJw71vw8ar4pJPB8aoFgS+san0q/7vcPGttPRvGtt1wgustB6Ui2pe0Ffs+32l1eDDYQ=="
        auth_blob=BlockBlobService(account_name=AccountName,account_key=AccountKey)

        container_name = 'asmongold'
        auth_blob.create_container(container_name)

        autoname = just_add_sample.split("/")[-1]
        auth_blob.create_blob_from_path(container_name, autoname, just_add_sample)


def main():
        # local_path=os.path.expanduser("~/Documents")
        # local_file_name ="QuickStart_" + str(uuid.uuid4()) + ".txt"
        # full_path_to_file =os.path.join(local_path, local_file_name)
        #

        ##get output file ready
        rand=random.randint(100,999)
        print(rand)

        var="7C339423030"
        fulllink="https://duckduckgo.com/assets/icons/meta/DDG-iOS-icon_60x60.png"#("https://clips-media-assets2.twitch.tv/AT-cm%" + var + "-360.mp4")
        output=("/home/admin/asdasd " + str(rand) + ".png")
        #auth_blob.create_blob_from_bytes("asmongold","videoname")
        print(fulllink)
        print(output)
        wget.download(fulllink, output)
        request=requests.get(fulllink)
        #
        #
        # file = open(actual_output,  'w')
        # file.write(request)
        # file.close()








# Main method.
if __name__ == '__main__':
    # file="https://duckduckgo.com/assets/bathroom.png"
    fileURL="https://duckduckgo.com/assets/bathroom.png"
    #uploadfile="https://clips-media-assets2.twitch.tv/AT-cm%7C339423030-360.mp4"
    #file="/home/admin/youtube-project/Asmon/Blizzard hates Asmongold-337878169.mp4"
    # upload_to_blob_from_pc(file)
    download_direct_file(fileURL)







