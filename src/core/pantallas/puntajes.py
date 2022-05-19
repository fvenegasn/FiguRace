import PySimpleGUI as sg

def abrir_puntajes():
    layout = [
        [
            sg.Text("Pantalla de puntajes",font=('Arial',15))
            ],
        [
            sg.Button("Volver al menú", key="-Volver-",font=('Arial',14))
            ],
    ]
    return sg.Window("Pantalla de puntajes", layout, margins=(100, 100),finalize=True)