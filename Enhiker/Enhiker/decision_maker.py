def evaluate_conditions(temperature, humidity, uv_intensity, light_intensity, pressure, elevation, heat_index):
    rating = "Suitable: Best"
    message = "The location is ideal for camping or staying."

    # Very High UV Intensity
    if uv_intensity > 11:
        rating = "Can't stay"
        message = "Extreme UV intensity makes it unsafe to stay outdoors."

    # High Heat Index and High Humidity
    elif heat_index > 45 and humidity > 70:
        rating = "Leave the place immediately"
        message = "Dangerously high heat index and humidity; staying here can lead to heat stroke."

    # High Temperature and Low Pressure
    elif temperature > 40 and pressure < 950:
        rating = "Can't stay"
        message = "Extreme heat combined with low pressure makes the environment hazardous."

    # Low Temperature and High Pressure
    elif temperature < -20 and pressure > 1020:
        rating = "Can't stay"
        message = "Severely cold conditions with high pressure can cause hypothermia."

    # Mild Temperature, High UV, and High Light Intensity
    elif 20 <= temperature <= 28 and uv_intensity > 8 and light_intensity > 12000:
        rating = "Moderate"
        message = "Moderate temperature but intense sunlight and UV exposure; caution is advised."

    # High Temperature, Low Humidity, and High Elevation
    elif temperature > 35 and humidity < 30 and elevation > 3000:
        rating = "Can't stay"
        message = "High temperature and low humidity at high elevation can lead to dehydration."

    # Low Temperature, Low Humidity, and High UV
    elif temperature < 0 and humidity < 20 and uv_intensity > 7:
        rating = "Can't stay"
        message = "Cold, dry conditions with high UV exposure can be dangerous."

    # High Temperature, High Humidity, and High UV
    elif temperature > 35 and humidity > 70 and uv_intensity > 8:
        rating = "Can't stay"
        message = "Hot, humid conditions with high UV exposure are very risky."

    # Low Temperature and High Elevation
    elif temperature < -10 and elevation > 2000:
        rating = "Can't stay"
        message = "Low temperatures at high elevation can cause frostbite and altitude sickness."

    # High Heat Index and Moderate Humidity
    elif 35 <= heat_index <= 40 and 60 <= humidity <= 80:
        rating = "Moderate"
        message = "High heat index with moderate humidity; caution is advised."

    # Low Temperature, High Humidity, and Low Pressure
    elif temperature < 5 and humidity > 80 and pressure < 950:
        rating = "Can't stay"
        message = "Cold, humid, and low-pressure conditions can lead to respiratory issues."

    # Moderate Temperature and High UV
    elif 25 <= temperature <= 30 and uv_intensity > 10:
        rating = "Moderate"
        message = "Moderate temperature but high UV intensity; sun protection is necessary."

    # High Temperature, Low Humidity, and High UV
    elif temperature > 35 and humidity < 30 and uv_intensity > 8:
        rating = "Can't stay"
        message = "Hot and dry conditions with high UV exposure are dangerous."

    # High Altitude and High UV
    elif elevation > 3000 and uv_intensity > 8:
        rating = "Can't stay"
        message = "High elevation with intense UV radiation can cause altitude sickness and sunburn."

    # Low Pressure and High Heat Index
    elif pressure < 930 and heat_index > 40:
        rating = "Can't stay"
        message = "Low pressure with high heat index; dangerous conditions for staying outdoors."

    # Low Temperature, Low Humidity, and High Light Intensity
    elif temperature < 5 and humidity < 20 and light_intensity > 15000:
        rating = "Moderate"
        message = "Cold and dry but bright conditions; staying might be uncomfortable."

    # Very High Light Intensity and High UV
    elif light_intensity > 20000 and uv_intensity > 10:
        rating = "Can't stay"
        message = "Extremely intense sunlight with high UV radiation; staying outdoors is unsafe."

    # Cold and High Pressure
    elif temperature < -15 and pressure > 1010:
        rating = "Can't stay"
        message = "Extremely cold and stable conditions can lead to frostbite."

    # Hot and Low Pressure
    elif temperature > 40 and pressure < 940:
        rating = "Can't stay"
        message = "Hot and low-pressure conditions can cause heat exhaustion."

    # High Temperature, Moderate Humidity, and High Pressure
    elif 30 <= temperature <= 35 and 40 <= humidity <= 60 and pressure > 1000:
        rating = "Moderate"
        message = "Warm and stable conditions; manageable but not ideal."

    # High Elevation, Moderate Temperature, and Low Pressure
    elif elevation > 3000 and 15 <= temperature <= 25 and pressure < 900:
        rating = "Moderate"
        message = "High elevation with moderate temperature and low pressure; caution is advised."

    # High Heat Index, High Humidity, and Low Pressure
    elif heat_index > 40 and humidity > 70 and pressure < 950:
        rating = "Can't stay"
        message = "High heat index with high humidity and low pressure creates hazardous conditions."

    # Low Temperature, High Humidity, and High UV
    elif temperature < 10 and humidity > 80 and uv_intensity > 6:
        rating = "Moderate"
        message = "Cold and humid with moderate UV exposure; staying might be uncomfortable."

    # Mild Temperature, Low Humidity, and Low Pressure
    elif 15 <= temperature <= 25 and humidity < 40 and pressure < 950:
        rating = "Moderate"
        message = "Mild temperature but dry and low pressure; conditions are manageable but not ideal."

    # Moderate Conditions with High UV
    elif 20 <= temperature <= 30 and 40 <= humidity <= 60 and uv_intensity > 8:
        rating = "Moderate"
        message = "Comfortable temperature and humidity but high UV; sun protection is needed."

    # High Temperature, High Light Intensity, and Low Humidity
    elif temperature > 35 and light_intensity > 15000 and humidity < 30:
        rating = "Can't stay"
        message = "High temperature and intense sunlight with low humidity can lead to dehydration."

    # Low Temperature, High Pressure, and High UV
    elif temperature < 0 and pressure > 1020 and uv_intensity > 7:
        rating = "Can't stay"
        message = "Cold and high pressure with intense UV exposure can be dangerous."

    # Moderate Temperature, High Humidity, and High Light Intensity
    elif 20 <= temperature <= 28 and humidity > 70 and light_intensity > 12000:
        rating = "Moderate"
        message = "Moderate temperature but high humidity and intense sunlight; caution is advised."

    # High Elevation, High UV, and High Light Intensity
    elif elevation > 3000 and uv_intensity > 8 and light_intensity > 15000:
        rating = "Can't stay"
        message = "High elevation with intense UV radiation and sunlight can cause altitude sickness and sunburn."

    # Low Temperature, Low Humidity, and High Elevation
    elif temperature < 0 and humidity < 20 and elevation > 3000:
        rating = "Can't stay"
        message = "Cold and dry conditions at high elevation can lead to frostbite and altitude sickness."

    # High Heat Index, High Humidity, and High Light Intensity
    elif heat_index > 40 and humidity > 70 and light_intensity > 15000:
        rating = "Can't stay"
        message = "High heat index with high humidity and intense sunlight creates hazardous conditions."

    # Low Temperature, High Pressure, and High Elevation
    elif temperature < -10 and pressure > 1020 and elevation > 3000:
        rating = "Can't stay"
        message = "Low temperatures with high pressure and elevation can cause frostbite and altitude sickness."

    # High Temperature, High Humidity, and Low Light Intensity
    elif temperature > 35 and humidity > 70 and light_intensity < 8000:
        rating = "Moderate"
        message = "Hot and humid conditions with low sunlight; staying might be uncomfortable."

    # Low Temperature, Low Pressure, and High Humidity
    elif temperature < 0 and pressure < 950 and humidity > 80:
        rating = "Can't stay"
        message = "Cold, low-pressure, and humid conditions can lead to respiratory issues."

    # High Temperature, High Pressure, and High Light Intensity
    elif temperature > 35 and pressure > 1000 and light_intensity > 15000:
        rating = "Moderate"
        message = "Hot and stable conditions with intense sunlight; caution is advised."

    # Low Temperature, High Humidity, and Low Light Intensity
    elif temperature < 5 and humidity > 80 and light_intensity < 8000:
        rating = "Moderate"
        message = "Cold and humid conditions with low sunlight; staying might be uncomfortable."

    # High Temperature, High Humidity, and High Pressure
    elif temperature > 35 and humidity > 70 and pressure > 1000:
        rating = "Moderate"
        message = "Hot, humid, and stable conditions; staying might be uncomfortable."

    # Moderate Temperature, High UV, and High Elevation
    elif 20 <= temperature <= 28 and uv_intensity > 8 and elevation > 3000:
        rating = "Moderate"
        message = "Moderate temperature with intense UV exposure at high elevation; sun protection is necessary."

    # High Temperature, Low Humidity, and High Pressure
    elif temperature > 35 and humidity < 30 and pressure > 1000:
        rating = "Moderate"
        message = "Hot, dry, and stable conditions; caution is advised."
    
        # Moderate Temperature, Moderate Humidity, and High UV
    elif 20 <= temperature <= 25 and 50 <= humidity <= 70 and uv_intensity > 8:
        rating = "Moderate"
        message = "Comfortable temperature and humidity but high UV; sun protection is needed."

    # High Temperature, Low Humidity, and Low Pressure
    elif temperature > 35 and humidity < 30 and pressure < 950:
        rating = "Can't stay"
        message = "Hot and dry conditions with low pressure can cause heat exhaustion."

    # Low Temperature, Low Humidity, and Moderate UV
    elif temperature < 5 and humidity < 30 and uv_intensity > 5:
        rating = "Moderate"
        message = "Cold and dry with moderate UV exposure; staying might be uncomfortable."

    # Mild Temperature, Low Humidity, and High Light Intensity
    elif 15 <= temperature <= 20 and humidity < 30 and light_intensity > 15000:
        rating = "Moderate"
        message = "Mild temperature but low humidity and intense sunlight; staying might be uncomfortable."

    # High Temperature, High Humidity, and Moderate UV
    elif temperature > 35 and humidity > 70 and 5 <= uv_intensity <= 8:
        rating = "Moderate"
        message = "Hot and humid with moderate UV exposure; caution is advised."

    # Low Temperature, High Pressure, and Low Humidity
    elif temperature < 0 and pressure > 1020 and humidity < 30:
        rating = "Can't stay"
        message = "Cold and dry conditions with high pressure can cause hypothermia."

    # Moderate Temperature, Moderate Humidity, and High Light Intensity
    elif 20 <= temperature <= 28 and 50 <= humidity <= 70 and light_intensity > 15000:
        rating = "Moderate"
        message = "Comfortable temperature and humidity but intense sunlight; sun protection is needed."

    # High Temperature, Low Humidity, and Low Elevation
    elif temperature > 35 and humidity < 30 and elevation < 1000:
        rating = "Moderate"
        message = "Hot and dry conditions at low elevation; staying might be uncomfortable."

    # Low Temperature, High Pressure, and High Light Intensity
    elif temperature < 5 and pressure > 1020 and light_intensity > 15000:
        rating = "Moderate"
        message = "Cold conditions with high pressure and intense sunlight; caution is advised."

    # High Heat Index, Low Humidity, and High UV
    elif heat_index > 40 and humidity < 30 and uv_intensity > 8:
        rating = "Can't stay"
        message = "High heat index with low humidity and intense UV exposure can cause heat stroke."

    # Low Temperature, Low Pressure, and Low Light Intensity
    elif temperature < 5 and pressure < 950 and light_intensity < 8000:
        rating = "Moderate"
        message = "Cold and low-pressure conditions with low sunlight; staying might be uncomfortable."

    # High Temperature, High Pressure, and Low Humidity
    elif temperature > 35 and pressure > 1000 and humidity < 30:
        rating = "Moderate"
        message = "Hot and dry conditions with high pressure; caution is advised."

    # Low Temperature, Moderate Humidity, and High UV
    elif temperature < 5 and 40 <= humidity <= 60 and uv_intensity > 8:
        rating = "Moderate"
        message = "Cold conditions with moderate humidity and high UV; caution is advised."

    # High Temperature, Moderate Pressure, and Low Humidity
    elif temperature > 35 and 950 <= pressure <= 1000 and humidity < 30:
        rating = "Moderate"
        message = "Hot and dry conditions with moderate pressure; caution is advised."

    # Low Temperature, High UV, and High Light Intensity
    elif temperature < 5 and uv_intensity > 8 and light_intensity > 15000:
        rating = "Moderate"
        message = "Cold conditions with high UV and intense sunlight; sun protection is needed."

    # High Temperature, Low Humidity, and Moderate UV
    elif temperature > 35 and humidity < 30 and 5 <= uv_intensity <= 8:
        rating = "Moderate"
        message = "Hot and dry conditions with moderate UV exposure; caution is advised."

    # Low Temperature, Low Pressure, and High UV
    elif temperature < 5 and pressure < 950 and uv_intensity > 8:
        rating = "Moderate"
        message = "Cold and low-pressure conditions with high UV; caution is advised."

    # High Temperature, High Humidity, and High Pressure
    elif temperature > 35 and humidity > 70 and pressure > 1020:
        rating = "Moderate"
        message = "Hot, humid, and stable conditions; staying might be uncomfortable."

    # Moderate Temperature, Low Pressure, and High UV
    elif 20 <= temperature <= 28 and pressure < 950 and uv_intensity > 8:
        rating = "Moderate"
        message = "Comfortable temperature but low pressure and high UV; sun protection is needed."

    # Low Temperature, High Pressure, and High Humidity
    elif temperature < 5 and pressure > 1020 and humidity > 70:
        rating = "Moderate"
        message = "Cold conditions with high pressure and humidity; staying might be uncomfortable."

    # High Temperature, Low Pressure, and Moderate Humidity
    elif temperature > 35 and pressure < 950 and 40 <= humidity <= 60:
        rating = "Moderate"
        message = "Hot conditions with low pressure and moderate humidity; caution is advised."

    # Low Temperature, High Pressure, and Low UV
    elif temperature < 5 and pressure > 1020 and uv_intensity < 3:
        rating = "Moderate"
        message = "Cold and stable conditions with low UV exposure; staying might be uncomfortable."

    # Moderate Temperature, Moderate Humidity, and Low UV
    elif 20 <= temperature <= 28 and 50 <= humidity <= 70 and uv_intensity < 3:
        rating = "Suitable: Best"
        message = "Comfortable temperature, humidity, and low UV exposure; ideal for staying."

    # High Temperature, Low Humidity, and High Pressure
    elif temperature > 35 and humidity < 30 and pressure > 1020:
        rating = "Moderate"
        message = "Hot and dry conditions with high pressure; caution is advised."

    # Low Temperature, Low Pressure, and Low Humidity
    elif temperature < 5 and pressure < 950 and humidity < 30:
        rating = "Moderate"
        message = "Cold and dry conditions with low pressure; staying might be uncomfortable."

    # High Temperature, Low Pressure, and High UV
    elif temperature > 35 and pressure < 950 and uv_intensity > 8:
        rating = "Moderate"
        message = "Hot conditions with low pressure and high UV exposure; sun protection is needed."

    # Low Temperature, Moderate Humidity, and Low Pressure
    elif temperature < 5 and 40 <= humidity <= 60 and pressure < 950:
        rating = "Moderate"
        message = "Cold conditions with moderate humidity and low pressure; staying might be uncomfortable."

    # High Temperature, Low Humidity, and High Light Intensity
    elif temperature > 35 and humidity < 30 and light_intensity > 15000:
        rating = "Moderate"
        message = "Hot and dry conditions with intense sunlight; staying might be uncomfortable."

    # Low Temperature, High Humidity, and High Pressure
    elif temperature < 5 and humidity > 70 and pressure > 1020:
        rating = "Moderate"
        message = "Cold and humid conditions with high pressure; staying might be uncomfortable."

    # High Temperature, High Pressure, and High UV
    elif temperature > 35 and pressure > 1020 and uv_intensity > 8:
        rating = "Moderate"
        message = "Hot and stable conditions with intense UV exposure; sun protection is needed."

    # Low Temperature, High Light Intensity, and Low Humidity
    elif temperature < 5 and light_intensity > 15000 and humidity < 30:
        rating = "Moderate"
        message = "Cold and dry conditions with intense sunlight; staying might be uncomfortable."

    # High Temperature, Low Light Intensity, and High Humidity
    elif temperature > 35 and light_intensity < 8000 and humidity > 70:
        rating = "Moderate"
        message = "Hot and humid conditions with low sunlight; staying might be uncomfortable."

    # Low Temperature, High Pressure, and Low Light Intensity
    elif temperature < 5 and pressure > 1020 and light_intensity < 8000:
        rating = "Moderate"
        message = "Cold and stable conditions with low sunlight; staying might be uncomfortable."

    # High Temperature, Low Pressure, and Low Humidity
    elif temperature > 35 and pressure < 950 and humidity < 30:
        rating = "Moderate"
        message = "Hot and dry conditions with low pressure; caution is advised."

    # Low Temperature, High UV, and Low Light Intensity
    elif temperature < 5 and uv_intensity > 8 and light_intensity < 8000:
        rating = "Moderate"
        message = "Cold conditions with high UV exposure and low sunlight; sun protection is needed."

    # High Temperature, High UV, and High Light Intensity
    elif temperature > 35 and uv_intensity > 8 and light_intensity > 15000:
        rating = "Moderate"
        message = "Hot conditions with intense UV exposure and sunlight; sun protection is needed."

    # Final Message
    print(f"Rating: {rating}")
    print(f"Message: {message}")
    return rating, message