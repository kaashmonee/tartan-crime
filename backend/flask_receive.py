from flask import Flask
app = Flask(__name__)


@app.route('/<arg_1>') #Route is denoted by the 
def hello_world(arg_1):
	#data = request.data
	#print(data)
	return 'Hello, World!' + ' ' + arg_1

@app.route('/')
def humaness():
	return 'Intelligence!'


if __name__ == "__main__": 
    app.run(host='0.0.0.0')

