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

![PCB Bottom](https://github.com/GrazerComputerClub/Game0-xHAT/raw/master/GV-xHAT_top.png)
![PCB Bottom](https://github.com/GrazerComputerClub/Game0-xHAT/raw/master/GV-xHAT_bottom.png)


## Screenshots 160x128 display

![Console](https://github.com/GrazerComputerClub/Game0-xHAT/raw/master/screenshots/160x128/Console.png)
![Gameboy - Tetris](https://github.com/GrazerComputerClub/Game0-xHAT/raw/master/screenshots/160x128/Tetris.png)
![Gameboy Color - Skoardy](https://github.com/GrazerComputerClub/Game0-xHAT/raw/master/screenshots/160x128/Skoardy.png)
![Mega Drive - Sonic](https://github.com/GrazerComputerClub/Game0-xHAT/raw/master/screenshots/160x128/Sonic.png)
![Mega Drive - Thunder Force IV](https://github.com/GrazerComputerClub/Game0-xHAT/raw/master/screenshots/160x128/ThunderForceIV.png)
![SummVM - Space Quest (Menü)](https://github.com/GrazerComputerClub/Game0-xHAT/raw/master/screenshots/160x128/ScummVM-Menu.png)
![SummVM - Space Quest (Text)](https://github.com/GrazerComputerClub/Game0-xHAT/raw/master/screenshots/160x128/ScummVM-Text.png)
