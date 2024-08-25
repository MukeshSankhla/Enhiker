"""
Project: Enhiker - A Portable Weather Decision Maker
Author: Mukesh Sankhla
Website: https://www.makerbrains.com
Social Media: Instagram @mukesh.diy

Description:
This Python script interfaces with an environmental sensor and a GNSS (Global Navigation Satellite System) sensor,
displaying real-time data on a Pygame-powered graphical user interface (GUI). The script is designed to monitor 
various environmental parameters such as temperature, humidity, UV intensity, atmospheric pressure, and light intensity. 
It also gathers location data using the GNSS sensor and evaluates the environmental conditions, providing a health rating 
based on the collected data.
"""

import time
import os
import csv
from pinpong.board import Board
from lib.DFRobot_Environmental_Sensor import *
from lib.DFRobot_GNSS_I2C import DFRobot_GNSS_I2C, MODE_GPS_BEIDOU_GLONASS
from decision_maker import evaluate_conditions
from advance_decision_maker import evaluate_advance_conditions
from heat_index import calculate_heat_index
from internet_data import get_weather_data
from display import display_loading_screen, display_data


API_Key = '43f22249d3d42ec5daf08c4384ca809b'

# Initialize the board
Board().begin()

# Initialize sensors
SEN0501 = DFRobot_Environmental_Sensor_I2C(bus=0x01, addr=0x22)
GNSS = DFRobot_GNSS_I2C()
GNSS.set_gnss_mode(MODE_GPS_BEIDOU_GLONASS)
GNSS.set_enable_power()

# Define constants
MINIMUM_SATELLITES = 3  # Minimum number of satellites required for reliable data
DELAY_SECONDS = 5  # Delay between each loop iteration

# Function to check Wi-Fi connection status
def check_wifi():
    return os.system("ping -c 1 google.com") == 0

# Setup function to initialize sensors
def setup():
    while not SEN0501.begin():
        print("Sensor initialization failed!")
        time.sleep(1)
    print("Sensor initialization successful!")

# Main loop function to read sensor data, evaluate conditions, and display the data
def loop():
    # Wait until the required number of satellites is found
    while True:
        num_satellites = GNSS.get_num_sta_used()
        if num_satellites > MINIMUM_SATELLITES:
            break
        print(f"Searching... Satellites found: {num_satellites}")
        display_loading_screen()
        time.sleep(1)

    # Read data from sensors
    temperature = SEN0501.get_temperature(TEMP_C)
    humidity = SEN0501.get_humidity()
    uv_intensity = SEN0501.get_ultraviolet_intensity()
    light_intensity = SEN0501.get_luminousintensity()
    pressure = SEN0501.get_atmosphere_pressure(HPA)
    elevation = SEN0501.get_elevation()
    heat_index = calculate_heat_index(temperature, humidity)

    # Get GPS data if the satellite count is sufficient
    latitude, longitude, altitude = None, None, None
    current_date, current_time = None, None
    if num_satellites > MINIMUM_SATELLITES:
        lat_data = GNSS.get_lat()
        lon_data = GNSS.get_lon()
        alt_data = GNSS.get_alt()
        
        latitude = f"{lat_data[0]:.6f}° {lat_data[1]}"
        longitude = f"{lon_data[0]:.6f}° {lon_data[1]}"
        altitude = f"{alt_data:.2f} m"

        # Get the date and time from GNSS
        current_date = GNSS.get_date()
        current_time = GNSS.get_time()

    wifi_connected = check_wifi()

    air_quality, wind_speed, wind_direction, sunrise, sunset, clouds = None, None, None, None, None, None
    if wifi_connected:
        air_quality, wind_speed, wind_direction, sunrise, sunset, clouds = get_weather_data(latitude, longitude, API_Key)

    # Print sensor data to the console
    print(f"Date: {current_date}")
    print(f"Time: {current_time}")
    print(f"Temperature: {temperature} 'C")
    print(f"Humidity: {humidity} %")
    print(f"Ultraviolet intensity: {uv_intensity} mw/cm2")
    print(f"Luminous intensity: {light_intensity} lx")
    print(f"Atmospheric pressure: {pressure} hpa")
    print(f"Elevation: {elevation} m")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print(f"Altitude: {altitude}")
    print(f"Heat Index: {heat_index}")
    print(f"Satellites: {num_satellites}")
    print(f"Wi-Fi Status: {wifi_connected}")
    if wifi_connected:
        print(f"Air Quality: {air_quality}")
        print(f"Wind Speed: {wind_speed}")
        print(f"Wind Diredction: {wind_direction}")
        print(f"Sunrise: {sunrise}")
        print(f"Sunset: {sunset}")
        print(f"Clouds: {clouds}")
         # Evaluate environmental advance conditions based on sensor and internet data
        rating, message = evaluate_advance_conditions(current_time, temperature, humidity, uv_intensity, light_intensity, pressure, elevation, heat_index, air_quality, wind_speed, wind_direction, clouds)
    else:
        # Evaluate environmental conditions based on sensor data
        rating, message = evaluate_conditions(temperature, humidity, uv_intensity, light_intensity, pressure, elevation, heat_index)
    print("-------------------------------------")

    display_data(wifi_connected, current_date, current_time, num_satellites, temperature, humidity, heat_index, light_intensity, uv_intensity, pressure, elevation, latitude, longitude, rating, message, air_quality, wind_speed, wind_direction, sunrise, sunset, clouds)
    with open('data_log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([wifi_connected, current_date, current_time, num_satellites, temperature, humidity, heat_index, light_intensity, uv_intensity, pressure, elevation, latitude, longitude, rating, message, air_quality, wind_speed, wind_direction, sunrise, sunset, clouds])
    
    # Delay before the next loop iteration
    time.sleep(DELAY_SECONDS)

if __name__ == "__main__":
    setup()  # Initialize the sensors
    while True:
        loop()  # Continuously read and display sensor data
