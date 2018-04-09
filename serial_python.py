import serial
import time

try:
    
    arduino = serial.Serial('COM3', baudrate=9600, timeout=200.0)
    arduino.setDTR(False)
    time.sleep(1)
    arduino.flushInput()
    arduino.setDTR(True)

except (ImportError, serial.SerialException):
        # No hay módulo serial o placa Arduino disponibles
    print("Conecte la Placa Arduino")
    import io

    class FakeArduino(io.RawIOBase):

        def readline(self):
            time.sleep(0.1)
            return b'null'

    arduino = FakeArduino()

def get_distance():
    line = arduino.readline()
    value = line.decode('ascii', errors='replace')
    return value
