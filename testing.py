import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

headers = {
	"x-rapidapi-key": "119993f560msh2752b9e1ac6a02cp137297jsn92c16e918bbb",
	"x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())