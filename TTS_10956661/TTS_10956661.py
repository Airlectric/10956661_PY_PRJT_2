import PySimpleGUI as sg
import pyttsx3

def speak(text, volume, speed, voice_id):
    # Starting the text to speech engine
    engine = pyttsx3.init()

    # Setting the voice and speech 
    engine.setProperty('voice', voice_id)
    engine.setProperty('volume', volume / 100)
    engine.setProperty('rate', speed)

    
    engine.say(text)
    engine.runAndWait()

# layout of the app
layout = [
    [sg.Text('Enter text here :', font=('Arial', 15)), sg.InputText(key='-INPUT-', font=('Arial', 15)), sg.Button('Speak', font=('Arial', 15))],
    [sg.Text('Select a voice:', font=('Arial', 15)), sg.Radio('Male', "RADIO1", default=True, font=('Arial', 15), key='-MALE-'), sg.Radio('Female', "RADIO1", font=('Arial', 15), key='-FEMALE-')],
    [sg.Text('Adjust the volume:', font=('Arial', 15)), sg.Slider(range=(0, 100), default_value=50, orientation='h', size=(20, 15), font=('Arial', 15), key='-VOLUME-')],
    [sg.Text('Adjust the speed:', font=('Arial', 15)), sg.Slider(range=(100, 500), default_value=200, orientation='h', size=(20, 15), font=('Arial', 15), key='-SPEED-')],
    [sg.Button('Exit',font=('Arial', 15))]
]


sg.theme('DarkBlue15') # Setting the theme 
window = sg.Window('Text-to-Speech App', layout ) #creating the window

# Defining IDs of male and female voice
male_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
female_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

# looping of events
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Speak':
        text = values['-INPUT-']
        volume = values['-VOLUME-']
        speed = values['-SPEED-']
        voice_id = male_voice_id if values['-MALE-'] else female_voice_id
        speak(text, volume, speed, voice_id)


window.close()
