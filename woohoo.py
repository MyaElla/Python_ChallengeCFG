from flask import Flask
from flask import render_template

import json
import random

#special varial in python
app = Flask (__name__)

#declare an empty list call words
words = []

#we are opening the data.json file, and open returns a file object which we are storing in a variable call f.. f is just shorthand for file but you can use anything. we are then completely replacing the previous empty list with the json decoded contents of the file.
with open('data.json', 'r') as f:
	words = json.loads(f.read()) 

print words

@app.route('/')
def home():
	quote = random.choice(words)
	return render_template('index.html', quote=quote)
	return words

app.run()