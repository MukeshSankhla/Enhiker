import requests
from datetime import datetime

def get_weather_data(lat, lon, api_key):

    lat_des = lat[0:-3]
    lon_des = lon[0:-3]
    # Define the API endpoint for current weather data
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat_des}&lon={lon_des}&appid={api_key}&units=metric"
    
    # Define the API endpoint for air quality data
    air_quality_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat_des}&lon={lon_des}&appid={api_key}"
    
    try:
        # Fetch current weather data
        weather_response = requests.get(weather_url)
        weather_response.raise_for_status()  # Raise an exception for HTTP errors
        weather_data = weather_response.json()
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
        return None
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return None
    except ValueError:
        print("Error: Unable to decode weather response into JSON.")
        return None

    try:
        # Fetch air quality data
        air_quality_response = requests.get(air_quality_url)
        air_quality_response.raise_for_status()  # Raise an exception for HTTP errors
        air_quality_data = air_quality_response.json()
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
        return None
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return None
    except ValueError:
        print("Error: Unable to decode air quality response into JSON.")
        return None

    # Extract relevant information with error handling
    try:
        wind_speed = weather_data['wind']['speed']
        wind_direction = weather_data['wind']['deg']
        sunrise = datetime.utcfromtimestamp(weather_data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
        sunset = datetime.utcfromtimestamp(weather_data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')
        clouds = weather_data.get('clouds', {}).get('all', "Data not available")
        air_quality_index = air_quality_data['list'][0]['main']['aqi']
    except KeyError as key_err:
        print(f"Key error: {key_err}")
        wind_speed = "Data not available"
        wind_direction = "Data not available"
        sunrise = "Data not available"
        sunset = "Data not available"
        clouds = "Data not available"
        air_quality_index = "Data not available"

    # Return the extracted data
    return (air_quality_index, wind_speed, wind_direction, sunrise, sunset, clouds)
