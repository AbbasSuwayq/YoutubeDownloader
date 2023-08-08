# needed modules
from pytube import YouTube
from customtkinter import *
from tkinter import *
import CTkMessagebox as CTkM
import os

window = CTk()
window.title('Youtube Downloader')
window.iconbitmap(r'YoutubeIcon.ico')  # the icon tn top left corner
window.geometry(f'{500}x{315}+{518}+{274}')
window.resizable(False, False)


def AudioPlayer():
    os.startfile(Audio)  # playing the audio


def VideoPlayerWindow():
    os.startfile(Video)  # playing the video


# Downloading function
def download():
    try:
        global Video  # I used global to use Video outside this function
        global Audio  # and the same thing with the Audio

        YT = YouTube(str(link.get()))  # getting the link from the entry
        choice = SelectedOption.get()  # getting the choice in option menu widget
        Checkbox_selection = str(Checkbox_var.get())  # getting the checkbox
        print('checking the prosses of the program')

        if choice == 'Video':

            video = YT.streams.get_highest_resolution()  # this function will get the video ID with the highest resolution
            Video = video.download(filename=f'{video.title}.mp4')  # video.title will get the title of the video

            # ( Installed messagebox ) that will show up when the video is downloaded
            Installed_messagebox = CTkM.CTkMessagebox(message=f"{video.title} is successfully installed.", icon="check",
                                                      option_1="Thanks")
            if Checkbox_selection == 'ON':
                VideoPlayerWindow()

            else:
                pass

        elif choice == 'Only audio':
            audio = YT.streams.get_audio_only()  # this function will extract audio from the video
            Audio = audio.download(filename=f'{audio.title}.mp3')  # the title of the audio from YOUTUBE
            # ( Installed messagebox )
            Installed_messagebox = CTkM.CTkMessagebox(message=f"{audio.title} is successfully installed.", icon="check",
                                                      option_1="Thanks")
            if Checkbox_selection == 'ON':
                AudioPlayer()
            else:
                pass

    except:
        # Error message to ask the user to enter a valid value
        ErrorMessage = CTkM.CTkMessagebox(title="Error", message="Error! please enter a valid value", icon="cancel")


# This is the background of the window(tkinter)
my_image = PhotoImage(file='Background.png')
image_label = Label(window, image=my_image).place(x=0, y=0)

# Download it now! label
label = CTkLabel(window, text='Download Now!', bg_color='#F6F6F6', font=('Times New Roman', 30)).place(x=150, y=50)

# This widget to make the user choose what he wants to do download
SelectedOption = StringVar(value='Video')  # the initial value in the widget
optionmenu = CTkOptionMenu(window,
                           variable=SelectedOption,
                           dropdown_hover_color='#F8F7F2',
                           fg_color='#22577A',
                           values=['Video', 'Only audio']).place(x=100, y=100)

# Entry box to get the link from the user
link = StringVar()
link_Enter = CTkEntry(window, placeholder_text='Enter your link please',
                      font=('Arial', 15),
                      width=300,
                      textvariable=link).place(x=100, y=150)

# Download button

button = CTkButton(window, text='Download',
                   font=('Arial Bold', 15),
                   fg_color='red',
                   hover_color='red4',
                   command=download).place(x=175, y=190)

# Checkbox to play the video if the user wants to
Checkbox_var = StringVar()
Checkbox = CTkCheckBox(window, text='Play it when finished', border_width=2, hover_color='#22577A',
                       variable=Checkbox_var, onvalue='ON',
                       offvalue='OFF', border_color='black',
                       font=('Arial', 15)).place(x=270, y=101.5)
warningMessage = CTkM.CTkMessagebox(title="Warning", message="Please wait for a few seconds after pressing Download.")

window.mainloop()
