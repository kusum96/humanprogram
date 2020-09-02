import pyttsx3
import os

pyttsx3.speak("Good evening kusum , you can write any application name which you would like to open on your PC or laptop")
print("Good evening kusum , you can write any application name which you would like to open on your PC or laptop")
pyttsx3.speak("What would you like to open")
print("What would you like to open")
while True:  


	print("chat with me with your requirements:" , end='')

	p= input()

	#print(p)
	#os.system(p)

	if(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("chrome" in p) or ("google" in p)):
		pyttsx3.speak("Opening your Chrome")
		print("Here it is..")
		os.system("chrome")
		pyttsx3.speak("Requirement fulfilled!! You can continue with your next requirement")
		print("Requirement fulfilled!! You can continue with your next requirement")

	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("youtube" in p)):
		pyttsx3.speak("Opening your Youtube")
		print("Here it is..")
		os.system("chrome youtube.com")
		pyttsx3.speak("Requirement fulfilled!! You can continue with your next requirement")
		print("Requirement fulfilled!! You can continue with your next requirement")

	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("notepad" in p) or ("editor" in p)):
		pyttsx3.speak("Opening your Notepad")
		print("Here it is..")
		os.system("Notepad")
		pyttsx3.speak("Requirement fulfilled!! You can continue with your next requirement")
		print("Requirement fulfilled!! You can continue with your next requirement")

	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("windows media player" in p) or ("media player" in p)):
		pyttsx3.speak("Opening your Windows media player")
		os.system("Windows media player")
		print("Here it is..")
		pyttsx3.speak("Requirement fulfilled!! You can continue with your next requirement")
		print("Requirement fulfilled!! You can continue with your next requirement")

	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("sublime textedit" in p) or ("sublime" in p)):
		pyttsx3.speak("Opening your sublime texteditor")
		os.system("sublime texteditor")
		print("Here it is..")
		pyttsx3.speak("Requirement fulfilled!! You can continue with your next requirement")
		print("Requirement fulfilled!! You can continue with your next requirement")

	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("calculator" in p) or ("calci" in p) or ("calc" in p)):
		pyttsx3.speak("Opening your Calculator")
		os.system("calc")
		print("Here it is..")
		pyttsx3.speak("Requirement fulfilled!! You can continue with your next requirement")
		print("Requirement fulfilled!! You can continue with your next requirement")

	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("vlc" in p) or ("vlc media player" in p) or ("vlc player" in p)):
		pyttsx3.speak("Opening your VLC Media player")
		os.system("vlc")
		print("Here it is..")
		pyttsx3.speak("Requirement fulfilled!! You can continue with your next requirement")
		print("Requirement fulfilled!! You can continue with your next requirement")

	elif(("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("teamviewer" in p) or ("tviewer" in p) or ("TeamViewer" in p)):
		pyttsx3.speak("Opening your TeamViewer")
		os.system("teamviewer")
		print("Here it is..")
		pyttsx3.speak("Requirement fulfilled!! You can continue with your next requirement")
		print("Requirement fulfilled!! You can continue with your next requirement")


	elif ("exit" in p) or ("quit" in p) or ("end" in p):
		break


	else:
		pyttsx3.speak("Sorry , The program is not available in your system!!")
		print("Sorry , The program is not available in your system!!")
		pyttsx3.speak("Please try some other command.")
		print("Please try some other command.")

