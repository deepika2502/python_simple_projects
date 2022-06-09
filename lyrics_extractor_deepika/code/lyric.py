#ProjectGurukul's Guide for lyrics extractor
from tkinter import * 
from tkinter import messagebox
from tkinter import scrolledtext
from googleapiclient.discovery import build
import requests
from bs4 import BeautifulSoup

#define key and search engine
api_key =  "AIzaSyCcd4CBY6o_9_dWGBGTZRcZcbVObAMmLX4" 
cse_key = "d65c907b6f85832c4"

#Create the extractor function
def lyrics_extractor():
    #Read the name of the song    
    song = song_entry.get()    
    #Raise a warning if no input if given
    if len(song) <=0:
        messagebox.showerror(message = "Enter a song name" )
        return
    else:    
        #connect the API with the search engine
        lyric_object = build("customsearch", 'v1', developerKey=api_key).cse()
        #execute the search
        result = lyric_object.list(q=song, cx=cse_key).execute()
        #Obtain the first result of the 10 retrieved
        try:  
            first_value = next(iter(result["items"]))
        except:
            messagebox.showwarning(message = "Lyrics for "+song+" were not found" )
            return
        #Send a request link to extract contents of the first website
        result = requests.get(first_value["link"])
        #To obtain individual components in the html format
        soup_lyrics = BeautifulSoup(result.content, "html.parser")
        #Find the language using the link
              
        if ("tamil" in first_value["link"]) | ("hindi" in first_value["link"]):
            #if tamil, read the lyric from the div tag containing print-lyrics class
            lyrics = soup_lyrics.find(class_ = "print-lyrics")
        elif "azlyrics" in first_value["link"]:
            #if english, read the lyric from the div tag containing no class and id
            lyrics = soup_lyrics.find("div", {'class':'', 'id':''})
        
        #Display the output
        display_lyrics = scrolledtext.ScrolledText(lyrics_app, width = 60, height=10, font=("Ubuntu Mono",10), bd=0, bg="seagreen3")
        display_lyrics.insert("1.0",lyrics.text)
        display_lyrics.config(state=DISABLED)
        display_lyrics.grid(row=2, column=0, columnspan=3)
    
#Create the user interface for the application
lyrics_app = Tk()
lyrics_app.geometry("500x300")
lyrics_app.title("ProjectGurukul's Lyrics extractor")
lyrics_app.config(bg="seagreen1")

#Specify the entry fields
song_label = Label(lyrics_app, text="Enter song name: ",bg="seagreen1")
song_label.grid(row=0, column=0, padx=20, pady=20)
song_entry = Entry(lyrics_app, width=40)
song_entry.grid(row=0, column=1)
#Button for lyrics
get_lyrics_button = Button(lyrics_app, text="Get Lyrics", command=lyrics_extractor)
get_lyrics_button.grid(row=1, columnspan=2,pady=20)
#Terminate the app upon closing
lyrics_app.mainloop()