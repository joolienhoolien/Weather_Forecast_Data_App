import requests

API_KEY = "91e91e6d45f0d25c57a5de6ea339281b"

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}&units=imperial"
    response = requests.get(url)
    data = response.json()
    chunks_per_day = 8

    #Filter days
    data = [data['list'][0:forecast_days * chunks_per_day][i] for i in range(forecast_days * chunks_per_day)]

    #From that limited data, return...
    dates = [(data[i]['dt_txt']) for i in range(len(data))]
    if kind.lower() == "sky":
        data = [(data[i]['weather'][0]['main']) for i in range(len(data))]
    elif kind.lower() == "temperature":
        data = [(data[i]['main']['temp']) for i in range(len(data))]

    return  dates, data

if __name__ == "__main__":
    print(get_data("Tokyo", 1, "temperature"))