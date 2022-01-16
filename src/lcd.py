import time
import smbus

class LCD:
    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.LCD_ADDR = 0x27
        self.BACKGROUND_LIGHT = 1

        self._send_command(0x33) # Must initialize to 8-line mode at first
        time.sleep(0.005)
        self._send_command(0x32) # Then initialize to 4-line mode
        time.sleep(0.005)
        self._send_command(0x28) # 2 Lines & 5*7 dots
        time.sleep(0.005)
        self._send_command(0x0C) # Enable display without cursor
        time.sleep(0.005)
        self._send_command(0x01) # Clear Screen
        self.bus.write_byte(self.LCD_ADDR ,0x08)

    def turn_light(self):
        if self.BACKGROUND_LIGHT == 1:
            self.bus.write_byte(LCD_ADDR ,0x08)
        else:
            self.bus.write_byte(LCD_ADDR ,0x00)

    def _send_command(self, comm):
        # Send bit7-4 firstly
        buf = comm & 0xF0
        buf |= 0x04               # RS = 0, RW = 0, EN = 1
        self._write_word(self.LCD_ADDR ,buf)
        time.sleep(0.002)
        buf &= 0xFB               # Make EN = 0
        self._write_word(self.LCD_ADDR ,buf)
        
        # Send bit3-0 secondly
        buf = (comm & 0x0F) << 4
        buf |= 0x04               # RS = 0, RW = 0, EN = 1
        self._write_word(self.LCD_ADDR ,buf)
        time.sleep(0.002)
        buf &= 0xFB               # Make EN = 0
        self._write_word(self.LCD_ADDR ,buf)

    def _write_word(self, addr, data):
        temp = data
        if self.BACKGROUND_LIGHT == 1:
            temp |= 0x08
        else:
            temp &= 0xF7
        self.bus.write_byte(addr ,temp)

    def _send_data(self, data):
        # Send bit7-4 firstly
        buf = data & 0xF0
        buf |= 0x05               # RS = 1, RW = 0, EN = 1
        self._write_word(self.LCD_ADDR ,buf)
        time.sleep(0.002)
        buf &= 0xFB               # Make EN = 0
        self._write_word(self.LCD_ADDR ,buf)
        
        # Send bit3-0 secondly
        buf = (data & 0x0F) << 4
        buf |= 0x05               # RS = 1, RW = 0, EN = 1
        self._write_word(self.LCD_ADDR ,buf)
        time.sleep(0.002)
        buf &= 0xFB               # Make EN = 0
        self._write_word(self.LCD_ADDR ,buf)

    def print_lcd(self, x, y, str):
        if x < 0:
            x = 0
        if x > 15:
            x = 15
        if y <0:
            y = 0
        if y > 1:
            y = 1
 
        # Move cursor
        addr = 0x80 + 0x40 * y + x
        self._send_command(addr)
        
        for chr in str:
            self._send_data(ord(chr))

if __name__ == "__main__":
    lcd = LCD()
    lcd.print_lcd(0, 0, "HELLO")
