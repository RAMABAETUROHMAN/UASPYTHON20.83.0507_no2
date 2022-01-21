import PySimpleGUI as sg

sg.theme("DarkTeal2")
#building design
layout = [[sg.T("")],
          [sg.Text("Choose a folder : "), sg.Input(key="-IN2-" ,change_submits=True), sg.FileBrowse("Browse",key="-IN-")],
          [sg.Button("Submit"), sg.Button("Exit")]]

#Building Window
window = sg.Window('Encode & Decode', layout, size=(600,150))
    
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event=="Exit":
        window.close()
        raise SystemExit()
        break
    elif event == "Submit":
        print(values["-IN-"])
        file = open(values["-IN-"],'rb')
        data = file.read()
        file.close()

        data = bytearray(data)
        for index, nilai in enumerate(data):
            data[index] = nilai ^ 152

        file = open(values["-IN-"], 'wb')
        file.write(data)
        file.close()
        sg.popup('\nEncode Succes\n')


