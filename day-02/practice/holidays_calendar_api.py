# holidays_calender_api
import requests                                                       # Step 1 import requests library

API_KEY = "eb855af6-b329-431c-80d8-0472877807dd"                      # Step 2 get API key

api_url = "https://holidayapi.com/v1/holidays"                        # Step 3 find a base URL


def get_holidays_data(country_code):                                  # Step 4 create function to get data
    
    query = f"?country={country_code}&year=2024&key={API_KEY}"        # Step 5 create query string
    response = requests.get(url=api_url+query)                        # Step 6 make a GET request
    
    data = response.json()                                            # Step 7 parse JSON response

    return data.get("holidays", [])                                   # Step 8 return holidays list


country_code = input("Enter country code (e.g., US, IN, GB, AU): ")   # Step 9 get user input
holidays = get_holidays_data(country_code)                            # Step 10 call function to get holidays

holiday_dict = {                                                      # Step 11 create dictionary comprehension
    h["date"]: {                                                      # Step 12 structure holiday data
        "name": h["name"],                                            # Step 13 add holiday name
        "public": h["public"],                                        # Step 14 add public holiday status
        "weekday": h["weekday"]["date"]["name"]                       # Step 15 add weekday name
    }
    for h in holidays                                                 # Step 16 iterate over holidays list
}

print(holiday_dict)                                                   # Step 17 print the holiday dictionary
