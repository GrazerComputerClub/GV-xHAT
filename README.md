# Game0-xHAT - Gaming xHAT V0.1

This is a modified [Pi-XO](https://github.com/GrazerComputerClub/Pi-XO) Rev. 0.1 PCB Version for use with Raspberry Pi B versions.  
All modifications for new connection or components are marked red. Unused components are removed.  

Key/Button mapping can support Nintendo NES, Gameboy (Color) and Sega Mega Drive layout (Gambatte and PicoDrive Emulator).  
Key/Button mapping can support mouse input (ScummVM). 

## In Action

[![GC2 Game0-xHAT ScummVM](https://img.youtube.com/vi/9YzMNbByE_w/0.jpg)](https://www.youtube.com/watch?v=9YzMNbByE_w)
[![GC2 Game0-xHAT Sega Mega Drive](https://img.youtube.com/vi/PtT1OVjE4Fs/0.jpg)](https://www.youtube.com/watch?v=PtT1OVjE4Fs)[![GC2 Game0-xHAT Nintendo Gameboy](https://img.youtube.com/vi/3sH8cGopgdA/0.jpg)](https://www.youtube.com/watch?v=3sH8cGopgdA)

## Features

- **SPI TFT display** - 160x128 or 320x240
  SPI, CS0   
- **SPI TFT background LED control**
  GPIO18 (active low)
- **SPI TFT display LED voltage monitor**
  MCP3202 (SPI, CS1) CH0 
- **Speaker**
  Mono audio via GPIO13  
- **Analog input (wheel)** 
  MCP3202 (SPI, CS1) - CH1
- **Switches** 
  - 4 x DPAD arranged   
    * Up - GPIO16  
    * Down - GPIO21  
    * Left - GPIO26  
    * Right - GPIO20  
  - 4 x free arranged (NES style) + 1 function  
    * S (S9) - GPIO03
    * P (S6) - GPIO19  
    * O (S8) - GPIO14     
    * X (S7) - GPIO15  
    * Fn (S5) - GPIO02  
- **LED bar (10 elements)**  
  red - GPIO25 (shared with vibration motor, activation via jumper JP)  
  red - GPIO17  
  orange - GPIO18  
  orange - GPIO27  
  orange - GPIO22  
  green - GPIO23  
  green - GPIO23  
  green - GPIO24  
  green - GPIO24  
  blue - GPIO04 (active on boot)   
- **Vibration motor**  
 GPIO25 (shared with first red LED, activation via jumper JP6)

## Jam use case (using and programming)

- SPI TFT Display (SPI)
  - Video
  - Gaming
  - Grafic output
- GPIO Input
  - Joypad
  - Mouse
  - Shutdown
- GPIO Output
  - LEDs
  - vibration motor
- Analog input (SPI)

## Screenshots 160x128 display

![Console](https://github.com/GrazerComputerClub/Game0-xHAT/raw/master/screenshots/160x128/Console.png)
![Gameboy - Tetris](https://github.com/GrazerComputerClub/Game0-xHAT/raw/master/screenshots/160x128/Tetris.png)
![Gameboy Color - Skoardy](https://github.com/GrazerComputerClub/Game0-xHAT/raw/master/screenshots/160x128/Skoardy.png)
![Mega Drive - Sonic](https://github.com/GrazerComputerClub/Game0-xHAT/raw/master/screenshots/160x128/Sonic.png)
![Mega Drive - Thunder Force IV](https://github.com/GrazerComputerClub/Game0-xHAT/raw/master/screenshots/160x128/ThunderForceIV.png)
![SummVM - Space Quest (Menü)](https://github.com/GrazerComputerClub/Game0-xHAT/raw/master/screenshots/160x128/ScummVM-Menu.png)
![SummVM - Space Quest (Text)](https://github.com/GrazerComputerClub/Game0-xHAT/raw/master/screenshots/160x128/ScummVM-Text.png)

# Assembling

![Curcuit](https://github.com/GrazerComputerClub/Game0-xHAT/raw/master/Curcuit.jpg)

![PCB top](https://github.com/GrazerComputerClub/Game0-xHAT/raw/master/GV-xHAT_top.png)
![PCB Bottom](https://github.com/GrazerComputerClub/Game0-xHAT/raw/master/GV-xHAT_bottom.png)

**Order recommendation:**
- Drill 4x1,0 mm hole for new switch left top (use 2,5 mm drill to deburring to remove copper)
- TC1262-3.3
- Changed soldering accourding to PCB picture above
- ...
- LED bar (sodering one pin to right like PCB picture above! Check polarity!)
- Resistor array
- 40-pin Header 
- User 5-pin header to connect audio amplifier board (do not solder speaker +/-!)
- Use 8-pin IC socket for MCP3202
- Place electrical tape on backside of TFT display sd slot
- TFT display
- Fix speaker with hot glue
- use wires to connect speaker contacts with audio amplifier board  

**Hints:** 
- Swiches: Only solder two opposite contacts 
- Solder all components (transistors, resistors, capacitors) to backside 
- Place electrical tape on left backside of PCB (avoid shortcut with USB connector on Raspberry Pi B)


## Components list
	
 1 x Female pin header socket 2x20  (JP1) - Adapter for Raspberry Pi B needed  
 1 x 10-100 KOhm Poti/Trimmer  
 1 x 2Pin + Jumper or Switch 2-pin (JP6, vibration motor on/off)    
 1 x 2Pin + Jumper or Switch 2-pin (JP, left red LED on/off)    
 9 x Tactile switch 6x6mm (S1-S9)  
     https://www.reichelt.com/at/en/short-stroke-key-6x6-mm-height-5-0-mm-12-v-vertical-taster-9302-p44579.html  
 1 x Audio amplifier board PAM8302 (JP3, do not connect PAD5 and PAD6)  
     https://www.ebay.de/sch/i.html?_nkw=PAM8302  
 1 x TC1262-3.3 - Voltage regulator 3,3 V (JP2)  
     https://www.conrad.at/de/p/microchip-technology-tc1262-3-3vdb-pmic-spannungsregler-linear-ldo-positiv-fest-sot-223-3-651849.html  
 1 x Speaker 8 Ohm (connect to amplifier board PAM8302 Output via wire, SP1)  
     https://www.reichelt.com/at/en/metal-speaker-soldered-connection-lsm-36m-b-p145887.html  
     https://www.neuhold-elektronik.at/catshop/product_info.php?products_id=6645  
 1 x LED bar 10 segments - blue orange red (LB10)  
     https://www.ebay.at/sch/i.html?_trksid=m570.l1313&_nkw=10-Segment+MULTICOLOR+Bar  
 1 x Resistor array 1K (RN1)  
     https://secure.reichelt.at/resistor-network-8-res-9-pin-1-0-k-x2126-sil-9-8-1-0k-p18012.html  
 1 x Vibration motor (JP5)  
     https://www.neuhold-elektronik.at/catshop/product_info.php?products_id=6971  
 1 x BC547B transiior (T2)  
     https://secure.reichelt.at/npn-to-92-transistor-45-v-0-1-a-0-5-w-bc-547b-p5006.html  
 1 x BC559 transistor (Q2)  
     https://secure.reichelt.at/bipolartransistor-pnp-30v-0-1a-0-5w-to-92-bc-559c-p219085.html  
 1 x Resistor 4K7 Ohm (Transistor base vibration motor: R2)  
 1 x Resistor 270 Ohm (Audio filter: R3)  
 1 x Resistor 150 Ohm (Audio filter: R4)  
 5 x Resistor 1K Ohm (protection UART: R5, R6; LED-Bar left right; transistor background LED display: R7)   
 1 x Capacitor 33 nF (C1)  
 1 x Electrolytic capacitor 10 uF/6,3 V (C2)  
 1 x Capacitor 100 nF (C5)  
 1 x Electrolytic capacitor 1 uF/6,3 V (connected to PAM8302 supply)  
 1 x MCP3202 - ADC (IC1)  
     https://www.conrad.at/de/p/microchip-technology-mcp3202-ci-p-datenerfassungs-ic-analog-digital-wandler-adc-extern-pdip-8-651461.html  
 1 x Diode 1N4001 (D2)  
     https://secure.reichelt.at/rectifier-diode-do41-50-v-1-a-1n-4001-p1723.html  
 1 x 1,8" Display 160x128 ST7735 11-pin (JP7) or 8-pin (JP11) - https://www.ebay.de/sch/i.html?_nkw=1.8+128x160+ST7735  
     2,2" Display 320x240 ILI9341 9-pin (JB8) - https://www.ebay.de/sch/i.html?_nkw=2.2+ILI9341+240x320  
