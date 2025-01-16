# How to ssh to the Raspberry Pi:
## 1. SSH to the pi:
```
ssh pi@192.168.1.39
```
Use the password:
```
raspberry
```
## 2. In a new terminal window, upload the code with secure copy:
```
scp bootupscript.py pi@192.168.1.39:~/bootupscript.py
```
Use the password:
```
raspberry
```
## 3. In the ssh window, run the code:
```
pi@raspberrypi:~ $ python3 bootupscript.py
```

### Notes
Running this on the pi will give you the ip address:
```
hostname -I
```

# How to setup script to run on boot
Navigate to here: 
```
cd /etc/systemd/system
```
Edit the boot script:
```
sudo nano mybootscript.service
```
Boot script (Remember to save and exit):
```
[Unit]
Description=My Startup Script
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/bootupscript.py
Restart=always
User=pi
WorkingDirectory=/home/pi
StandardOutput=inherit
StandardError=inherit

[Install]
WantedBy=multi-user.target
```
Enable it!
```
sudo systemctl enable mybootscript.service
sudo systemctl start mybootscript.service
sudo systemctl status mybootscript.service
sudo reboot
```
Stop it temporarily
```
sudo systemctl stop mybootscript.service
```
Stop from future reboots:
```
sudo systemctl disable myscript.service
```


# Controlling the pi
## Shutdown
Run this commmand to shutdown:
```
sudo shutdown -h now
```
Shut down after 5 minutes:
```
sudo shutdown -h +5
```
Shut down at a specific time (e.g., 8:30 PM):
```
sudo shutdown -h 20:30
```