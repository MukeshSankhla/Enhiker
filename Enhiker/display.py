import pygame
import time

pygame.init()

# Set the display dimensions
screen_width = 240
screen_height = 320
screen = pygame.display.set_mode((screen_width, screen_height))

fontSize = 24
iconWidth = 24
iconHeight = 24

# Load fonts and icons for display
font = pygame.font.Font(None, fontSize)
messageFont = pygame.font.Font(None, 20)

SatelliteIcon = pygame.image.load("Icons/satellite.png")
SatelliteIcon = pygame.transform.scale(SatelliteIcon, (18, 18))

WifiIcon = pygame.image.load("Icons/wifi.png")
WifiIcon = pygame.transform.scale(WifiIcon, (18, 18))

LoadingIcon = pygame.image.load("Icons/loading.png")
LoadingIcon = pygame.transform.scale(LoadingIcon, (140, 140))

TempIcon = pygame.image.load("Icons/temperature.png")
TempIcon = pygame.transform.scale(TempIcon, (iconWidth, iconHeight))

HumIcon = pygame.image.load("Icons/humidity.png")
HumIcon = pygame.transform.scale(HumIcon, (iconWidth, iconHeight))

HeatIcon = pygame.image.load("Icons/heat.png")
HeatIcon = pygame.transform.scale(HeatIcon, (iconWidth, iconHeight))

LightIntIcon = pygame.image.load("Icons/light.png")
LightIntIcon = pygame.transform.scale(LightIntIcon, (iconWidth, iconHeight))

UVIcon = pygame.image.load("Icons/uv.png")
UVIcon = pygame.transform.scale(UVIcon, (iconWidth, iconHeight))

AltitudeIcon = pygame.image.load("Icons/altitude.png")
AltitudeIcon = pygame.transform.scale(AltitudeIcon, (iconWidth, iconHeight))

PressureIcon = pygame.image.load("Icons/pressure.png")
PressureIcon = pygame.transform.scale(PressureIcon, (iconWidth, iconHeight))

LocationIcon = pygame.image.load("Icons/location.png")
LocationIcon = pygame.transform.scale(LocationIcon, (iconWidth, iconHeight))

WindIcon = pygame.image.load("Icons/wind.png")
WindIcon = pygame.transform.scale(WindIcon, (iconWidth, iconHeight))

AirIcon = pygame.image.load("Icons/air.png")
AirIcon = pygame.transform.scale(AirIcon, (iconWidth, iconHeight))

CloudsIcon = pygame.image.load("Icons/clouds.png")
CloudsIcon = pygame.transform.scale(CloudsIcon, (iconWidth, iconHeight))

SunriseIcon = pygame.image.load("Icons/sunrise.png")
SunriseIcon = pygame.transform.scale(SunriseIcon, (iconWidth, iconHeight))

SunsetIcon = pygame.image.load("Icons/sunset.png")
SunsetIcon = pygame.transform.scale(SunsetIcon, (iconWidth, iconHeight))

# Function to display a loading screen while searching for satellites
def display_loading_screen():
    frame_surface = pygame.Surface((screen_width, screen_height))
    frame_surface.fill((0, 0, 0))
    screen.blit(frame_surface, (0, 0))
    
    # Display loading icon
    screen.blit(LoadingIcon, (50, 90))
    pygame.display.update()

    return None

def display_data(wifi_connected, current_date, current_time, num_satellites, temperature, humidity, heat_index, light_intensity, uv_intensity, pressure, elevation, latitude, longitude, rating, message, air_quality, wind_speed, wind_direction, sunrise, sunset, clouds):
    # Update the Pygame display with sensor data
    frame_surface = pygame.Surface((screen_width, screen_height))
    frame_surface.fill((0, 0, 0))
    screen.blit(frame_surface, (0, 0))

    # Display date and time
    date_time_str = f"{current_date} {current_time}"
    text_surface = font.render(date_time_str, True, (255, 255, 255))
    screen.blit(text_surface, (50, 8))

    # Display satellite status
    screen.blit(SatelliteIcon, (5, 5))
    text_surface = font.render(f"{num_satellites}", True, (255, 255, 255))
    screen.blit(text_surface, (27, 8))

    # Display Wi-Fi status
    if wifi_connected:
        screen.blit(WifiIcon, (215, 5))

    pygame.draw.line(screen, (255, 255, 255), (0, 30), (screen_width, 30), 1)

    # Display environmental data
    screen.blit(TempIcon, (5, 35))
    text_surface = font.render(f"{temperature} 'C", True, (255, 255, 255))
    screen.blit(text_surface, (30, 40))

    screen.blit(HumIcon, (115, 35))
    text_surface = font.render(f"{humidity} %", True, (255, 255, 255))
    screen.blit(text_surface, (140, 40))

    screen.blit(LightIntIcon, (5, 65))
    text_surface = font.render(f"{light_intensity} lx", True, (255, 255, 255))
    screen.blit(text_surface, (30, 70))

    screen.blit(UVIcon, (115, 65))
    text_surface = font.render(f"{uv_intensity} mw/cm²", True, (255, 255, 255))
    screen.blit(text_surface, (140, 70))

    screen.blit(PressureIcon, (5, 95))
    text_surface = font.render(f"{int(pressure)} hPa", True, (255, 255, 255))
    screen.blit(text_surface, (30, 100))

    screen.blit(AltitudeIcon, (115, 95))
    text_surface = font.render(f"{elevation} m", True, (255, 255, 255))
    screen.blit(text_surface, (140, 100))

    screen.blit(LocationIcon, (5, 125))
    text_surface = font.render(f"{latitude}, {longitude}", True, (255, 255, 255))
    screen.blit(text_surface, (30, 130))

    if wifi_connected:
        screen.blit(HeatIcon, (5, 150))
        text_surface = font.render(f"{heat_index} 'C", True, (255, 255, 255))
        screen.blit(text_surface, (30, 155))

        screen.blit(AirIcon, (115, 150))
        text_surface = font.render(f"{air_quality}", True, (255, 255, 255))
        screen.blit(text_surface, (140, 155))

        screen.blit(CloudsIcon, (5, 175))
        text_surface = font.render(f"{clouds} %", True, (255, 255, 255))
        screen.blit(text_surface, (30, 180))

        screen.blit(WindIcon, (115, 175))
        text_surface = font.render(f"{wind_speed}, {wind_direction}", True, (255, 255, 255))
        screen.blit(text_surface, (140, 180))

        screen.blit(SunriseIcon, (5, 200))
        text_surface = font.render(f"{sunrise}", True, (255, 255, 255))
        screen.blit(text_surface, (30, 205))

        screen.blit(SunsetIcon, (5, 225))
        text_surface = font.render(f"{sunset}", True, (255, 255, 255))
        screen.blit(text_surface, (30, 230))

    pygame.draw.line(screen, (255, 255, 255), (0, 250), (screen_width, 250), 1)

    # Display rating
    text_surface = font.render(f"{rating}", True, (255, 255, 255))
    screen.blit(text_surface, (0, 255))

    # Display the evaluation message, wrapped for the screen width
    wrapped_lines = [message[i:i + 36] for i in range(0, len(message), 36)]
    y_offset = 270
    for line in wrapped_lines:
        text_surface = messageFont.render(line, True, (255, 255, 255))
        screen.blit(text_surface, (0, y_offset))
        y_offset += messageFont.get_height()

    pygame.display.update()
    return None

# wifi_connected = True
# current_date = "2023-12-25"
# current_time = "17:30:00"
# num_satellites = 15
# temperature = 28.5
# humidity = 65
# heat_index = 32
# light_intensity = 500
# uv_intensity = 3
# pressure = 1010
# elevation = 500
# latitude = 17.57
# longitude = 78.32
# rating = 4
# message = "Weather is pleasant."
# air_quality = "Good"
# wind_speed = 5
# wind_direction = 270
# sunrise = "06:30 AM"
# sunset = "06:30 PM"
# clouds = 20

# while True:
#     display_data(wifi_connected, current_date, current_time, num_satellites, temperature, humidity, heat_index, light_intensity, uv_intensity, pressure, elevation, latitude, longitude, rating, message, air_quality, wind_speed, wind_direction, sunrise, sunset, clouds)