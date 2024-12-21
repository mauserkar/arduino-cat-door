ampy.exe -p COM4 -b 115200 -d 1 rm .env
ampy.exe -p COM4 -b 115200 -d 1 rmdir /cats_door
ampy.exe -p COM4 -b 115200 -d 1 put .\.env .env
ampy.exe -p COM4 -b 115200 -d 1 put .\cats_door /cats_door
ampy.exe -p COM4 -b 115200 -d 1 put .\boot.py boot.py
ampy.exe -p COM4 -b 115200 -d 1 ls /cats_door
ampy.exe -p COM4 -b 115200 -d 1 ls /
ampy.exe -p COM4 -b 115200 -d 1 reset