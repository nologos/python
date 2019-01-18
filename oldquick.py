

import os
import random  

def convert_and_concatenate(videos_to_concat): # takes array of videos
    my_cwd = os.getcwd()
    dir2 = my_cwd + "/main-downloader-temp/concat-list/"
    dir3 = my_cwd + "/main-downloader-temp/compiled-vids/"
    dir4 = my_cwd + "/main-downloader-temp/allcliprepo/"

        
    cononccc = (dir2 + "convert_and_concat_list" + str(random.randint(1000, 9999)) + ".txt")  # ffmpeg script required file
    concat_outputfile = (dir3 + "multi_converted" + str(random.randint(1000, 9999)) + ".mp4")
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
            " -c:v libx264" + 
            " -crf 22 " + 
            " -preset slow " + 
            " -pix_fmt yuv420p " + 
            " -c:a libmp3lame " + # audiot encoder <<<<<<
            " -vbr 3 " + 
            " -ac 2 " + #Set the number of audio channels. 
            " -ar 44100 " +  #Set the audio sampling frequency.
            " " + out # output file
        )
        print(cmd1)
        os.system(cmd1)
    cmd2 = ("ffmpeg -f concat -safe 0 -i " + cononccc + " -c copy " + concat_outputfile)
    print(cmd2)
    os.system(cmd2)


    return(concat_outputfile)

if __name__ == '__main__':
    convert_and_concatenate(a)



