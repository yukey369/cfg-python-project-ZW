import requests

id = "84600bca7507293656495e8972aec659"


def query_weather(payload):
    payload = {'q':city, UK', 'units':'metric', 'appid':id}
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    response = requests.get(endpoint, params=payload)

    return jsonify(response)['main']['temp']

def jsonify(response):
    json_response = response.json()
    return json_response

print("The temperature in {} is {}". format('London', query_weather('lo')))
