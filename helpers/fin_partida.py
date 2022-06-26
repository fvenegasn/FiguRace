import time
from common.manejo_datos_juego import guardar_partida, guardar_puntaje, guardar_puntaje_maximo 
from common.partida import Partida
import PySimpleGUI as sg

def fin_partida(id_partida,usuarie,nivel,genero,dataset,data):
    partida = Partida(int(time.time()),id_partida,'fin',usuarie,'finalizada','-','-',nivel,genero, dataset)
    guardar_partida(partida)

    puntaje_final=data['puntaje']
    guardar_puntaje(usuarie,puntaje_final,nivel)
    if puntaje_final > data['puntaje_max']:
        guardar_puntaje_maximo(usuarie,puntaje_final,nivel)
        sg.Popup(f"Terminaste la partida con un puntaje de {data['puntaje']}")