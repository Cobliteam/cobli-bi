from PySimpleGUI import PySimpleGUI as sg
import os

def new_line(i):
    return [[sg.T("Nome da Frota: ", key=f"fleetInput {i}"), sg.InputText(key=f"fleet {i}", size=[30, 1]), 
        sg.T("Chave de API", key=f"apiKeyInput {i}"), sg.InputText(key=f"apiKey {i}", size=[30, 1]),
        sg.T("Chave API Inválida", key=f"errorMessage {i}", visible=False, text_color="red"),
        ]]

def gui(check_api_keys):

    sg.theme('Reddit')

    layout = [
        [sg.Text('Por favor, digite abaixo o nome das frotas, e suas chaves de API correspondentes:')],
        [sg.Column(new_line(0), key='-Column-')],
        [sg.Button('Gerar Script', key='-generate-'), sg.Button("Adicionar", key="-plus-")],
    ]

    # Create the window
    window = sg.Window("Demo", layout, default_element_size=(30, 2))

    # Create an event loop
    i = 1
    dataList = dict()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == '-plus-':
            if i<5:
                window.extend_layout(window['-Column-'], new_line(i))
                i += 1
        if event == '-generate-':
            for element in range(i):
                dataList[values[f"fleet {element}"]] = values[f"apiKey {element}"]
                window.find_element(f"errorMessage {element}").Update(visible=False)
              
            invalidApiKeyIndex = check_api_keys(dataList)
            dataList = dict()
            if invalidApiKeyIndex or invalidApiKeyIndex == 0:
                window.find_element(f"errorMessage {invalidApiKeyIndex}").Update(visible=True)
            else: 
                window.extend_layout(window['-Column-'], [[sg.Output(size=(90,20))]]) 
                with open(os.path.expanduser('~/cobliBI/main_file.txt'), 'r') as main_file:
                    print(main_file.read())
                window.find_element("-plus-").Update(disabled=True)
                window.find_element("-generate-").Update(disabled=True)
    window.close()