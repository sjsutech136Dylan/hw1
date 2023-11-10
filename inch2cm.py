from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
        return 'Hello World'

@app.route('/inch2cm')
def cm2inch():
	return render_template('inch2cm.html')

@app.route('/inch2cm_action')
def cm2inch_action():
	inches = request.args.get("inches")
	return "inches="+str(inches)+" cm="+str(float(inches) / 2.54)

if __name__ == '__main__':
        app.run(host="0.0.0.0",port=5001)
