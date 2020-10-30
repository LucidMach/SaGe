import serial
while True:
# with serial.Serial("COM4",9600) as ser:
    # ser.write(b"H")
    a = input("Enter: ")
    se = serial.Serial("COM5",9600)
    if a == "H":
        se.write(b"H")
    elif a == "L":
        se.write(b"L")
    se.close()