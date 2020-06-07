import requests

KEY = 'e1ee55658d4a2b28c4841e373c3b3d87'
URL = 'https://api.darksky.net/forecast/{}/{},{}'


def _api_on(lat, lng):

    url = URL.format(KEY, lat, lng)
    try:
        resp = requests.head(url)
    except ConnectionError:
        resp = False

    return 200 <= resp.status_code <= 299


def request_api_temperature(lat, lng):

    if _api_on(lat, lng):
        url = URL.format(KEY, lat, lng)
        data = requests.get(url)
        resp = data.json()

    else:
        resp = {}

    return resp


def calculate_temperature(temperature):
    return int((temperature - 32) * 5.0 / 9.0)


def get_temperature(lat, lng):

    data = request_api_temperature(lat, lng)
    temperature = data.get('currently').get('temperature')

    if temperature:
        resp = calculate_temperature(temperature)
    else:
        resp = None

    return resp




