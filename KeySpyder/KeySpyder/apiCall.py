import requests

api_url = "http://127.0.0.1:5000/data"

def postRequest(desktopId , body):
    headers = {
        "Content-Type": "application/x-www-from-urlencoded"
    }


    # Sending POST request with form data
    response = requests.post(api_url, data=body, headers=headers)

    if response.status_code == 200:
        print("Data Successfully Sent")
        print(response.json())
    else:
        print("Data failed to sent")
        print(response.text)

