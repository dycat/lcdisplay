from lcd import LCD
from datetime import datetime


#TODO turn on or off light accroding to time
lcd = LCD()
# lcd.BACKGROUND_LIGHT = 0
while True:
    now = datetime.now()
    if now.hour >= 22 or now.hour < 8:
        lcd.BACKGROUND_LIGHT = 0
        # lcd.turn_light()
    else:
        lcd.BACKGROUND_LIGHT = 1
    now_string = now.strftime("%b %d %H:%M")
    lcd.print_lcd(0, 0, now_string)
