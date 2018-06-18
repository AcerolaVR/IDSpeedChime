import time

import obd # library for connecting and reading OBD-II
import simpleaudio as sa # library for playing audio files
import pyttsx3 as tts # text to speech for connect and speed prompts

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

    threshold = 30
    enabled = True

    # obd connection initialization
    connection = obd.OBD()  # auto-connects to USB or RF port
    # txt->speech "connected"
    speak("car connected")

    while True:
        trackSpeed = obd.commands.SPEED  # select an OBD command (sensor)
        response = connection.query(trackSpeed)  # send the command, and parse the response
        print(response.value)  # returns unit-bearing values thanks to Pint
        print(response.value.to("mph"))  # user-friendly unit conversions
        if threshold < response.value.to("mph") and enabled:
            print(threshold)
            playDing()
        time.sleep(1.5)
