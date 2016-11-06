from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
   return "Hello world"

@app.route("/<greeting>/<name>/<time>")
def greeting(greeting, name, time):
	return render_template("hello.html", greeting=greeting.title(),name=name.title(),time=time.title())

if __name__ == 'main':
	app.run()