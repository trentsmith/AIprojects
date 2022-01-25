# -*- coding: utf-8  -*-
"""
Created on Sat Dec 12 12:20:23 2020

@author: Trent Smith
"""
import cv2
import speech_recognition as sr
import sqlite3
import pyttsx3
import flask
conn = sqlite3.connect(":memory:")
#basic crude functions
def create_table():
    conn.execute('''create table my_table (user text, name text, xml text)''')
# read text from your input file containing xml
def open_xml_file():
    f = open("buffer.xml")
    xml_string_from_file = f.read()
    f.close()
    return xml_string_from_file
def save_to_file(xml_string_from_file):
    f = open("buffer.xml","w")
    f.write(xml_string_from_file)
    f.close()
    print("test")
def insert_into_xml(user,name,xml_string):
    cur = conn.cursor()
    cur.execute('''insert into my_table (user, name, xml) values (?, ?, ?)''', (user, name, xml_string))
    conn.commit()
def select_from_table(user,name):
        sql_select_query = """select * from my_table where name = ? and user = ?"""
        records= conn.execute(sql_select_query,(name,user))
        for row in records:
            print("integer = " , row[0])
            print("name = ", row[1] )
            print("xml = ", row[2])
            response=row[2]
        return response
def addedtrainedcas(user,name):
    xml_string_from_file= open_xml_file()
    insert_into_xml(user, name, xml_string_from_file)
def update_xml_file(user,name):
    answer = select_from_table(user,name)
    print(answer)
    save_to_file(answer)
create_table()
################################
#add a file to the database
user = "trent"
name = "trent"
addedtrainedcas(user,name)
#update the file to find the current object
update_xml_file(user,name)
faceCascade = cv2.CascadeClassifier("buffer.xml")
#############################
def find_uglies():
    match = False
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))
#############################
cap = cv2.VideoCapture(0)

import sqlite3
conn = sqlite3.connect('Talk.db')
c = conn.cursor()

def create_table():
  c.execute('CREATE TABLE IF NOT EXISTS Talk(Keywords TEXT, Response TEXT, User TEXT)')

def listToString(s):  
    # initialize an empty string 
    str1 = " " 
    # return string   
    return (str1.join(s)) 

def insert_value_into_table(user,keywords,response):
  c.execute('INSERT INTO Talk(Keywords,Response,User)VALUES(?,?,?)',(keywords,response,user))
  str1= " "
  keywords = str1.join(keywords)
  print(keywords)
  conn.commit()

def select_from_table(user,keywords):
        sql_select_query = """select * from Talk where user = ? and keywords = ?"""
        c.execute(sql_select_query, (user,keywords))
        records = c.fetchall()
        print("Printing ID ", user)
        for row in records:
            print("keywords = " , sorted(row[0]))
            print("response = ", sorted(row[1]))
            response=row[1]
            # print("user = ", row[2])
        #c.close()
        #c.execute('Select * from Talk where user = '+user)
create_table()
#insert_value_into_table("admin","show test response","This is a test response")
#print(select_from_table("admin"))
class node:
  def __init__(self,value=None):
    self.value = value
    self.word = []
    self.wordnode =[]
    
class binary_search_tree:
  def __init__(self):
    self.root=None

  def insert(self,value):
    if self.root==None:
      self.root=node(value)
    else:
      self._insert(value,self.root)  

  def _insert(self,value,cur_node,words):
    flag = False
    keywords = []
    while len(words)!=0:
        print(words)
        for i in words:
            if i in cur_node.word:
                cur_node= self.wordnode[cur_node.word.index(i)]
                words.remove(i)
                keywords.append(i)
                if len(words)==0:
                       break
            elif flag:
                cur_node.word.append(i)
                cur_node.wordnode.append(node(value))
                words.remove(i)
                keywords.append(i)
                keywordsstr = str(keywords)
                keywordsstr = listToString(keywords)
                print("the keywordsstr is "+ keywordsstr)
                insert_value_into_table("admin",keywordsstr,value)
                if len(words)==0:
                  #insert_value_into_table()             
                  break
            if i == words[len(words)-1]:
                flag = True
                break

         
  def find(self,value):
    if self.root!=None:
        return self._find(value,self.root)
    else:
        select_from_table("admin")
        ##search for phrase
        return None

  def _find(self,words,cur_node):
    flag = False
    final = ""
    while len(words) != 0:
        for i in words:
            if i in cur_node.word:
                words.remove(i)
                cur_node= cur_node.wordnode[cur_node.word.index(i)]
                flag=False
                final = cur_node.value
        if flag:
            break
        flag=True
    return final

from xml.dom.minidom import parseString
a = binary_search_tree()
a.insert("Hello")
a._insert("How are you??!!",a.root,["Hello"])
a._find(["good","Hello"],a.root)
print(a.root.wordnode[0].value)
# List of string 
print(a.root.value)
r = sr.Recognizer()
engine = pyttsx3.init()
engine.say("Hello Trent How are you?")
engine.runAndWait()
with sr.Microphone() as source:
    audio = r.listen(source)
    engine.runAndWait()
    while True:
        text = r.recognize_google(audio)
        x=""
        engine.say("input please")
        x =r.recognize_google(audio)
        print("x is " + x)
        engine.runAndWait()
        x=x.split(" ")
        answer = a._find(x,a.root)
        engine.say("answer is "+answer)
        if answer == None or answer =="":
            engine.say("unfamiliar what to say what should I say?")
            y = r.recognize_google(audio)
            print("y is " + y)
            engine.runAndWait()
            a._insert(y,a.root,x)


'''
while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	)
	print("Found {0} faces!".format(len(faces)))
	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	# Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
# When everything done, release the capture'''
cap.release()
cv2.destroyAllWindows()

