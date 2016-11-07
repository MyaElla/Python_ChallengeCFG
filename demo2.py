#open the data.json file and read it
#function that returns a value, which is called a file object, which lets you read the file, individual lines

# f = open ('data.json', 'r')
# #to print the contents of the file
# print f.read()

# f.close()


#or use this:
import json
import random 

with open('data.json', 'r') as f:
	#print f.read()
	data = json.loads(f.read())
#this is going to print a random thing
	print random.choice(data)