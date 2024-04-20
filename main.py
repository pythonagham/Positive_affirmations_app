# Importing necessary modules
from tkinter import *
import pyttsx3

# Creating the main window
root=Tk()
root.title("Positive Affirmations")
root.geometry("550x650")
root.resizable(False,False)
root.configure(bg="#7B3183")

# Initializing the text-to-speech conversion library
engine=pyttsx3.init()

# Defining the Function that speak the entered text
def speak():
    text="Today will be a good day, I am open and ready to learn, " \
         "I can overcome any challenge I face, " \
         "I'll focus on what I can control, " \
         "My dreams are possible."

    # Setting speech rate
    engine.setProperty('rate', 130)

    # speak the given text
    engine.say(text)
    engine.runAndWait()

# Creating the top frame for logo and title
Top_frame=Frame(root,bg="#F5DCFF",width=900,height=150)
Top_frame.place(x=0,y=0)

# Adding logo to the top frame
Logo=PhotoImage(file="logo.png")
Label(Top_frame, image=Logo,bg="#F5DCFF").place(x=20,y=10)

# Adding title to the top frame
Label(Top_frame,text="Positive Affirmations",
      font="Helvetica 22 bold italic",bg="#F5DCFF",
      fg="#7B3183").place(x=170,y=50)

# Creating the text area
text_area=Text(root,font="Robote 20",
               bg="#F5DCFF",relief=GROOVE,wrap=WORD)
text_area.place(x=40,y=180, width=470,height=290)

# Create a Label widget displaying text inside the text_area
Label(text_area,text=f"Today will be a good day.\n\n"
                     f"I am open and ready to learn."
                     f"\n\nI can overcome any challenge I face."
                     f"\n\nI'll focus on what I can control."
                     f"\n\nMy dreams are possible.",
      font="arial 15 bold",bg="#F5DCFF",
      fg="#7B3183").place(x=45,y=27)

# Load the image "speak.png"
icon1=PhotoImage(file="speak.png")

# create a Button with the image and text
speak=Button(root,text=" Play",activebackground="#D7C1E1",
           compound=LEFT,image=icon1,width=130,
           font="arial 15 bold",bg="#F5DCFF",fg="#7B3183",command=speak)
speak.place(x=200,y=500)

# Create a Label widget displaying text
insta_page = Label(root, text="@ pythonagham",
                       font=("Helvetica", 10, "bold italic"),
                       fg='#F5DCFF',bg='#7B3183')
insta_page.place(x=215, y=600)

root.mainloop()
