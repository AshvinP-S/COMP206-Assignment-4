#!/usr/bin/env python

import cgi, cgitb
print "Content-Type:text/html"
print 
form = cgi.FieldStorage()
if form.getvalue('username'):
	username= form.getvalue('username')
else:
	username= ""
if form.getvalue('textcontent'):
	status_update = form.getvalue('textcontent')
else:
	status_update = ""
	

text_file = open('status.txt', 'a')
text_file.write(username)
text_file.write(' ')
text_file.write(status_update)
text_file.write('\n')
text_file.close()

print """
<html>

<meta http-equiv="refresh" content="0; url=http://cgi.cs.mcgill.ca/~apradh32/dashboard.py?username=%s" />
</html>
"""%(username)