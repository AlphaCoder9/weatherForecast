import requests

API_KEY = "9cb87bd80332508f48864b426caea33b"


def get_data(place, forcast=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = forcast * 8
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    if kind == "Sky view":
        filtered_data = [dict['weather'][0]['description'] for dict in filtered_data]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="tokyo", forcast=1, kind="temperature"))
