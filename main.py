import random
import tkinter as tk

passwordLength = 0
trackClicks = 0



password = []
characterList = ["!","@","#","$","%","^","&","*","(",")","_","+","~","<",">","?",",",".","/",";",":",",","[","]","{","}","|",
"0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
seperator = ","

# Reusable label for displaying the generated password (prevents stacking of the label)
passwordDisplayLabel = None

# Maximum allowed characters (changeable)
MAX_CHARS = 50



def getInputForNumOfChars():
    # Use the .get() method to retrieve the text
    global password
    global passwordDisplayLabel
    user_input = answerToCharsQuestion.get()
    if not user_input:
        return
    password.clear()

    n = int(user_input)
    if n <= 0:
        return

    for i in range(n):
        randChar = random.choice(characterList)
        password.append(randChar)

    passw0rd = "".join(password)
    if passwordDisplayLabel is None:
        passwordDisplayLabel = tk.Label(mainWindow, text=f"Here's your password: {passw0rd}")
        passwordDisplayLabel.pack()
    else:
        passwordDisplayLabel.config(text=f"Here's your password: {passw0rd}")

mainWindow = tk.Tk()

mainWindow.title("Trent's Password Generator")
mainWindow.state('zoomed')
mainWindow.minsize(800, 600)

# Validate the entry so it only allows integers in range 0..MAX_CHARS
def validate_chars(proposed: str) -> bool:
    if proposed == "":
        return True
    if not proposed.isdigit():
        return False
    try:
        val = int(proposed)
    except ValueError:
        return False
    return 0 <= val <= MAX_CHARS

vcmd = mainWindow.register(validate_chars)

howManyCharsLabel = tk.Label(mainWindow, text="How many characters do you want the password to be?")
howManyCharsLabel.pack()
answerToCharsQuestion = tk.Entry(mainWindow, width=5, validate='key', validatecommand=(vcmd, '%P'))
answerToCharsQuestion.pack()
submitButtn = tk.Button(mainWindow, text="Generate", command=getInputForNumOfChars)
submitButtn.pack()


mainWindow.mainloop()


