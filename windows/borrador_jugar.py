from common.manejo_datos_juego import mostrar_seleccionado, parametros_configuracion,puntaje_usuario

#"----------------Variables del juego------------------"
nick = mostrar_seleccionado('perfil')
dataset_actual = mostrar_seleccionado('dataset')
dificultad_actual = mostrar_seleccionado('dificultad')
puntaje = puntaje_usuario(nick,dificultad_actual)

parametro = parametros_configuracion(dificultad_actual)
tiempo_limite = parametro["tiempo_limite"]
cant_rondas = parametro["cant_rondas"]
rta_correcta = parametro["rta_correcta"]
rta_incorrecta = parametro["rta_incorrecta"]
cant_caracteristicas = parametro["cant_caracteristicas"]
#"-------------------------------------------------------"
