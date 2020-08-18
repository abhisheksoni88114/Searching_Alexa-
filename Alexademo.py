import os
import pyttsx3

print()

pyttsx3.speak(" Namaste Welcome to searching alexa app")
 
print("SEARCHING ALEXA APPLICATION")

print()
print()

print("Select from the following menu: ")

print()

print("1. Chrome browser")
print("2. Virtual Box")
print("3. Notepad Editor")
print("4. VLC media player")
print("5. Alexademo")
print("6. My Image")
print("7. C++ slides")
print("8. Arduino Application")
print("9. exit")

print()

while True:
	choice = input("what you want to open(select from the above menus)?: ")
	print()

	if (("run" in choice) or ("open" in choice )) and (("virtualbox" in choice) or ("VitualBox" in choice)):
		os.chdir("G:\\Oracle\\VirtualBox")
		os.system("VirtualBox")

	elif (("run" in choice) or  ("open" in choice)) and (("chrome" in choice) or ("Chrome" in choice)):
		os.system("chrome")

	elif (("run" in choice) or ('open' in choice)) and (("notepad" in choice) or ("Notepad" in choice)):
		os.system("notepad")

	elif (("run" in choice) or ("open" in choice)) and ("vlc" in choice):
		os.system("vlc")

	elif (("run" in choice) or ("open" in choice )) and (("Alexademo" in choice) or ("alexademo" in choice)):
		os.chdir("F:\\")
		os.system("Alexademo.py")

	elif (("run" in choice) or ("open" in choice )) and (("Image" in choice) or ("image" in choice) or ("pic" in choice)):
		os.chdir("C:\\Users\\LENO\\OneDrive\\Pictures\\Camera Roll")
		os.system("abhishek.jpg")

	elif (("run" in choice) or ("open" in choice )) and (("c++" in choice) or ("C++" in choice)):
		os.chdir("G:\\C and C++ slides")
		os.system("c++.pdf")

	elif (("run" in choice) or ("open" in choice )) and (("arduino" in choice) or ("Arduino" in choice)):
		os.chdir("G:\\Arduino")
		os.system("arduino")

	elif "exit" in choice or "quit" in choice:
		break

	else:
		print("Please Enter Valid Choice")
		print()
		