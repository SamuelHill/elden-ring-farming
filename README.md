# elden-ring-farming

A simple bit of code to help farm runes in the game Elden Ring.

Use at Lena's Rise. The farming run is built out of a few functions;

- go_to_grace() - which just presses 'gfee' to open the map and fast travel, setting up the start of the run
- if INVINCIBLE: drink_pysick() - optional, use with the twiggy cracked tear to avoid loosing runes on a bad run
- call_torrent() - assumes you have torrent on the upper slot of the pockets (normally mapped to 'e')
- run() - this is where the key strokes for running towards, triggering, and dodging the ball at the bottom of the hill.
    - if NO_HUMAN: turn_left() - optional, at the end of the run (if you are afk) turn towards the edge of the cliff. This helps to collect runes as you can miss them if you aren't looking where the ball died.

Got the idea when realizing how simple the run/dodge can be even with just the keyboard. Most of the functions are super simple, just calling a few key presses in the same way you would in game. The run function is a little more complicated with the key presses being interwoven to continue the sprint on torrent.

The timings in this code works for my system but may need tweaking for yours.
