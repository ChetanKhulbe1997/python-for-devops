# Basic API
# import requests

# url = "https://dog.ceo/api/breeds/image/random"

# response = requests.get(url=url)

# for key,value in response.json().items():
#     if key == "status":
#         if value == "success":
#             print("API is working")



# HOLIDAYS-Calender API
import requests

url = "https://holidayapi.com/v1/holidays"

params = {
    "key": "fd4c31a4-3d30-4a46-aa10-ccde16a9b9ec",
    "country": "IN",
    "year": 2024,
    "pretty": True
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()          
    holidays = data["holidays"]     

    public_holidays = [h for h in holidays if h["public"]]

    print("Status Code:", response.status_code)
    print(response.json())

    for h in public_holidays:
        print(h["date"], "-", h["name"])
else:
    print("API error:", response.text)


