import os
import shutil
import webbrowser
import pywhatkit as kit
ch=int(input("Enter your choice:"))
if ch==1:
    current_working_directory = os.getcwd()
    print(current_working_directory)
elif ch==2:
    path='C:/Users/91874/Desktop/Regex'
    os.mkdir(path)
elif ch==3:
    source_file='c:/Users/91874/Desktop/Python Programs/task.py'
    destination_file='c:/Users/91874/Desktop/Regex/task.py'
    shutil.copy(source_file, destination_file)
elif ch==4:
    url = "https://www.google.com.tr/search?q={regex software}"
    webbrowser.open(url)
elif ch==5:
    phoneNumber = "+917852069974"
    message = "This is Python Assignment given by tushar sir"
    kit.sendwhatmsg(phoneNumber, message,18,2)

