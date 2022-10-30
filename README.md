# Micropython button debouncer
Micropython implementation of a debounced button. Tested to work well with the Raspberry Pi Pico.

### How to use:
1. Connect a button to ground and any pin of the microcontroller
2. Upload `button.py` to the microcontroller
3. Use according to the below example script

### Features:
- Simple and easy to use
- Interrupt/Callback based -> no polling
- Supports short and long presses 
- Software debounce -> no additional hardware required

### Example code:
```python

from button import Button

button_pin = 18

def click():
    print("Short click")
    
def long():
    print("Long press")

b = Button(button_pin, click, long)

```

Debouce time and long-press duration can be modified using:

```python
b = Button(pin_number, callback, long_press_callback=None, debounce_time_ms=50, long_press_duration_ms=2000)
```
