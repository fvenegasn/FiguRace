import PySimpleGUI as sg

def abrir_juego():
    layout = [
        [
            sg.Text("Pantalla de juego",font=('Arial',15))
            ],
        [
            sg.Button("Volver al menú", key="-Volver-",font=('Arial',14))
            ],
    ]
    return sg.Window("Pantalla de Juego", layout, margins=(100, 100),finalize=True)