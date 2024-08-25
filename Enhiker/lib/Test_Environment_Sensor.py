import time
from DFRobot_Environmental_Sensor import *

from pinpong.board import Board

Board().begin()

SEN0501 = DFRobot_Environmental_Sensor_I2C(bus=0x01,addr=0x22)

from unihiker import GUI

u_gui=GUI()

spacing=25
titleTextSize=14
valueTextSize=18

u_gui.draw_text(text="temperature:",x=0,y=0*spacing,font_size=titleTextSize, color="#0000FF")
txt_temperature = u_gui.draw_text(text="",x=0,y=1*spacing,font_size=valueTextSize, color="#0000FF")

u_gui.draw_text(text="humidity:",x=0,y=2*spacing,font_size=titleTextSize, color="#0000FF")
txt_humidity = u_gui.draw_text(text="",x=0,y=3*spacing,font_size=valueTextSize, color="#0000FF")

u_gui.draw_text(text="Ultraviolet intensity:",x=0,y=4*spacing,font_size=titleTextSize, color="#0000FF")
txt_uv = u_gui.draw_text(text="",x=0,y=5*spacing,font_size=valueTextSize, color="#0000FF")

u_gui.draw_text(text="LuminousIntensity:",x=0,y=6*spacing,font_size=titleTextSize, color="#0000FF")
txt_light = u_gui.draw_text(text="",x=0,y=7*spacing,font_size=valueTextSize, color="#0000FF")

u_gui.draw_text(text="Atmospheric pressure:",x=0,y=8*spacing,font_size=titleTextSize, color="#0000FF")
txt_pressure = u_gui.draw_text(text="",x=0,y=9*spacing,font_size=valueTextSize, color="#0000FF")

u_gui.draw_text(text="Elevation:",x=0,y=10*spacing,font_size=titleTextSize, color="#0000FF")
txt_elevation = u_gui.draw_text(text="",x=0,y=11*spacing,font_size=valueTextSize, color="#0000FF")


'''
  Atmospheric pressure unit select
'''
HPA                       = 0x01
KPA                       = 0X02

'''
  Temperature unit select
'''
TEMP_C                    = 0X03
TEMP_F                    = 0X04
 
def setup():
  while (SEN0501.begin() == False):
    print("Sensor initialize failed!!")
    time.sleep(1)
  print("Sensor  initialize success!!")
  
def loop():
  ##Obtain sensor data

  txt_temperature.config(text=str(SEN0501.get_temperature(TEMP_C)) + " 'C")
  txt_humidity.config(text=str(SEN0501.get_humidity()) + " %")
  txt_uv.config(text=str(SEN0501.get_ultraviolet_intensity()) + " mw/cm2")
  txt_light.config(text=str(SEN0501.get_luminousintensity()) + " lx")
  txt_pressure.config(text=str(SEN0501.get_atmosphere_pressure(HPA)) + " hpa")
  txt_elevation.config(text=str(SEN0501.get_elevation()) + " m")
  time.sleep(1)

if __name__ == "__main__":
  setup()
  while True:
    loop()
    