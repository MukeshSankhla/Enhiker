from pinpong.board import Board
from DFRobot_GNSS_I2C import DFRobot_GNSS_I2C, MODE_GPS_BEIDOU_GLONASS
import time
from unihiker import GUI

u_gui = GUI()

MINIMUM_SATELLITES = 3
DELAY_SECONDS = 2

def main():
    Board().begin()
    sensor = DFRobot_GNSS_I2C()
    sensor.set_gnss_mode(MODE_GPS_BEIDOU_GLONASS)
    sensor.set_enable_power()

    spacing = 25
    titleTextSize = 14

    while True:
        num_satellites = sensor.get_num_sta_used()
        
        if num_satellites > MINIMUM_SATELLITES:
            lat_data = sensor.get_lat()
            lon_data = sensor.get_lon()
            
            latitude = f"{lat_data[0]:.6f}° {lat_data[1]}"
            longitude = f"{lon_data[0]:.6f}° {lon_data[1]}"
            
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
            
            u_gui.clear()
            u_gui.draw_text(text=f"Latitude: {latitude}", x=0, y=0*spacing, font_size=titleTextSize, color="#0000FF")
            u_gui.draw_text(text=f"Longitude: {longitude}", x=0, y=2*spacing, font_size=titleTextSize, color="#0000FF")
        else:
            print(f"Searching... Satellites found: {num_satellites}")
            
            u_gui.clear()
            u_gui.draw_text(text="Latitude: Searching...", x=0, y=0*spacing, font_size=titleTextSize, color="#0000FF")
            u_gui.draw_text(text="Longitude: Searching...", x=0, y=2*spacing, font_size=titleTextSize, color="#0000FF")
        
        u_gui.update()
        time.sleep(DELAY_SECONDS)

if __name__ == '__main__':
    main()