import requests

API_KEY = "9cb87bd80332508f48864b426caea33b"


def get_data(place, forcast=None,):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = forcast * 8
    filtered_data = filtered_data[:nr_values]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="tokyo", forcast=2,))
