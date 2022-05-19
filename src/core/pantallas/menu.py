from sre_parse import expand_template
import PySimpleGUI as sg
from abrir_menu import abrir_menu
from juego import abrir_juego
from puntajes import abrir_puntajes

sg.theme('BrightColors')

abrir_menu()

while True:
    current_window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        current_window.close()
        break
    elif event == '-Jugar-':
        abrir_juego()
        current_window.close()
    elif event == '-Puntajes-':
        abrir_puntajes()
        current_window.close()
    elif event == '-Volver-':
        abrir_menu()
        current_window.close()
