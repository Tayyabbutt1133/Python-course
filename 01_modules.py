# Modules, comments and pip

# This is a module --> A package in the form of code which perform some functionality that we can use instead of making it by ourself
import pyjokes
import os
import pyttsx3



# pip --> Python Installer for packages which help us to install those external functionalities/modules

# print(pyjokes.get_joke())

engine = pyttsx3.init()
engine.say("Hey I'm good")
engine.runAndWait()


