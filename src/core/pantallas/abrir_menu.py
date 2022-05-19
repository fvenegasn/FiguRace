import os
import PySimpleGUI as sg

def abrir_menu():

    ruta_imagen = os.path.join(os.getcwd(),'imagenes','figurace_logo.png')
    
    perfiles_lista = ['Aca','van','los','perfiles']

    menu = [
        [
            sg.Button("Jugar",key="-Jugar-",font=('Arial',27))
            ],
        [
            sg.Button("Configuración",font=('Arial',20))
            ],
        [
            sg.Button("Puntaje",key='-Puntajes-',font=('Arial',20))
            ],
        [
            sg.Button("Perfil",font=('Arial',20))
            ],
        ]

    perfiles = [
        [
            sg.Text("Perfiles",font=('Arial',15))
            ],
        [
            sg.Listbox(values=perfiles_lista,size=(15,10),horizontal_scroll=True)
            ]
    ]

    dificultad = [
        [
            sg.Text("DIFICULTAD: ",font=('Arial',13)),
            sg.Checkbox("Fácil",font=('Arial',12)),
            sg.Checkbox("Media",font=('Arial',12)),
            sg.Checkbox("Difícil",font=('Arial',12))
            ]

    ]
 
    layout = [
        [
            sg.Image(ruta_imagen)
            ],
        [
            sg.Column(menu),sg.Column(perfiles)
            ],
        [
            dificultad
        ]
    ]
    return sg.Window("Menú",layout,finalize=True)