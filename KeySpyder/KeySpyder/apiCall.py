import requests

api_url = "http://127.0.0.1:5000/data"


def postRequest(desktopId, body):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Prepare data as a dictionary
    data = {
        "desktopId": desktopId,
        "data": "".join(body)  # Convert list to string
    }

    print(f"Sending Data: {data}")

    # Sending POST request
    response = requests.post(api_url, data=data, headers=headers)

    if response.status_code == 200:
        print("Data Successfully Sent")
        print(response.json())
    else:
        print("Failed to send data")
        print(response.text)
