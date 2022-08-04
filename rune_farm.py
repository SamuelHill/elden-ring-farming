from time import sleep, time
from sys import argv, exit as sys_exit
from pyautogui import getActiveWindow
from pydirectinput import press, keyUp, keyDown


def farming_loop(num_runs, timed):
    # Wait for Elden Ring to become the active window
    while getActiveWindow().title != 'ELDEN RING™':
        sleep(1)
    sleep(3)  # give the player a moment to exit any menus etc.
    running_average = []  # only needed if you want timing data
    for run_num in range(num_runs):
        allow_farming_pause(timed_farming_run if timed else farming_run,
                            run_num, num_runs, running_average)
    print()  # keeps last print statement on screen


def allow_farming_pause(farming_code, run_num, num_runs, running_average):
    run_text = f'On run number {run_num + 1} of {num_runs}'
    try:
        farming_code(run_text, running_average)
    except KeyboardInterrupt:
        # extra spaces at the end of the string clear avg runtime text...
        print(f'Paused during run number {run_num + 1} of {num_runs}...      ')
        if input('Continue? (y/n) ') not in ('', 'y'):
            sys_exit()
        sleep(3)  # give the player a moment to exit any menus again


def timed_farming_run(run_text, running_average):
    start = time()
    farming_run(run_text, running_average)  # ignores second input
    running_average.append(time() - start)
    avg = round(sum(running_average)/len(running_average), 2)
    print(f'{run_text}, avg runtime ~ {avg}s', end='\r')


def farming_run(run_text, _):  # second input for matching timed signature
    print(run_text, end='\r')
    go_to_grace()
    if INVINCIBLE:
        drink_pysick()
    call_torrent()
    run()


def go_to_grace():
    press('g')  # bring up map
    press('f')  # bring up sites of grace menu
    press('e')  # select lenne's rise (autoselected by proximity)
    press('e')  # confirm travel
    sleep(6)  # travel loading screen wait time


def drink_pysick():
    sleep(1)
    press('r')  # drink phsyick with twiggy cracked tear
    sleep(1)


def call_torrent():
    keyDown('e')  # hold e for pouch
    sleep(.8)
    press('up')  # spectral steed whistle in upper slot
    keyUp('e')


def run():
    keyDown('d')  # immediately start turning while mounting
    sleep(2)
    keyDown('w')  # begin straightening out
    keyUp('d')  # should be just past the first tree
    press('space')  # start sprinting
    keyDown('d')  # minor path adjust 1, get in line with
    sleep(.55)
    keyUp('d')  # the edges of the rock and root that jut out
    sleep(4)  # (on the right side of the path)
    keyDown('a')  # minor path adjust 2, get in line with
    sleep(.3)
    keyUp('a')  # the edge on the small ledge on the left
    sleep(3.7)
    # Begin dodge manuver
    keyDown('d')
    keyUp('w')
    press('space')
    sleep(.7)
    keyDown('w')
    sleep(.8)
    keyUp('d')
    keyUp('w')
    if NO_HUMAN:
        turn_left()
    else:
        sleep(.8)
    sleep(3)  # wait for ball to de-agro so map works, also gives player an
    # opportunity to adjust camera to look over the edge (helps with runes)
    # pydirectinput.move(120, -10), can't get to work reliably...


def turn_left():
    sleep(.3)
    keyDown('x')
    sleep(.1)
    keyUp('x')
    sleep(.2)
    keyDown('a')
    sleep(.65)
    keyUp('a')
    press('q')
    keyDown('w')
    sleep(.15)
    keyUp('w')
    sleep(.3)


if __name__ == '__main__':
    INVINCIBLE = False
    NO_HUMAN = False
    farming_loop(int(argv[1]) if len(argv) > 1 else 10,
                 argv[2] == 't' if len(argv) > 2 else False)
