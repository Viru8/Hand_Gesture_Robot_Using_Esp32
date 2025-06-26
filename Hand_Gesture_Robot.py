import network
import socket
import machine
import time

# WiFi credentials
ssid = "VIRU"
password = "Virendra"

# Motor pins
in1 = machine.Pin(0, machine.Pin.OUT)
in2 = machine.Pin(4, machine.Pin.OUT)
in3 = machine.Pin(2, machine.Pin.OUT)
in4 = machine.Pin(15, machine.Pin.OUT)

# Speed control (not PWM used here as original code had it commented)
Left_speed = 50
Right_speed = 50

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Connecting to WiFi...")
while not wlan.isconnected():
    time.sleep(1)
    print(".", end="")

print("\nConnected to WiFi. IP:", wlan.ifconfig()[0])

# Set up UDP socket
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(('', 12345))
udp.setblocking(False)

# Function to parse CSV-like data (e.g., "f,50")
def parse_data(data_str):
    parts = data_str.strip().split(',')
    return parts

def forward():
    in1.on(); in2.off()
    in3.on(); in4.off()

def backward():
    in1.off(); in2.on()
    in3.off(); in4.on()

def left():
    in1.on(); in2.off()
    in3.off(); in4.on()

def right():
    in1.off(); in2.on()
    in3.on(); in4.off()

def stop():
    in1.off(); in2.off()
    in3.off(); in4.off()

while True:
    try:
        data, addr = udp.recvfrom(1024)
        msg = data.decode()
        print("Received:", msg)
        fields = parse_data(msg)

        command = fields[0]
        if len(fields) > 1:
            speed = int(fields[1])
            Left_speed = speed
            Right_speed = speed

        if command == "f":
            forward()
            print("Forward")
        elif command == "b":
            backward()
            print("Backward")
        elif command == "l":
            left()
            print("Left")
        elif command == "r":
            right()
            print("Right")
        elif command == "s":
            stop()
            print("Stop")

    except OSError:
        pass  # No data received, non-blocking mode
    time.sleep(0.01)

