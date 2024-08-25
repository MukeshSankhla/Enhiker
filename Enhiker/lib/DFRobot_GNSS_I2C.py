from pinpong.board import I2C
from time import sleep


GNSS_DEVICE_ADDR = 0x20

MODE_GPS = 0x01
MODE_BeiDou = 0x02
MODE_GPS_BeiDou = 0x03
MODE_GLONASS = 0x04
MODE_GPS_GLONASS = 0x05
MODE_BEIDOU_GLONASS = 0x06
MODE_GPS_BEIDOU_GLONASS = 0x07


class DFRobot_GNSS_I2C:

    ENABLE_POWER = 0x00
    DISABLE_POWER = 0x01

    RGB_ON = 0x05
    RGB_OFF = 0x02

    I2C_YEAR_H = 0x00
    I2C_HOUR = 0x04
    I2C_LAT_1 = 0x07
    I2C_LON_1 = 0x0D
    I2C_USE_STAR = 0x13
    I2C_ALT_H = 0x14
    I2C_SOG_H = 0x17
    I2C_COG_H = 0x1A
    I2C_GNSS_MODE = 0x22
    I2C_SLEEP_MODE = 0x23
    I2C_RGB_MODE = 0x24

    def __init__(self, i2c_addr=GNSS_DEVICE_ADDR, bus=0):
        """
        Initialize the DFRobot_GNSS communication
        :param i2c_addr: I2C address
        :param bus: I2C bus number
        """
        self._addr = i2c_addr

        try:
            self._i2c = I2C(bus)
        except Exception as err:
            print(f'Could not initialize i2c! bus: {bus}, error: {err}')

    def _write_reg(self, reg, data) -> None:
        """
        Write data to the I2C register
        :param reg: register address
        :param data: data to write
        :return: None
        """
        if isinstance(data, int):
            data = [data]

        try:
            self._i2c.writeto_mem(self._addr, reg, bytearray(data))
        except Exception as err:
            print(f'Write issue: {err}')

    def _read_reg(self, reg, length) -> bytes:
        """
        Reads data from the I2C register
        :param reg: I2C register address
        :param length: number of bytes to read
        :return: bytes
        """
        try:
            result = self._i2c.readfrom_mem(self._addr, reg, length)
        except Exception as err:
            print(f'Read issue: {err}')
            result = [0, 0]

        return result

    @staticmethod
    def _calculate_latitude_longitude(value: bytes) -> float:
        """
        Calculates the latitude and longitude from bytes to tuple [degree, direction]
        :param value: gnss bytes
        :return: list
        """
        val_dd = value[0]
        val_mm = value[1]
        val_mm_mm = value[2] * 65536 + value[3] * 256 + value[4]
        degree = val_dd + val_mm / 60.0 + val_mm_mm / 100000.0 / 60.0

        return degree

    @staticmethod
    def _optional_calculate_bytes_to_float(value: bytes) -> float:
        """
        Calculates the bytes to float (for altitude, cog and sog)
        :param value: gnss bytes
        :return: float
        """
        return value[0] * 256 + value[1] + value[2] / 100.0

    def set_enable_power(self) -> None:
        """
        Enable gnss power
        :return: None
        """
        self._write_reg(self.I2C_SLEEP_MODE, self.ENABLE_POWER)
        sleep(.1)

    def set_disable_power(self) -> None:
        """
        Disable gnss power
        :return: None
        """
        self._write_reg(self.I2C_SLEEP_MODE, self.DISABLE_POWER)
        sleep(.1)

    def set_rgb_on(self) -> None:
        """
        Turn LED on
        :return: None
        """
        self._write_reg(self.I2C_RGB_MODE, self.RGB_ON)
        sleep(.1)

    def set_rgb_off(self) -> None:
        """
        Turn LED off
        :return: None
        """
        self._write_reg(self.I2C_RGB_MODE, self.RGB_OFF)
        sleep(.1)

    def set_gnss_mode(self, mode: int) -> None:
        """
        Set gnss mode
        - 1 for GPS
        - 2 for BeiDou
        - 3 for GPS + BeiDou
        - 4 for GLONASS
        - 5 for GPS + GLONASS
        - 6 for BeiDou + GLONASS
        - 7 for GPS + BeiDou + GLONASS
        :param mode: number for mode
        :return: None
        """
        if 1 <= mode <= 7:
            self._write_reg(self.I2C_GNSS_MODE, int(mode))
            sleep(.1)

    def get_gnss_mode(self) -> int:
        """
        Get gnss mode (1 till 7)
        :return: number for GNSS mode
        """
        result = self._read_reg(self.I2C_GNSS_MODE, 1)
        return int(result[0])

    def get_num_sta_used(self) -> int:
        """
        Get number of current satellite used
        :return: number of current satellite used
        """
        result = self._read_reg(self.I2C_USE_STAR, 1)
        return int(result[0])

    def get_date(self) -> str:
        """
        Get date and return in format "YYYY-MM-DD"
        :return: str
        """
        year = 2000
        month = 1
        day = 1

        result = self._read_reg(self.I2C_YEAR_H, 4)

        if result != -1:
            year = result[0] * 256 + result[1]
            month = result[2]
            day = result[3]

        return f'{year}-{month:02d}-{day:02d}'

    def get_time(self) -> str:
        """
        Get utc time and return in format "HH:MM:SS"
        :return: str
        """
        hour = 0
        minute = 0
        second = 0

        result = self._read_reg(self.I2C_HOUR, 3)

        if result != -1:
            hour = result[0]
            minute = result[1]
            second = result[2]

        return f'{hour:02d}:{minute:02d}:{second:02d}'

    def get_lat(self) -> list:
        """
        Get latitude and return in format [degree, direction]
        :return: list
        """
        degree = 0.00
        direction = 'S'

        result = self._read_reg(self.I2C_LAT_1, 6)

        if result != -1:
            degree = DFRobot_GNSS_I2C._calculate_latitude_longitude(result)
            direction = chr(result[5])

        return [degree, direction]

    def get_lon(self) -> list:
        """
        Get longitude and return in format [degree, direction]
        :return: list
        """
        degree = 0.00
        direction = 'W'

        result = self._read_reg(self.I2C_LON_1, 6)

        if result != -1:
            degree = DFRobot_GNSS_I2C._calculate_latitude_longitude(result)
            direction = chr(result[5])

        return [degree, direction]

    def get_alt(self) -> float:
        """
        Get altitude over ground in meters
        :return: float
        """
        result = self._read_reg(self.I2C_ALT_H, 3)

        if result != -1:
            high = DFRobot_GNSS_I2C._optional_calculate_bytes_to_float(result)
        else:
            high = 0.0

        return high

    def get_cog(self) -> float:
        """
        Get course over ground in degrees
        :return: float
        """
        result = self._read_reg(self.I2C_COG_H, 3)

        if result != -1:
            cog = DFRobot_GNSS_I2C._optional_calculate_bytes_to_float(result)
        else:
            cog = 0.0

        return cog

    def get_sog(self) -> float:
        """
        Get speed over ground on knot
        :return: float
        """
        result = self._read_reg(self.I2C_SOG_H, 3)

        if result != -1:
            sog = DFRobot_GNSS_I2C._optional_calculate_bytes_to_float(result)
        else:
            sog = 0.0

        return sog
