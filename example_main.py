from button import Button

button_pin = 18

def click():
    print("Short click")
    
def long():
    print("Long press")

b = Button(button_pin, click, long)
        

    
