import requests         #We use requests to send data to an API and to get the data back.
                            #*The httprequests library is used to send HTTP requests to APIs and receive responses.
payload = {
    "model": "random-model",
    "prompt": "what is ai",
    "temp": 0.02
}

print("Payload type:", type(payload))   #payload is a dictionary,data we want to send to the API. 
print("Payload:", payload)

response = requests.post("https://jsonplaceholder.typicode.com/posts",json=payload)      #the requests library converts that Python dictionary into JSON file and sends it in the request body.
        #Now the POST request is sent.The server receives the request, processes it, and sends something back.
print("Response type:", type(response)) #response is a Response object not string or dictionary. It contains the server's response to the HTTP request.
print("Status code:", response.status_code)
print("Response text:", response.text)

data = response.json()

print("Data type:", type(data))
print("Response data:", data)

# requests.post() → sends data to an API using the POST method
# API_URL → tells Python where to send the request
# json=payload → takes the Python dictionary in payload and sends it as JSON
# response → stores whatever the API sends back


