from flask import Flask

application = flask(__name__)

@application.route('/')
def hello():
	return "Hello World"

if __name__ == "__main__":
	application.run()
