import time

import simpleaudio as sa
from pynput.mouse import Listener

def playDing():
    wave_obj = sa.WaveObject.from_wave_file("speedchime.wav")
    play_obj = wave_obj.play()
    # play_obj.wait_done()


def incThresh(thresh):
    return thresh + 5


def decThresh(thresh):
    return thresh - 5

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return True


# Collect events until released
with Listener(
        on_click=on_click) as listener:
    listener.join()


if __name__ == "__main__":
    # obd connection initialization
    threshold = 30
    #
    # connection = obd.OBD()  # auto-connects to USB or RF port
    #
    # cmd = obd.commands.SPEED  # select an OBD command (sensor)
    #
    # response = connection.query(cmd)  # send the command, and parse the response

    while True:
        # print(response.value)  # returns unit-bearing values thanks to Pint
        # print(response.value.to("mph"))  # user-friendly unit conversions
        # if threshold < response.value.to("mph"):
        if True:
            print(threshold)
            playDing()

        time.sleep(1.7)
