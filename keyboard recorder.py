# Keyboard module in Python 
import keyboard 
# It records all the keys until escape is pressed 
rk = keyboard.record(until = 'esc') 
  
# It replay back the all keys 
print("\n")
keyboard.play(rk, speed_factor = 1000) 
print("\n")
