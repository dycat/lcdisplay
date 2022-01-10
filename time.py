from lcd import LCD
from datetime import datetime

lcd = LCD()
lcd.BACKGROUND_LIGHT = 0
while True:
    now = datetime.now().strftime("%b %d %H:%M")
    lcd.print_lcd(0, 0, now)
