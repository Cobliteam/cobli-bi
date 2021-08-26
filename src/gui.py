from PySimpleGUI import PySimpleGUI as sg

def new_line(i):
    return [[sg.T("Nome da Frota: ", key=f"fleetInput {i}"), sg.InputText(key=f"fleet {i}"), 
        sg.T("Chave de API", key=f"apiKeyInput {i}"), sg.InputText(key=f"apiKey {i}"),
        sg.T("Chave API Inválida", key=f"errorMessage {i}", visible=False, text_color="red")]]

def gui(check_api_keys):

    sg.theme('Reddit')

    layout = [
        [sg.Text('Por favor, digite abaixo o nome das frotas, e suas chaves de API correspondentes:')],
        [sg.Column(new_line(0), key='-Column-')],
        [sg.Button('Gerar Script'), sg.Button("Adicionar", key="-plus-")]
    ]
    # Create the window
    window = sg.Window("Demo", layout)

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
        if event == 'Gerar Script':
            for element in range(i):
                dataList[values[f"fleet {element}"]] = values[f"apiKey {element}"]
                window.find_element(f"errorMessage {element}").Update(visible=False)
            InvalidApiKeyIndex = check_api_keys(dataList)
            window.find_element(f"errorMessage {InvalidApiKeyIndex}").Update(visible=True)