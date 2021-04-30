import vfd_display_class
import time

b = vfd_display_class.VFD(0, 0)

print("Some info to know that script is running")
#set character (max 8 (0-7), driver limitation)

Custom_character_0 = ["00000","11111","10101","11111","11111","01010","01010","11011"]
Custom_character_1 = ["00000","00000","01010","00000","10001","11111","00000","00000"]
Custom_character_2 = ["01110","10001","10000","11111","11111","11011","11111","11111"]

#create characters
b.createChar(0, Custom_character_0)
b.createChar(1, Custom_character_1)
b.createChar(2, Custom_character_2)

#fully clear display
b.cls()

#set position
b.setPosition(1, 0)
#wtite text
b.writeStr("Test")

time.sleep(2)

b.cls()
b.setPosition(0, 0)
#print char
b.printChar(0)

b.setPosition(2, 0)
#print char
b.printChar(1)

b.setPosition(4, 0)
#print char
b.printChar(2)


time.sleep(2)

b.cls()
#brightness test
b.setPosition(0, 0)
b.brightness(25)
b.writeStr("Brightness 25%")

time.sleep(2)

b.cls()
b.setPosition(0, 0)
b.brightness(50)
b.writeStr("Brightness 50%")

time.sleep(2)

b.cls()
b.setPosition(0, 0)
b.brightness(75)
b.writeStr("Brightness 75%")

time.sleep(2)

b.cls()
b.setPosition(0, 0)
b.brightness(100)
b.writeStr("Brightness 100%")

time.sleep(2)

b.cls()
b.setPosition(0, 0)
b.writeStr("Bye, and have fun!")

print("Some info to know that script ends")

