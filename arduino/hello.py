import serial


arduino = serial.Serial(port='/dev/ttyACM0', timeout=.1)

d = 0
while d == 0:
    u = arduino.readline().decode('utf-8')
    if len(u) > 0:  # check if not empty string
        d = int(u)
        print(d)
