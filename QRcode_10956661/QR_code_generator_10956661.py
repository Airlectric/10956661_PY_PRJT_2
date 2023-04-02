import qrcode
import PySimpleGUI as sg
import os

# Defining the layout
sg.theme('DarkPurple4')
layout = [
    [sg.Text('Enter text:', font=('Arial', 14)), sg.InputText(key='text', font=('Arial', 15))],
    [sg.Text('Select QR code size:', font=('Arial', 14)), sg.Slider(range=(1, 20), orientation='h', default_value=10, key='size', font=('Arial', 14))],
    [sg.Text('Select QR code color:', font=('Arial', 14))],
    [sg.Radio('Black', "COLOR", default=True, key='color_black', font=('Arial', 14)), sg.Radio('Red', "COLOR", key='color_red', font=('Arial', 14)), sg.Radio('Green', "COLOR", key='color_green', font=('Arial', 14)), sg.Radio('Blue', "COLOR", key='color_blue', font=('Arial', 14))],
    [sg.Text('Select background color:', font=('Arial', 14))],
    [sg.Radio('White', "BG_COLOR", default=True, key='bg_color_white', font=('Arial', 14)), sg.Radio('indigo', "BG_COLOR", key='bg_color_indigo', font=('Arial', 14)), sg.Radio('Yellow', "BG_COLOR", key='bg_color_yellow', font=('Arial', 14)), sg.Radio('Purple', "BG_COLOR", key='bg_color_purple', font=('Arial', 14))],
    [sg.Button('Generate QR Code', font=('Arial', 14)), sg.Button('Exit',font=('Arial', 14))],
    [sg.Image(key='image')]
]

# Creating the window
window = sg.Window('QR Code Generator', layout)#background_color='lightgoldenrodyellow')

# Loop for events
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    

    if event == 'Generate QR Code':
        # Converting text into qr code image
        qr = qrcode.QRCode(version=1, box_size=values['size'], border=4)
        qr.add_data(values['text'])
        qr.make(fit=True)
        img = qr.make_image(fill_color='black' if values['color_black'] else 'red' if values['color_red'] else 'green' if values['color_green'] else 'blue',
                            back_color='white' if values['bg_color_white'] else 'indigo' if values['bg_color_indigo'] else 'yellow' if values['bg_color_yellow'] else 'purple')

        # Saving the QR code image with a filename
        img_file = 'qrcode.png'
        path = os.path.join(os.getcwd(), img_file)
        img.save(path)

        # Updating the window in app to display the QR code image
        window['image'].update(filename=path)


window.close()
