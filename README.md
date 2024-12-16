# Cat's door Micropython project

# Hardware requirements
- esp32 arduino
- 1 servo 15KG
- 2 movement sensor

# Software requirements
- ampy: to manage the code inside the arduino.
- esptool: to flash arduito with the micropthon proyect


# ampy
* windows: port COM4
* unix: port /dev/ttyUSB
```bash
ampy -p /dev/ttyUSB -b 115200 -d 1 ls
ampy -p /dev/ttyUSB -b 115200 -d 1 put source_file.py dest_file.py
ampy -p /dev/ttyUSB -b 115200 -d 1 run dest_file.py
```