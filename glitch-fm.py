# write a cli that takes in a .txt  file with 10 sentences and converts it to a .mp3 file using polly neural voice of Matthew.

# after each sentence add a pause of 2 seconds. 

# save the mp3 file to the folder assets/Book-Summary/project_name/Book-Summary.mp3
# input the project name from the command line
# input the Author's name from the command line
# input the book title from the command line



import os
import sys
import subprocess
import re
from mutagen.mp3 import MP3
from PIL import Image
from pathlib import Path
from moviepy import editor
import shutil



class MP3ToMP4:
    def __init__(self, folder_path, audio_path, video_path_name):
        """
        :param folder_path: contains the path of the root folder.
        :param audio_path: contains the path of the audio (mp3 file).
        :param video_path_name: contains the path where the created
                                video will be saved along with the
                                name of the created video.
        """
        self.folder_path = folder_path
        self.audio_path = audio_path
        self.video_path_name = video_path_name

        # Calling the create_video() method.
        self.create_video()

    def get_length(self):
        """
        This method reads an MP3 file and calculates its length
        in seconds.

        :return: length of the MP3 file
        """
        song = MP3(self.audio_path)
        return int(song.info.length)

    def get_images(self):
        """
        This method reads the filenames of the images present
        in the folder_path of type '.png' and stores it in the
        'images' list.

        Then it opens the images, resizes them and appends them
        to another list, 'image_list'

        :return: list of opened images
        """
        path_images = Path(self.folder_path)
        images = list(path_images.glob("*.png"))
        image_list = list()
        for image_name in images:
            image = Image.open(image_name).resize((800, 800), Image.ANTIALIAS)
            image_list.append(image)
        return image_list

    def create_video(self):
        """
        This method calls the get_length() and get_images()
        methods internally. It then calculates the duration
        of each frame. After that, it saves all the opened images
        as a gif using the save() method. Finally it calls the
        combine_method()

        :return: None
        """

        # show each image for 1/10th of the length of the audio. Keep looping through the images until the audio is done.

        


        length_audio = self.get_length()
        image_list = self.get_images()

        
        duration = int(length_audio / len(image_list)) * 1000
        print(duration)
        image_list[0].save(
            self.folder_path + "temp.gif",
            save_all=True,
            append_images=image_list[1:],
            duration=duration,
        )

        # Calling the combine_audio() method.
        self.combine_audio()

    def combine_audio(self):
        """
        This method attaches the audio to the gif file created.
        It opens the gif file and mp3 file and then uses
        set_audio() method to attach the audio. Finally, it
        saves the video to the specified video_path_name

        :return: None
        """
        video = editor.VideoFileClip(self.folder_path + "temp.gif")
        audio = editor.AudioFileClip(self.audio_path)
        final_video = video.set_audio(audio)
        final_video.write_videofile(self.video_path_name, audio_codec="aac", fps=24, codec='libx264', audio=True)





#get cwd
cwd = os.getcwd()

# image folder is inside the assets/project_name/Book-Summary/Photos
image_file_folder = os.path.join(cwd, "Images")

# duplicate each image 10 times
# for each image in the folder

images= os.listdir(image_file_folder)


# Import the ImageGlitcher class
from glitch_this import ImageGlitcher

# Create an instance of the ImageGlitcher class
glitcher = ImageGlitcher()

# Set the input and output directories
input_dir = "images"
output_dir = "glitched_images"

# Get a list of all the images in the input directory
image_filenames = os.listdir(input_dir)

# Iterate over the images in the input directory
for image_filename in image_filenames:
  # Load the image
  image = Image.open(os.path.join(input_dir, image_filename))
  
  # Glitch the image with 5 effects
  glitched_image = glitcher.glitch_image(image, 2)
  
  # Save the glitched image to the output directory
  glitched_image.save(os.path.join(input_dir, image_filename+"glitched.png"))


# for each image in the image folder, create 25 copies of the image

image_list = os.listdir(image_file_folder)

for image in image_list:
    for i in range(25):
        shutil.copy(image_file_folder + "/" + image, image_file_folder + "/" + image + str(i) + ".png")

# get the path to the mp3 file
mp3_file_path = os.path.join(cwd,"mp3", "mp3.mp3")

# create the command to convert ssml to mp3



# create a movie file using the image file and the mp3 file
# save the movie file to the folder assets/project_name/Book-Summary.mp4




MP3ToMP4( image_file_folder, mp3_file_path,"video.mp4")















# create the sample cli command for the user to run
# the command should be:
# python create-book-summary.py project_name author book_title image_file text_file
# python3 create-book-summary.py The-Seven-Spiritual-Laws-of-Success "Deepak Chopra" "The Seven Spiritual Laws of Success" images/deepak-chopra.jpg text-summary/deepak-chopra.txt