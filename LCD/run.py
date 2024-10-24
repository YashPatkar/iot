import lcd
lcd.init(0x27, 1)
while(True):
    lcd.write(0,0,"Hello")
    lcd.write(0,1,"World")