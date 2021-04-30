import spidev
import sys
import time

class VFD:
    def __init__(self, spi_num, spi_ce):
        self.spi = spidev.SpiDev()
        self.spi.open(spi_num, spi_ce)
        # on raspberry pi zero w buster, speed was set to 1250000 and didn't work
#        self.spi.max_speed_hz = 1250000
        self.spi.max_speed_hz = 2500000
#        self.spi.max_speed_hz = 500000
        self.setDisplay(True, False, False)
        self.setDirection(True, False)


    def VFD_SPIDATA(self, data): 
        self.spi.writebytes([0xFA, data])
        time.sleep(0.00001)
        
        
    def VFD_SPICOMMAND(self, data): 
        self.spi.writebytes([0xF8, data])
        time.sleep(0.00001)


    def writeCmd(self, c): 
        self.VFD_SPICOMMAND(c)
        time.sleep(0.00001)
        
    def writeStr(self, s): 
        for c in s:
            self.VFD_SPIDATA(ord(c))
            time.sleep(0.00001)
            
  
    def cls(self):
        self.VFD_SPICOMMAND(0x01)
        time.sleep(0.005)

    def setPosition(self, x, y):
        self.VFD_SPICOMMAND(0x80 | (0x40*y + x))
        time.sleep(0.005)
        
    def setDirection(self, leftToRight, autoScroll):
        cmd = 4
        if leftToRight:
            cmd = cmd | 2
        if autoScroll:
            cmd = cmd | 1

        self.VFD_SPICOMMAND(cmd)
        

            
            
    def setDisplay(self, display, cursor, blink):
        cmd = 8
        if display:
            cmd = cmd | 4
        if cursor:
            cmd = cmd | 2
        if blink:
            cmd = cmd | 1

        self.VFD_SPICOMMAND(cmd)

              

    def scrollDisplayLeft(self):
        self.VFD_SPICOMMAND(0x10 | 0x08 | 0x00)
        
    def scrollDisplayRight(self):
        self.VFD_SPICOMMAND(0x10 | 0x08 | 0x04)       
        

    def createChar(self, char_vfd_number, char_maps):
        charmap_ = char_maps
        char_ = 0
        numer_char_vfd = 64 + char_vfd_number * 8
        self.VFD_SPICOMMAND(numer_char_vfd) 
        for char_ in range(0, 7):
            dat = int(charmap_[char_], 2)
            self.VFD_SPIDATA(dat)
        
    def printChar(self, numer_char):
        self.VFD_SPIDATA(numer_char)

    def displayOnOff(self, status):
        if status == "on":
            self.VFD_SPICOMMAND(12)
            time.sleep(0.005)

        if status == "off":
            self.VFD_SPICOMMAND(8)
            time.sleep(0.005)

    def brightness(self, brit):
        if brit == 25:
           self.VFD_SPICOMMAND(48)
           time.sleep(0.005)
           self.VFD_SPIDATA(3)
           time.sleep(0.005)

        if brit == 50:
           self.VFD_SPICOMMAND(48)
           time.sleep(0.005)
           self.VFD_SPIDATA(2)
           time.sleep(0.005)

        if brit == 75:
           self.VFD_SPICOMMAND(48)
           time.sleep(0.005)
           self.VFD_SPIDATA(1)
           time.sleep(0.005)

        if brit == 100:
           self.VFD_SPICOMMAND(48)
           time.sleep(0.005)
           self.VFD_SPICOMMAND(0)
           time.sleep(0.005)

