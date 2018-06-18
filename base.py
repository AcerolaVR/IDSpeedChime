import threading
import time

import pyttsx3 as tts  # text to speech for connect and speed prompts
import simpleaudio as sa  # library for playing audio files
from pynput.mouse import Button, Listener  # library for listening to mouse inputs

# shared value
THRESHOLD = 30  # speed threshold in mph
ENABLED = False  # whether or not the speed chime is enabled

# A lock for synchronizing access to x
THRESHOLD_lock = threading.Lock()
ENABLED_lock = threading.Lock()


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

    while True:
        if ENABLED:
            print(THRESHOLD)
            print(ENABLED)
            playDing()

        time.sleep(1.6)


def on_click(x, y, button, pressed):
    global THRESHOLD
    global ENABLED

    # print the
    print('Pressed' if pressed else 'Released')
    print(button)

    # change the value on release
    if not pressed:
        if button is Button.left:
            THRESHOLD = THRESHOLD - 5
        if button is Button.middle:
            ENABLED = not ENABLED
        if button is Button.right:
            THRESHOLD = THRESHOLD + 5


def speak(text):
    engine = tts.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


def playDing():
    wave_obj = sa.WaveObject.from_wave_file("speedchime.wav")
    play_obj = wave_obj.play()


if __name__ == "__main__":
    t1 = threading.Thread(
        name='speedListener',
        target=speedListener,
    )
    t2 = threading.Thread(
        name='eventListener',
        target=eventListener,
    )

    t1.start()
    t2.start()
