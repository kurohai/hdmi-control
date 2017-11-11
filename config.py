from dicto import dicto
import serial


class BaseConfig(dicto):
    """docstring for BaseConfig"""

    def __init__(self, *args, **kwargs):
        super(BaseConfig, self).__init__(*args, **kwargs)
        self.port = '/dev/ttyUSB0'
        self.baudrate = 9600
        self.bytesize = serial.EIGHTBITS
        self.stopbits = serial.STOPBITS_ONE
        self.parity = serial.PARITY_NONE


class DefaultConfig(BaseConfig):
    """docstring for DefaultConfig"""

    def __init__(self, *args, **kwargs):
        super(DefaultConfig, self).__init__(*args, **kwargs)
