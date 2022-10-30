# Micropython button debouncer
Micropython implementation of a debounced button. Tested to work well with the Raspberry Pi Pico

Debouce time and long-press duration can be modified using:

```python
b = Button(pin_number, callback, long_press_callback=None, debounce_time_ms=50, long_press_duration_ms=2000)
```