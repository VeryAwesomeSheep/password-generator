import tkinter as tk
import random, pyperclip

# Password generation
def generate():
	generatedPassword = ""
	upperCaseList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	lowerCaseList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	digitsList = ["1","2","3","4","5","6","7","8","9"]
	specialsList = ["!","@","#","$","%","^","&","*"]

	Choices0 = [upperCaseList, lowerCaseList, digitsList, specialsList]
	Choices1 = [upperCaseList]
	Choices2 = [upperCaseList, lowerCaseList]
	Choices3 = [upperCaseList, lowerCaseList, digitsList]
	Choices4 = [upperCaseList, specialsList]
	Choices5 = [upperCaseList, digitsList]
	Choices6 = [upperCaseList, digitsList, specialsList]
	Choices7 = [upperCaseList, lowerCaseList, specialsList]
	Choices8 = [lowerCaseList]
	Choices9 = [lowerCaseList, specialsList]
	Choices10 = [lowerCaseList, digitsList]
	Choices11 = [lowerCaseList, digitsList, specialsList]

	# Case for all checkboxes on
	if (upperCaseLetters.get() == 1 and lowerCaseLetters.get() == 1 and digits.get() == 1 and specialCharacters.get() == 1):
		for i in range(passwordLen.get()):
			generatedPassword = generatedPassword + random.choice(random.choices(Choices0, weights=map(len, Choices0))[0])

	# Case for upper letters on
	if (upperCaseLetters.get() == 1 and lowerCaseLetters.get() == 0 and digits.get() == 0 and specialCharacters.get() == 0):
		for i in range(passwordLen.get()):
			generatedPassword = generatedPassword + random.choice(random.choices(Choices1, weights=map(len, Choices1))[0])

	# Case for upper and lower letters on
	if (upperCaseLetters.get() == 1 and lowerCaseLetters.get() == 1 and digits.get() == 0 and specialCharacters.get() == 0):
		for i in range(passwordLen.get()):
			generatedPassword = generatedPassword + random.choice(random.choices(Choices2, weights=map(len, Choices2))[0])

	# Case for upper and lower letters and digits on
	if (upperCaseLetters.get() == 1 and lowerCaseLetters.get() == 1 and digits.get() == 1 and specialCharacters.get() == 0):
		for i in range(passwordLen.get()):
			generatedPassword = generatedPassword + random.choice(random.choices(Choices3, weights=map(len, Choices3))[0])

	# Case for upper letters and specials on
	if (upperCaseLetters.get() == 1 and lowerCaseLetters.get() == 0 and digits.get() == 0 and specialCharacters.get() == 1):
		for i in range(passwordLen.get()):
			generatedPassword = generatedPassword + random.choice(random.choices(Choices4, weights=map(len, Choices4))[0])

	# Case for upper letters and digits on
	if (upperCaseLetters.get() == 1 and lowerCaseLetters.get() == 0 and digits.get() == 1 and specialCharacters.get() == 0):
		for i in range(passwordLen.get()):
			generatedPassword = generatedPassword + random.choice(random.choices(Choices5, weights=map(len, Choices5))[0])

	# Case for upper letters and digits and specials on
	if (upperCaseLetters.get() == 1 and lowerCaseLetters.get() == 0 and digits.get() == 1 and specialCharacters.get() == 1):
		for i in range(passwordLen.get()):
			generatedPassword = generatedPassword + random.choice(random.choices(Choices6, weights=map(len, Choices6))[0])

	# Case for upper and lower letters and specials on
	if (upperCaseLetters.get() == 1 and lowerCaseLetters.get() == 1 and digits.get() == 0 and specialCharacters.get() == 1):
		for i in range(passwordLen.get()):
			generatedPassword = generatedPassword + random.choice(random.choices(Choices7, weights=map(len, Choices7))[0])

	# Case for lower letters on
	if (upperCaseLetters.get() == 0 and lowerCaseLetters.get() == 1 and digits.get() == 0 and specialCharacters.get() == 0):
		for i in range(passwordLen.get()):
			generatedPassword = generatedPassword + random.choice(random.choices(Choices8, weights=map(len, Choices8))[0])

	# Case for lower letters and specials on
	if (upperCaseLetters.get() == 0 and lowerCaseLetters.get() == 1 and digits.get() == 0 and specialCharacters.get() == 1):
		for i in range(passwordLen.get()):
			generatedPassword = generatedPassword + random.choice(random.choices(Choices9, weights=map(len, Choices9))[0])

	# Case for lower letters and digits on
	if (upperCaseLetters.get() == 0 and lowerCaseLetters.get() == 1 and digits.get() == 1 and specialCharacters.get() == 0):
		for i in range(passwordLen.get()):
			generatedPassword = generatedPassword + random.choice(random.choices(Choices10, weights=map(len, Choices10))[0])

	# Case for lower letters and digits and specials on
	if (upperCaseLetters.get() == 0 and lowerCaseLetters.get() == 1 and digits.get() == 1 and specialCharacters.get() == 1):
		for i in range(passwordLen.get()):
			generatedPassword = generatedPassword + random.choice(random.choices(Choices11, weights=map(len, Choices11))[0])

	# Case when no letters boxes are checked
	if (upperCaseLetters.get() == 0 and lowerCaseLetters.get() == 0):
		generatedPassword = "Password must contain letters!"

	password.set(generatedPassword)

# Copying the password to clipboard
def copy():
	pyperclip.copy(password.get())

# Initialization of window
root = tk.Tk()
root.geometry("300x280")
root.resizable(width = False, height = False)
root.title("Password Generator")

root.columnconfigure(0, minsize= 300)
for i in range(10):
	root.rowconfigure(i, minsize = 10)

# Top text label
topTextLabel = tk.Label(root, text = "Password Generator" , font ="arial 15 bold").grid(row = 0, column = 0, sticky = "nsew")

# Password settings interface
tk.Label(root, text = "PASSWORD LENGTH\n5-128 characters", font = "arial 10 bold").grid(row = 2, column = 0)

# Password length
passwordLen = tk.IntVar()
tk.Spinbox(root, from_ = 5, to_ = 128 , textvariable = passwordLen , width = 5).grid(row = 3, column = 0, pady = 10)

# Check boxes for password options
upperCaseLetters = tk.IntVar(value = 1)
lowerCaseLetters = tk.IntVar(value = 1)
digits = tk.IntVar()
specialCharacters = tk.IntVar()
tk.Checkbutton(root, text = "A-Z", variable = upperCaseLetters).grid(row = 4, column = 0, sticky = "w", padx = 80)
tk.Checkbutton(root, text = "a-z", variable = lowerCaseLetters).grid(row = 5, column = 0, sticky = "w", padx = 80)
tk.Checkbutton(root, text = "0-9", variable = digits).grid(row = 4, column = 0, sticky = "e", padx = 93)
tk.Checkbutton(root, text = "!@#$%^&*", variable = specialCharacters).grid(row = 5, column = 0, sticky = "e", padx = 50)

# Password generatring/copying buttons and display field
password = tk.StringVar()
tk.Button(root, text = "Generate", command = generate).grid(row = 6, column = 0, pady = 10)
tk.Entry(root, textvariable = password, width = 30).grid(row = 7, column = 0)
tk.Button(root, text = "Copy to clipboard", command = copy).grid(row = 8, column = 0, pady = 10)

# Running tkinker
root.mainloop()
