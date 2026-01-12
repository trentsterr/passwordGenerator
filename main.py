import random
import tkinter as tk

passwordLength = 0


password = []
characterList = ["!","@","#","$","%","^","&","*","(",")","_","+","~","<",">","?",",",".","/",";",":",",","[","]","{","}","|",
"0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
seperator = ","



def getInputForNumOfChars():
    # Use the .get() method to retrieve the text
    user_input = answerToCharsQuestion.get()

    password.clear()  # Clear previous password before generating a new one
    for i in range(int(user_input)):
        randChar = random.choice(characterList)
        password.append(randChar)
    
    passw0rd = "".join(password)
    passwordDisplayLabel = tk.Label(mainWindow,text=f"Here's your password: {passw0rd}",state='active')
    passwordDisplayLabel.pack()

mainWindow = tk.Tk()

mainWindow.title("Trent's Password Generator")
mainWindow.state('zoomed')
mainWindow.minsize(800, 600)

howManyCharsLabel = tk.Label(mainWindow, text="How many characters do you want the password to be?")
howManyCharsLabel.pack()
answerToCharsQuestion = tk.Entry(mainWindow, width=2)
answerToCharsQuestion.pack()
submitButtn = tk.Button(mainWindow, text="submit", command=getInputForNumOfChars)
submitButtn.pack()


mainWindow.mainloop()


