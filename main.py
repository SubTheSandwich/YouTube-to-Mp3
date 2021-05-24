#hi!
import os
import subprocess
from pydub import AudioSegment

url = input("Please enter your url: ")
ask = str(input("File name?"))

def main():
    try:
        if os.path.exists('file.m4a'):
            os.remove('file.m4a')

        subprocess.call(['youtube-dl', '-f', '140', url, '-o', 'file.m4a'])
        sound = AudioSegment.from_file('file.m4a')
        
        
        
        sound.export("./files/" + ask + '.mp3', format="mp3", bitrate="128k")

        print("Your video has been successfully downloaded and converted to an mp3.")

        if os.path.exists('file.m4a'):
            os.remove('file.m4a')
    except:
        print("An unknown error occured while performing this process.")


    
    





if __name__ == "__main__":
    main()
    
