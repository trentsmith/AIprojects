# This script will detect faces via your webcam.
# Tested with OpenCV3

import cv2
import speech_recognition as sr
import sqlite3
import pyttsx3
import flask
'''app = flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

app.run(host='0.0.0.0', port=8080)
'''
#create_table()
print("success")
print("success")
# connect to database and create table
import sqlite3
conn = sqlite3.connect(":memory:")
conn.execute('''create table my_table (value1 integer, name text, xml text)''')

# read text from your input file containing xml
f = open("haarcascade_frontalface_default.xml")
print(type(f))
xml_string_from_file = f.read()
print(type(xml_string_from_file))
cap = cv2.VideoCapture(0)

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# insert text into database
cur = conn.cursor()
cur.execute('''insert into my_table (value1, name, xml) values (?, ?, ?)''', (23, "ball", xml_string_from_file))
conn.commit()
s = cur.execute('''Select * from my_table''')
print (s)
# read from database into variable
xml_string_from_db = cur.fetchone()[2]
#print(xml_string_from_db)
# parse with the XML parser of your choice
from xml.dom.minidom import parseString

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

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
