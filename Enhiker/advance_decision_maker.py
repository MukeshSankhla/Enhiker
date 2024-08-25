def evaluate_advance_conditions(current_time, temperature, humidity, uv_intensity, light_intensity, pressure, elevation, heat_index, air_quality, wind_speed, wind_direction, clouds):
    # Default rating and message
    rating = "Suitable: Best"
    message = "The location is ideal for camping or staying."

    # Extreme conditions
    if temperature > 40:
        rating = "Leave Immediately"
        message = "Extremely high temperature. Risk of heatstroke."
    elif temperature < -10:
        rating = "Leave Immediately"
        message = "Extremely low temperature. Risk of frostbite."
    elif humidity > 90 and temperature > 35:
        rating = "Leave Immediately"
        message = "Dangerously high humidity and temperature."
    elif humidity < 10 and temperature > 30:
        rating = "Leave Immediately"
        message = "Very low humidity and high temperature. Risk of dehydration."
    elif heat_index > 45:
        rating = "Leave Immediately"
        message = "Heat index is dangerously high. Risk of heatstroke."
    elif pressure < 930:
        rating = "Leave Immediately"
        message = "Very low pressure. Storm conditions likely."
    elif uv_intensity > 11:
        rating = "Leave Immediately"
        message = "Extreme UV radiation. Risk of severe sunburn."
    elif wind_speed > 80:
        rating = "Leave Immediately"
        message = "Gale-force winds. Seek immediate shelter."
    elif air_quality > 300:
        rating = "Leave Immediately"
        message = "Hazardous air quality. Do not stay outdoors."
    elif clouds == 100 and pressure < 950:
        rating = "Leave Immediately"
        message = "Heavy clouds with low pressure. Severe storm imminent."

    # High caution conditions
    elif 35 <= temperature <= 40:
        rating = "Caution: Very Hot"
        message = "Very hot temperature. Avoid prolonged outdoor activity."
    elif 30 <= temperature <= 35 and humidity > 80:
        rating = "Caution: Hot and Humid"
        message = "Hot and humid. Stay hydrated and take breaks in the shade."
    elif humidity > 80 and pressure < 1000:
        rating = "Caution: Humid with Low Pressure"
        message = "High humidity with low pressure. Possible rain or thunderstorms."
    elif uv_intensity > 8 and light_intensity > 70000:
        rating = "Caution: Strong Sunlight"
        message = "Strong sunlight with high UV. Wear sunscreen and protective clothing."
    elif light_intensity < 100 and clouds > 90:
        rating = "Caution: Low Light"
        message = "Very low light conditions. Limited visibility, avoid hiking."
    elif wind_speed > 60 and wind_direction in range(0, 180):
        rating = "Caution: Strong Northern/Eastern Winds"
        message = "Strong winds from the north/east. Secure outdoor items."
    elif wind_speed > 60 and wind_direction in range(180, 360):
        rating = "Caution: Strong Southern/Western Winds"
        message = "Strong winds from the south/west. Secure outdoor items."
    elif pressure < 950 and clouds > 80:
        rating = "Caution: Low Pressure and Cloudy"
        message = "Low pressure with heavy clouds. Rain or storms likely."
    elif temperature < 5 and wind_speed > 30:
        rating = "Caution: Cold and Windy"
        message = "Cold temperature with strong winds. Dress warmly."
    elif air_quality > 150 and air_quality <= 200:
        rating = "Caution: Unhealthy Air Quality"
        message = "Unhealthy air quality. Limit outdoor activities, especially for sensitive groups."

    # Moderate conditions
    elif 25 <= temperature <= 30 and humidity < 60:
        rating = "Moderate: Warm and Dry"
        message = "Warm and dry. Good for most activities."
    elif 20 <= temperature <= 25 and humidity > 60:
        rating = "Moderate: Comfortable"
        message = "Comfortable temperature with some humidity."
    elif 15 <= temperature < 20 and light_intensity > 50000:
        rating = "Moderate: Pleasant with Sun"
        message = "Pleasant temperature with sunny conditions."
    elif uv_intensity > 3 and light_intensity > 30000:
        rating = "Moderate: UV Alert"
        message = "Moderate UV levels. Take precautions if outdoors."
    elif air_quality > 100 and air_quality <= 150:
        rating = "Moderate: Air Quality Concern"
        message = "Moderate air quality. Some may experience discomfort."
    elif wind_speed > 20 and wind_speed <= 40 and clouds < 50:
        rating = "Moderate: Breezy"
        message = "Breezy conditions with some clouds. Pleasant for most activities."
    elif pressure > 1015 and clouds < 20:
        rating = "Moderate: Clear and Calm"
        message = "Clear skies with calm conditions. Ideal for outdoor activities."

    # Suitable conditions
    elif 20 <= temperature <= 25 and humidity < 50:
        rating = "Suitable: Ideal"
        message = "Ideal weather for outdoor activities."
    elif 15 <= temperature < 20 and humidity < 50:
        rating = "Suitable: Cool"
        message = "Cool and comfortable weather for outdoor activities."
    elif uv_intensity < 3 and light_intensity > 30000:
        rating = "Suitable: Mild Sun"
        message = "Mild sunlight with low UV. Safe for most outdoor activities."
    elif air_quality <= 50:
        rating = "Suitable: Excellent Air Quality"
        message = "Excellent air quality. Perfect for outdoor activities."
    elif wind_speed <= 20 and clouds < 30:
        rating = "Suitable: Light Breeze"
        message = "Light breeze with few clouds. Perfect for outdoor activities."
    elif pressure > 1020 and clouds < 10:
        rating = "Suitable: Clear Skies"
        message = "Clear skies and high pressure. Ideal for stargazing."
    elif clouds < 20 and light_intensity > 10000:
        rating = "Suitable: Mostly Sunny"
        message = "Mostly sunny with a few clouds. Great for outdoor activities."

    # Additional moderate conditions
    elif 10 <= temperature < 15 and humidity < 70:
        rating = "Moderate: Cool and Dry"
        message = "Cool temperature with low humidity. Wear a light jacket."
    elif wind_speed > 30 and wind_direction in range(0, 90):
        rating = "Moderate: Windy from the Northeast"
        message = "Windy from the northeast. Secure loose items."
    elif wind_speed > 30 and wind_direction in range(90, 180):
        rating = "Moderate: Windy from the Southeast"
        message = "Windy from the southeast. Secure loose items."
    elif wind_speed > 30 and wind_direction in range(180, 270):
        rating = "Moderate: Windy from the Southwest"
        message = "Windy from the southwest. Secure loose items."
    elif wind_speed > 30 and wind_direction in range(270, 360):
        rating = "Moderate: Windy from the Northwest"
        message = "Windy from the northwest. Secure loose items."
    elif clouds > 60 and pressure < 980:
        rating = "Moderate: Cloudy and Low Pressure"
        message = "Cloudy with low pressure. Potential for rain."
        # High elevation with low pressure and low temperature
    elif elevation > 2000 and pressure < 900 and temperature < 5:
        rating = "Caution: High Elevation Cold"
        message = "High elevation with cold temperatures and low pressure. Risk of altitude sickness and hypothermia."

    # High humidity with low temperature (possible fog/mist)
    elif humidity > 90 and temperature < 10 and clouds > 70:
        rating = "Caution: Foggy Conditions"
        message = "High humidity with low temperature. Expect fog or mist. Reduced visibility."

    # Low humidity with strong winds (risk of fire)
    elif humidity < 20 and wind_speed > 30:
        rating = "Caution: Fire Hazard"
        message = "Low humidity with strong winds. High fire risk. Avoid open flames."

    # Very low light intensity during daytime (indicates thick cloud cover or eclipse)
    elif light_intensity < 1000 and clouds > 90:
        rating = "Caution: Very Low Light"
        message = "Very low light during daytime. Thick cloud cover or possible eclipse."

    # High heat index with no cloud cover (direct sunlight exposure)
    elif heat_index > 40 and clouds < 10:
        rating = "Caution: Extreme Heat Exposure"
        message = "High heat index with direct sunlight. High risk of heatstroke. Seek shade and stay hydrated."

    # High UV intensity with high elevation (risk of severe sunburn at high altitude)
    elif uv_intensity > 7 and elevation > 2500:
        rating = "Caution: High UV at Elevation"
        message = "High UV intensity at high elevation. Increased risk of sunburn. Use strong sunscreen."

    # High air quality index in a usually clean area (indicates pollution event)
    elif air_quality > 100 and pressure < 980 and usually_clean_area:
        rating = "Caution: Unusual Air Quality Event"
        message = "Poor air quality detected in a normally clean area. Possible pollution event or wildfire smoke."

    # Sudden drop in temperature with high wind speed (indicates cold front)
    elif temperature_drop > 10 and wind_speed > 40:
        rating = "Caution: Cold Front"
        message = "Sudden temperature drop with strong winds. Possible cold front. Dress warmly and prepare for rapid weather changes."

    # Low atmospheric pressure with high clouds and temperature (possible tropical storm)
    elif pressure < 940 and clouds > 90 and temperature > 25:
        rating = "Leave Immediately"
        message = "Very low pressure with high clouds and temperature. Possible tropical storm. Evacuate the area."

    # Low cloud cover with low temperature and high pressure (frost risk)
    elif clouds < 10 and temperature < 5 and pressure > 1020:
        rating = "Caution: Frost Risk"
        message = "Clear skies with low temperature and high pressure. Frost likely overnight."

    # High winds with clear skies (potential for wildfires)
    elif wind_speed > 50 and clouds < 10 and humidity < 20:
        rating = "Caution: Wildfire Risk"
        message = "High winds with clear skies and low humidity. High wildfire risk. Avoid using fire."

    # High pressure with rapidly falling temperature (possible cold snap)
    elif pressure > 1030 and temperature_falling > 15:
        rating = "Caution: Cold Snap"
        message = "High pressure with rapidly falling temperature. Cold snap likely. Prepare for sudden cold."

    # High wind speed and high elevation (increased wind chill)
    elif wind_speed > 40 and elevation > 1500:
        rating = "Caution: High Wind Chill"
        message = "Strong winds at high elevation. Increased wind chill effect. Dress warmly."

    # High humidity with very low temperature (ice formation risk)
    elif humidity > 90 and temperature < 0:
        rating = "Caution: Ice Formation"
        message = "High humidity with freezing temperatures. Risk of ice formation on surfaces. Drive carefully."

    # Low air quality with high temperature (risk of ozone pollution)
    elif air_quality > 150 and temperature > 30:
        rating = "Caution: Ozone Pollution"
        message = "Poor air quality combined with high temperature. Risk of ozone pollution. Limit outdoor activities."

    # High UV intensity with low humidity (increased risk of skin and eye damage)
    elif uv_intensity > 8 and humidity < 30:
        rating = "Caution: High UV and Dry Air"
        message = "High UV intensity with low humidity. Increased risk of skin and eye damage. Wear protective gear."

    # Low light intensity with high temperature (potential heat haze)
    elif light_intensity < 10000 and temperature > 35:
        rating = "Caution: Heat Haze"
        message = "Low light intensity combined with high temperature. Potential for heat haze. Reduced visibility."

    # High cloud cover with low pressure and falling temperature (indicates a storm is approaching)
    elif clouds > 90 and pressure < 960 and temperature_falling > 5:
        rating = "Caution: Approaching Storm"
        message = "High cloud cover with low pressure and falling temperature. A storm may be approaching. Take precautions."
    # High light intensity with low humidity (risk of dehydration)
    elif light_intensity > 90000 and humidity < 20:
        rating = "Caution: High Light and Dry Air"
        message = "Very bright conditions with low humidity. Risk of dehydration. Stay hydrated and protect your eyes."

    # Sudden rise in temperature with low pressure (possible heatwave)
    elif temperature_rise > 10 and pressure < 950:
        rating = "Caution: Heatwave"
        message = "Rapid temperature increase with low pressure. Possible heatwave conditions. Avoid strenuous outdoor activities."

    # Low temperature with very high pressure (clear but cold conditions)
    elif temperature < 0 and pressure > 1040:
        rating = "Caution: Cold and Clear"
        message = "Very cold temperature with high pressure. Clear skies but dress warmly."

    # High UV index with low cloud cover at midday (risk of severe sunburn)
    elif uv_intensity > 9 and clouds < 10 and "12:00:00" <= current_time <= "14:00:00":
        rating = "Caution: Midday Sun"
        message = "Extreme UV index with low cloud cover at midday. High risk of sunburn. Minimize sun exposure."

    # High wind speed with low cloud cover at night (risk of wind chill)
    elif wind_speed > 50 and clouds < 20 and "18:00:00" <= current_time <= "06:00:00":
        rating = "Caution: Night Wind Chill"
        message = "Strong winds with clear skies at night. Increased risk of wind chill. Dress warmly."

    # High humidity with moderate temperature (muggy and uncomfortable)
    elif humidity > 85 and 20 <= temperature <= 25:
        rating = "Moderate: Muggy"
        message = "High humidity with moderate temperature. Muggy and potentially uncomfortable. Stay hydrated."

    # Low temperature with high humidity (risk of freezing rain or sleet)
    elif temperature in range(-5, 1) and humidity > 85:
        rating = "Caution: Freezing Rain Risk"
        message = "Low temperature with high humidity. Risk of freezing rain or sleet. Travel with caution."

    # High atmospheric pressure with rapidly clearing skies (cold front passing)
    elif pressure > 1025 and clouds > 80 and clouds < 20:
        rating = "Caution: Cold Front Passed"
        message = "Rapidly clearing skies with high pressure. Cold front may have passed. Temperature could drop."

    # High wind speed combined with rain (risk of wind-driven rain)
    elif wind_speed > 50 and humidity > 90 and clouds > 80:
        rating = "Caution: Wind-Driven Rain"
        message = "Strong winds with high humidity and heavy clouds. Wind-driven rain likely. Seek shelter."

    # High wind speed combined with high temperature (dry, hot winds)
    elif wind_speed > 40 and temperature > 35 and humidity < 30:
        rating = "Caution: Hot Dry Winds"
        message = "Strong, hot winds with low humidity. Increased risk of dehydration and heat-related illnesses."

    # High cloud cover with moderate temperature (overcast and mild)
    elif clouds > 90 and 15 <= temperature <= 20:
        rating = "Moderate: Overcast"
        message = "High cloud cover with mild temperatures. Overcast but comfortable for outdoor activities."

    # Temperature close to zero with high humidity at dawn (frost risk)
    elif temperature in range(-1, 2) and humidity > 90 and "04:00:00" <= current_time <= "07:00:00":
        rating = "Caution: Dawn Frost Risk"
        message = "Temperature near freezing with high humidity at dawn. Frost likely. Be cautious on roads and paths."

    # Very high atmospheric pressure with calm winds and clear skies (anticyclone)
    elif pressure > 1040 and wind_speed < 10 and clouds < 10:
        rating = "Moderate: Anticyclone"
        message = "Very high pressure with calm winds and clear skies. Stable, dry conditions but could be chilly."

    # Sudden pressure drop with increasing cloud cover (indicating an approaching storm)
    elif pressure_falling > 15 and clouds_rising > 50:
        rating = "Caution: Storm Approaching"
        message = "Rapid pressure drop with increasing cloud cover. A storm is likely approaching. Take precautions."

    # Light rain with moderate winds (drizzle with breezy conditions)
    elif humidity > 85 and clouds > 70 and 10 <= wind_speed <= 30 and temperature > 10:
        rating = "Moderate: Breezy Drizzle"
        message = "Light rain with moderate winds. Drizzly and breezy. Wear a light raincoat."

    # High wind speed combined with snow (blizzard conditions)
    elif wind_speed > 40 and temperature < 0 and clouds > 90:
        rating = "Leave Immediately"
        message = "High winds with snow. Blizzard conditions. Seek immediate shelter."

    # Very high light intensity with low wind speed (glare risk)
    elif light_intensity > 100000 and wind_speed < 5:
        rating = "Caution: Glare Risk"
        message = "Very high light intensity with calm winds. Risk of glare, especially on water or snow. Wear sunglasses."

    # Low temperature combined with very high light intensity (risk of snow blindness)
    elif temperature < 0 and light_intensity > 80000 and snow_coverage > 50:
        rating = "Caution: Snow Blindness Risk"
        message = "Very bright conditions with cold temperatures and snow coverage. Risk of snow blindness. Wear protective eyewear."
    # Low light intensity with high cloud cover and high humidity (risk of mist or light drizzle)
    elif light_intensity < 5000 and clouds > 80 and humidity > 85:
        rating = "Moderate: Mist or Drizzle"
        message = "Low light with heavy clouds and high humidity. Expect mist or light drizzle. Light rain gear recommended."

    # High elevation with high UV intensity and low temperature (risk of sunburn and cold stress)
    elif elevation > 2000 and uv_intensity > 7 and temperature < 10:
        rating = "Caution: Sunburn and Cold Stress"
        message = "High elevation with strong UV and cold temperature. Risk of sunburn and cold stress. Wear sunscreen and dress warmly."

    # Low atmospheric pressure with high humidity (potential for heavy rainfall or thunderstorms)
    elif pressure < 950 and humidity > 90:
        rating = "Caution: Heavy Rain or Thunderstorm Risk"
        message = "Low pressure with high humidity. Potential for heavy rainfall or thunderstorms. Stay prepared."

    # Clear skies with very low temperature and calm winds (extreme frost risk)
    elif clouds < 5 and temperature < -10 and wind_speed < 5:
        rating = "Caution: Extreme Frost"
        message = "Clear skies with very low temperature and calm winds. Extreme frost likely. Dress warmly and avoid prolonged exposure."

    # Sudden rise in humidity with falling pressure (indicates storm development)
    elif humidity_rising > 20 and pressure_falling > 10:
        rating = "Caution: Developing Storm"
        message = "Rapid increase in humidity with falling pressure. Storm development likely. Take precautions."

    # High wind speed with shifting wind direction (indicates unstable weather)
    elif wind_speed > 40 and wind_direction_change > 90:
        rating = "Caution: Unstable Weather"
        message = "High winds with rapidly changing direction. Unstable weather likely. Stay alert."

    # High UV intensity with light snow cover (risk of snow glare)
    elif uv_intensity > 5 and snow_coverage > 20:
        rating = "Caution: Snow Glare"
        message = "High UV intensity with snow cover. Increased risk of snow glare. Wear protective eyewear."

    # Very high humidity with moderate temperature and low pressure (tropical climate conditions)
    elif humidity > 95 and 25 <= temperature <= 30 and pressure < 970:
        rating = "Caution: Tropical Conditions"
        message = "Very high humidity with warm temperature and low pressure. Tropical-like conditions. Stay cool and hydrated."

    # High wind speed with low cloud cover during sunrise/sunset (wind chill and glare risk)
    elif wind_speed > 30 and clouds < 10 and ("05:00:00" <= current_time <= "07:00:00" or "18:00:00" <= current_time <= "20:00:00"):
        rating = "Caution: Wind Chill and Glare"
        message = "Strong winds with clear skies during sunrise/sunset. Risk of wind chill and glare. Dress warmly and wear sunglasses."

    # High cloud cover with high humidity and low wind speed (risk of stagnant air and poor air quality)
    elif clouds > 85 and humidity > 90 and wind_speed < 5:
        rating = "Caution: Stagnant Air"
        message = "High cloud cover with high humidity and calm winds. Risk of stagnant air and poor air quality. Limit outdoor activities."

    # Very low pressure with clear skies (potential for rapidly changing weather)
    elif pressure < 930 and clouds < 10:
        rating = "Caution: Unstable Atmospheric Conditions"
        message = "Very low pressure with clear skies. Rapid weather changes possible. Stay alert."

    # High temperature with calm winds and clear skies (risk of heat exhaustion)
    elif temperature > 35 and wind_speed < 5 and clouds < 10:
        rating = "Caution: Heat Exhaustion Risk"
        message = "Very high temperature with calm winds and clear skies. High risk of heat exhaustion. Stay hydrated and avoid strenuous activities."

    # Low temperature with heavy snow cover and high humidity (risk of hypothermia)
    elif temperature < 0 and snow_coverage > 50 and humidity > 85:
        rating = "Caution: Hypothermia Risk"
        message = "Very cold with heavy snow cover and high humidity. Risk of hypothermia. Dress warmly and limit time outdoors."

    # High pressure with high cloud cover and moderate temperature (stable but overcast conditions)
    elif pressure > 1020 and clouds > 70 and 15 <= temperature <= 25:
        rating = "Moderate: Overcast and Stable"
        message = "High pressure with significant cloud cover and moderate temperature. Stable but overcast conditions. Suitable for most activities."

    # Low atmospheric pressure with very high light intensity (indicates potential for intense weather)
    elif pressure < 940 and light_intensity > 100000:
        rating = "Caution: Intense Weather Potential"
        message = "Very low pressure with intense light. Potential for severe weather events. Monitor conditions closely."

    # Very low wind speed with high humidity and moderate temperature (risk of fog formation)
    elif wind_speed < 5 and humidity > 95 and 10 <= temperature <= 20:
        rating = "Caution: Fog Formation"
        message = "Calm winds with high humidity and moderate temperature. High risk of fog formation. Reduced visibility likely."

    # High UV intensity with low ozone levels (increased risk of UV exposure)
    elif uv_intensity > 9 and ozone_level < 250:
        rating = "Caution: UV Exposure"
        message = "High UV intensity with low ozone levels. Increased risk of UV exposure. Use strong sunscreen and protective clothing."

    # High cloud cover with low light intensity and temperature drop (risk of snow or sleet)
    elif clouds > 90 and light_intensity < 5000 and temperature < 5:
        rating = "Caution: Snow or Sleet Risk"
        message = "Heavy cloud cover with low light and falling temperature. High chance of snow or sleet. Dress appropriately."

    # High wind speed with low atmospheric pressure and high humidity (risk of severe thunderstorms)
    elif wind_speed > 60 and pressure < 950 and humidity > 85:
        rating = "Leave Immediately"
        message = "Strong winds with low pressure and high humidity. Severe thunderstorms likely. Seek immediate shelter."
    # Sudden temperature drop with clear skies (risk of rapid frost formation)
    elif temperature_drop > 10 and clouds < 5 and humidity > 80:
        rating = "Caution: Rapid Frost Formation"
        message = "Sudden temperature drop with clear skies and high humidity. Rapid frost formation likely. Be cautious on roads."

    # High elevation with high wind speed (risk of wind exposure and altitude sickness)
    elif elevation > 2500 and wind_speed > 50:
        rating = "Caution: High Wind at Elevation"
        message = "High elevation with strong winds. Increased risk of wind exposure and altitude sickness. Limit outdoor activities."

    # High wind speed with sudden temperature rise (risk of wildfires in dry conditions)
    elif wind_speed > 40 and temperature_rise > 10 and humidity < 20:
        rating = "Leave Immediately"
        message = "Strong winds with sudden temperature rise in dry conditions. High risk of wildfires. Evacuate the area if necessary."

    # Very low temperature with moderate wind speed (risk of frostbite)
    elif temperature < -15 and wind_speed in range(20, 40):
        rating = "Caution: Frostbite Risk"
        message = "Very low temperature with moderate winds. Increased risk of frostbite. Wear appropriate winter gear."

    # Low humidity with high temperature and clear skies (risk of heat stroke)
    elif humidity < 15 and temperature > 40 and clouds < 5:
        rating = "Leave Immediately"
        message = "Extremely low humidity with high temperature and clear skies. Severe risk of heat stroke. Avoid outdoor activities."

    # Sudden increase in cloud cover with falling pressure (indicates incoming storm or front)
    elif clouds_rising > 50 and pressure_falling > 10:
        rating = "Caution: Incoming Storm"
        message = "Rapid increase in cloud cover with falling pressure. An incoming storm or front is likely. Prepare accordingly."

    # Low light intensity with heavy snow cover and low wind speed (risk of ground blizzard)
    elif light_intensity < 5000 and snow_coverage > 80 and wind_speed < 5:
        rating = "Caution: Ground Blizzard Risk"
        message = "Low light intensity with heavy snow cover and calm winds. Ground blizzard conditions possible. Stay indoors."

    # High wind speed with very low humidity (risk of dust storms in arid regions)
    elif wind_speed > 50 and humidity < 10 and temperature > 30:
        rating = "Leave Immediately"
        message = "Strong winds with very low humidity in hot conditions. High risk of dust storms. Evacuate or take shelter immediately."

    # High UV intensity with low cloud cover and high ozone levels (risk of ozone-induced respiratory issues)
    elif uv_intensity > 8 and clouds < 10 and ozone_level > 350:
        rating = "Caution: Ozone Risk"
        message = "High UV intensity with low cloud cover and elevated ozone levels. Increased risk of respiratory issues. Minimize outdoor exposure."

    # High humidity with low temperature and low wind speed (risk of freezing fog)
    elif humidity > 95 and temperature < 0 and wind_speed < 5:
        rating = "Caution: Freezing Fog"
        message = "Very high humidity with low temperature and calm winds. Freezing fog likely. Drive with caution and limit exposure."

    # High atmospheric pressure with very low wind speed and high light intensity (risk of thermal inversion)
    elif pressure > 1030 and wind_speed < 5 and light_intensity > 80000:
        rating = "Caution: Thermal Inversion"
        message = "High pressure with calm winds and strong sunlight. Risk of thermal inversion, which can trap pollutants. Air quality may deteriorate."

    # Sudden temperature rise with low pressure and high wind speed (indicates a possible incoming hurricane or severe storm in coastal areas)
    elif temperature_rise > 10 and pressure < 930 and wind_speed > 70 and elevation < 100:
        rating = "Leave Immediately"
        message = "Rapid temperature rise with very low pressure and strong winds in a coastal area. Possible hurricane or severe storm. Evacuate immediately."

    # Clear skies with very low temperature and high elevation (risk of altitude-related cold stress)
    elif clouds < 5 and temperature < -10 and elevation > 3000:
        rating = "Caution: Altitude Cold Stress"
        message = "Clear skies with very low temperatures at high elevation. Risk of cold stress and altitude sickness. Dress warmly and limit exposure."

    # High humidity with heavy cloud cover during sunset (risk of rapidly dropping visibility)
    elif humidity > 90 and clouds > 85 and "18:00:00" <= current_time <= "20:00:00":
        rating = "Caution: Rapid Visibility Drop"
        message = "High humidity with heavy clouds during sunset. Visibility may drop rapidly. Drive cautiously and use lights."

    # Low humidity with moderate temperature and high elevation (risk of dehydration at altitude)
    elif humidity < 20 and temperature in range(15, 25) and elevation > 2500:
        rating = "Caution: Dehydration Risk at Altitude"
        message = "Low humidity with moderate temperatures at high elevation. Increased risk of dehydration. Stay hydrated."

    # High light intensity with calm winds and heavy snow cover (risk of snow blindness in clear, calm conditions)
    elif light_intensity > 100000 and wind_speed < 5 and snow_coverage > 70:
        rating = "Caution: Snow Blindness Risk"
        message = "Very bright conditions with calm winds and heavy snow cover. Risk of snow blindness. Wear protective eyewear."

    # Low light intensity with moderate wind speed and low temperature (risk of black ice formation)
    elif light_intensity < 5000 and wind_speed in range(10, 30) and temperature in range(-5, 3):
        rating = "Caution: Black Ice Risk"
        message = "Low light intensity with moderate winds and near-freezing temperatures. Black ice formation likely. Drive cautiously."

    # Sudden drop in temperature with heavy rain and high wind speed (risk of flash freeze)
    elif temperature_drop > 10 and humidity > 90 and wind_speed > 40 and temperature in range(1, 5):
        rating = "Caution: Flash Freeze Risk"
        message = "Sudden drop in temperature with heavy rain and strong winds. Risk of flash freeze on surfaces. Avoid travel if possible."

    # High atmospheric pressure with high wind speed (risk of wind damage despite stable pressure)
    elif pressure > 1030 and wind_speed > 70:
        rating = "Caution: Wind Damage Risk"
        message = "High pressure with very strong winds. Risk of wind damage despite stable pressure. Secure outdoor objects and stay indoors."

    # High wind speed with very high light intensity and moderate temperature (risk of wildfire spread in dry regions)
    elif wind_speed > 50 and light_intensity > 90000 and temperature in range(20, 30) and humidity < 20:
        rating = "Leave Immediately"
        message = "Strong winds with intense sunlight in moderate temperatures. High risk of wildfire spread in dry regions. Evacuate if necessary."

    # High UV intensity with moderate humidity and moderate temperature (risk of heat cramps during physical activity)
    elif uv_intensity > 8 and humidity in range(50, 70) and temperature in range(25, 30):
        rating = "Caution: Heat Cramp Risk"
        message = "High UV intensity with moderate humidity and temperature. Increased risk of heat cramps during physical activity. Stay hydrated and take breaks."

    # Sudden rise in wind speed with dropping temperature and low pressure (indicates a possible cold front)
    elif wind_speed_rising > 20 and temperature_falling > 5 and pressure < 960:
        rating = "Caution: Cold Front Approaching"
        message = "Rapid increase in wind speed with falling temperature and low pressure. Possible cold front. Prepare for colder conditions."

    # High light intensity with very low humidity and clear skies (risk of dehydration and sunstroke)
    elif light_intensity > 100000 and humidity < 10 and clouds < 5:
        rating = "Leave Immediately"
        message = "Intense sunlight with very low humidity and clear skies. Severe risk of dehydration and sunstroke. Avoid outdoor activities."

    # Heavy rain with low wind speed and low pressure (risk of flooding)
    elif humidity > 95 and clouds > 90 and wind_speed < 10 and pressure < 950:
        rating = "Leave Immediately"
        message = "Heavy rain with calm winds and low pressure. High risk of flooding. Evacuate or seek higher ground."

    return rating, message

# Example usage:
rating, message = evaluate_advance_conditions("09:39:07", 32.46, 63.04, 0.0, 41.23, 936, 678.31, 39.2, 1, 8.15, 251, 100)
print(f"Rating: {rating}, Message: {message}")
