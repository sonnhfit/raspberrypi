how to blink led in raspberrypi

### Setting up the circuit
- Plug the (-)negative terminal of the led light into the GND pin
- Plug the (+)positive lead of the led into the GPIO pin (in this code: **GPIO 17/ Pin 11** ) 

### step 1: install lib 
```
sudo apt-get install python-rpi.gpio python3-rpi.gpio
```

### step 2: clone project

```
https://github.com/sonnhfit/raspberrypi
```
- change dir
```
cd raspberrypi/led
```

### step 3: run code python
```
python blink_led.py
```
