import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import wikipedia
from joke.jokes import *
from random import choice
import wikiquote, random
import re
import pywhatkit as kit
import time
import datetime

def om():
    app =QApplication(sys.argv)
    win = QWidget()
    win2 = QWidget()
     
    list = ["hello", "hi"]
    list2 = ["can you help me","help me","please help me","would you help me","would you like to help me","help"]
    list3 = ["who are you?","who are you","what is your name","your name"]
    list4 = ["tell me a joke","joke","can you tell me a joke","joke please"]
    list5 = ["quote","tell me any quote","motivate me","quotes please","quotes","say any quote"]
    list6 = ["play music","play song","search on youtube","search video"]
    list7 = ["weather","search weather","current weather"]
    list8 = ["time","current time"]
    list9 = ["today date","date"]
    def msg():
        if user.text() in  str(list): 
            chat.appendPlainText("User:"+user.text())
            chat.appendPlainText("Computer: Hi buddy")
            chat.appendPlainText("")
            
        elif user.text() in str(list8):
            chat.appendPlainText("User:" +user.text())
            chat.appendPlainText("computer : ")
            
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            chat.appendPlainText(f"Sir, the time is {strTime}")
            chat.appendPlainText("")
        
        elif user.text() in str(list9):
            chat.appendPlainText("User:" +user.text())
            chat.appendPlainText("computer : ")
            
            strdate = datetime.datetime.today().strftime("%d %m %y")
            chat.appendPlainText("Sir today's date is %s" %strdate)
            chat.appendPlainText("")
                
                           
        elif user.text() in str(list2):
            chat.appendPlainText("User:"+user.text())
            chat.appendPlainText("Computer: yea sure tell me")
            chat.appendPlainText("")
            
        elif user.text() in str(list3):
            chat.appendPlainText("User:" +user.text())
            chat.appendPlainText("computer:")
            chat.appendPlainText("hello my name is marcus and I am your AI chatbox")
             
        elif user.text() in str(list4):
            chat.appendPlainText("User:" +user.text())
            chat.appendPlainText("computer")
            chat.appendPlainText(choice([geek, icanhazdad, chucknorris, icndb])())
        
        elif user.text() in str(list5):
            chat.appendPlainText("User:" +user.text())
            chat.appendPlainText("computer:")
            turn = random.choice(wikiquote.quotes('Linus Torvalds'))
            chat.appendPlainText(str(turn))
        
        elif user.text() in str(list6):
            chat.appendPlainText("User:" +user.text())
            chat.appendPlainText("computer: what you want to listen")
                         
            
            if input.text():        
                kit.playonyt(input.text())
                input.returnPressed.connect(l1.click) 
                   
            chat.appendPlainText("")
            chat.appendPlainText("search :" +input.text())    
            chat.appendPlainText("")
            
            
            win2.setFixedHeight(70)
            win2.setStyleSheet("QWidget {background-color :rgba(50,50,50,250)}")
            win2.setFixedWidth(150)
            win2.show()
        elif user.text() in str(list7):
            chat.appendPlainText("User:" +user.text())
            chat.appendPlainText("computer")
            
            if input.text():
                kit.search("weather in "+input.text())
                input.returnPressed.connect(l1.click)
              
            win2.setFixedHeight(70)
            win2.setStyleSheet("QWidget {background-color :rgba(50,50,50,250)}")
            win2.setFixedWidth(150)
            win2.show()    
            chat.appendPlainText("")
            chat.appendPlainText("search :" +input.text())    
            chat.appendPlainText("")
            
                    
                                 
        elif user.text():
            chat.appendPlainText("User:" +user.text())
            chat.appendPlainText("computer:")
            try:
                
                result = wikipedia.summary(user.text(), sentences=2)
                chat.appendPlainText(result)
                chat.appendPlainText("")
            except:
                chat.appendPlainText("Sorry i dont know...!(maybe you can try by giving only name)")
                chat.appendPlainText("")
                 
        else:
            chat.setText("type correct")
            chat.appendPlainText("")  
            
              
    chat = QPlainTextEdit(win)
    chat.setFont(QFont("Arial",12))
    chat.setStyleSheet("QPlainTextEdit {background-color:rgba(0,0,0,150);color : white;border-radius:10px}")
    chat.move(24,5)
    chat.setFixedHeight(450)
    chat.setFixedWidth(450)
    chat.setReadOnly(True)
    
    l1 = QPushButton(win)
    l1.move(435,460)
    l1.setIcon(QIcon("arroe.png"))
    l1.setStyleSheet("QPushButton{background-color : rgba(0,0,0,100)}")
    l1.clicked.connect(msg)
    
    user = QLineEdit(win)
    user.setFont(QFont("Arial",12))
    user.setStyleSheet("QLineEdit {background-color :rgba(0,0,0,150);color: white;border-radius : 10px}")
    user.setFixedHeight(30)
    user.setFixedWidth(405)
    user.move(24,460)
    user.returnPressed.connect(l1.click)
    
    input = QLineEdit(win2)
    input.setStyleSheet("QLineEdit {background-color :rgba(0,0,0,150);color: white;border-radius : 10px}")
    input.move(5,5)
    input.setFixedHeight(50)
    input.setFixedWidth(140)
    input.returnPressed.connect(l1.click)
    
    win.setFixedHeight(500)
    win.setFixedWidth(500)
    win.setStyleSheet("QWidget {background-color :rgba(50,50,50,250)}")
    win.setWindowTitle("ChatBox")
    win.setWindowIcon(QIcon("arroe.png"))
    win.setWindowOpacity(0.90)
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    om()    