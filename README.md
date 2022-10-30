# Micropython button debouncer
Micropython implementation of a debounced button. Tested to work well with the Raspberry Pi Pico.

Since this Button implementation is interrupt-based there is no need to periodically poll/query the status of the button.

Example code:
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