import requests


url = "https://www.radissonhotels.com/en-us/hotels/radisson-blu-lagos-anchorage/rooms"

file = open("get_fiel.html", "+wb")

response = requests.get(url)

print(response.text)

file.write(response.content)
file.close