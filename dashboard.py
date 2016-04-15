#!/usr/bin/env python
print "Content-Type:text/html"
print

import cgi
import cgitb
form = cgi.FieldStorage()
username= form.getvalue('username')
print """
<!DOCTYPE html>
<html>
<head>
<title> Dashboard </title>
	<link rel="stylesheet" href="main.css">
	<link rel="icon" href="ico.png">

</head>
<body background="bat.png">
<div id="nav">
<u1>
<li><a href = "http://cgi.cs.mcgill.ca/~yxu233/makefriends.py?username=%s"
	>Make an Ally</a></li>
<li><a href = "http://cgi.cs.mcgill.ca/~yxu233/seefriends.cgi?username=%s"
	>See your Alliance</a></li>
<li><a href = "http://cgi.cs.mcgill.ca/~myu27/"
	>Logout</a></li>
</u1>
</div>
<form name="status" action="status.py" method="post" >
Status:<br>
<input type="type" name="textcontent" autocomplete="off" required title="Ya gotta write something first!!"><br>
<input type="hidden" name="username" value="%s">
<input type="submit" value="Submit" />
<p><span style="font-size: 24px;"><font face = "clean"> This just in: </font></span></p>
</form>

</body>
</html>
""" %(username, username, username)



def addNewToFriendsFile():
	existingUser = 0
	friendFile = open('/home/2016/yxu233/public_html/friends.txt', 'a+')
	for line in friendFile:
		
		checkLine = line.strip("\n")
		firstToken = checkLine.split(' ')[0]

		if (firstToken == username):
			existingUser=1

	if (existingUser==0):
		friendFile.write(username + "\n")
	friendFile.close()

addNewToFriendsFile()



def printTheStatuses():
	count = 0
	# Gotta read friends.txt
	friendList = open("/home/2016/yxu233/public_html/friends.txt", "r")
	for line in friendList:
		checkLine = line.strip("\n")
		friendNames = checkLine.split(' ')
		# When we find the line that has the friends list...
		if (friendNames[0] == username):
			# ...open up status.txt...
			statuses = open("status.txt", "r")
			list = statuses.readlines()
			statuses.close()
			list.reverse()
			for value in list:
				# ... look at the names...
				friendToken = value.split(' ', 1)[0]
				message = value.split(' ', 1)[1]
				
				for i in range(len(friendNames)):
				
					# ... and if it finds a match, print that line
					if (friendToken == friendNames[i]):
						print"""
						<html>
						<p>%s : %s</p>
						</html>"""%(friendToken, message)
						count=count +1
				if (count == 20):
					break
 
printTheStatuses()