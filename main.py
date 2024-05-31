import PySimpleGUI as sg

def convert_feet_inches_to_meters(feet_input, inches_input):
  #consts
  inch = 2.54/100
  feet = 12 * inch

  return round(feet_input*feet+inches_input*inch, 3)

# All the stuff inside your window.
layout = [  [sg.Text('Enter feet:'), sg.InputText()],
            [sg.Text('Enter inches:'), sg.InputText()],
            [sg.Button('Convert'), sg.Button('Exit'), sg.Text(key='-METERS-') ]]
#
# Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    feet_input = float(values[0])
    inches_input = float(values[1])

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Convert':
      meters_converted = convert_feet_inches_to_meters(feet_input, inches_input)
      window['-METERS-'].update(meters_converted)

window.close()