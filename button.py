from machine import Pin, Timer
from utime import ticks_ms, ticks_diff

class Button:

    def debounce_done(self, timer: Timer):
        if self.pin.value() == 1: self.rising()
        else: self.falling()
        self.pin.irq(handler=self.debounce)  #Reenable interupt after actions are complete
        
    def falling(self):
        self.t_fall = ticks_ms() #Remember time when button was pressed down
        
    def rising(self):
        if self.t_fall == -1: #Got a rising button before a falling one. This is likely due to a bounce -> ignore
            return
        if ticks_diff(ticks_ms(), self.t_fall) < self.long_press_duration_ms:
            self.callback()
        self.t_fall = -1

    def debounce(self, p: Pin):
        self.pin.irq(handler=None, trigger=Pin.IRQ_FALLING) # Disable interrupt, while we are waiting for the button to stop bouncing
        self.debounce_timer.init(mode=Timer.ONE_SHOT, period=self.debounce_time_ms, callback=self.debounce_done)
        if self.long_press_callback is not None:
            self.long_press_timer.init(mode=Timer.ONE_SHOT, period=self.long_press_duration_ms, callback=self.on_long_press)

    def on_long_press(self, timer: Timer):
        if self.pin.value() == 1 or self.long_press_callback is None:
            return
        self.long_press_callback()


    def __init__(self, pin_number: int, callback, long_press_callback=None, debounce_time_ms=50, long_press_duration_ms=2000):
        self.pin = Pin(pin_number, Pin.IN, Pin.PULL_UP)
        self.debounce_timer = Timer()
        self.long_press_timer = Timer()
        self.debounce_time_ms = debounce_time_ms
        self.long_press_duration_ms = long_press_duration_ms
        self.callback = callback
        self.long_press_callback = long_press_callback

        self.pin.irq(handler=self.debounce)
        #self.pin.irq(handler=self.changeHandler, trigger=Pin.IRQ_FALLING)
        self.t_fall = 0