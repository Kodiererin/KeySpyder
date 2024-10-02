from flask import Flask , request

app = Flask(__name__)

# Step 1:
# Create an API which receives the DesktopID and Keys
# Here the DesktopID is the parameter
# Keys are the Body

# Step 2:
# Store the data in the MongoDB



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/data' , methods=['POST'])
def getData():
    print(request.form['Name'])
    print(request.args['Keys'])
    return "Done"


if __name__ == '__main__':
    app.run()
