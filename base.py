import time

import obd  # library for connecting and reading OBD-II
import simpleaudio as sa  # library for playing audio files
import pyttsx3 as tts  # text to speech for connect and speed prompts
import multiprocessing

from pynput.mouse import Listener

# A shared value
THRESHOLD = 30
ENABLED = False

# A lock for synchronizing access to x
THRESHOLD_lock = multiprocessing.Lock()
ENABLED_lock = multiprocessing.Lock()

def eventListener():
    global THRESHOLD
    global ENABLED

    with Listener(on_click=on_click) as listener:
        listener.join()

def speedListener():
    global THRESHOLD
    global ENABLED

    # # obd connection initialization
    # connection = obd.OBD()  # auto-connects to USB or RF port
    # # txt->speech "connected"
    # speak("car connected")
    #
    # while True:
    #     trackSpeed = obd.commands.SPEED  # select an OBD command (sensor)
    #     response = connection.query(trackSpeed)  # send the command, and parse the response
    #     print(response.value)  # returns unit-bearing values thanks to Pint
    #     print(response.value.to("mph"))  # user-friendly unit conversions
    #     if threshold < response.value.to("mph") and enabled:
    #         print(threshold)
    #         playDing()
    #     time.sleep(1.5)

    # obd connection initialization
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
            print(THRESHOLD)
            playDing()

        time.sleep(1.7)


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    THRESHOLD + 5
    if not pressed:
        THRESHOLD + 5
        return True

def speak(text):
    engine = tts.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


def playDing():
    wave_obj = sa.WaveObject.from_wave_file("speedchime.wav")
    play_obj = wave_obj.play()


def incThresh(thresh):
    return thresh + 5


def decThresh(thresh):
    return thresh - 5


if __name__ == "__main__":
    t1 = multiprocessing.Process(
        name='speedListener',
        target=speedListener,
    )
    t2 = multiprocessing.Process(
        name='eventListener',
        target=eventListener,
    )

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # print (x)