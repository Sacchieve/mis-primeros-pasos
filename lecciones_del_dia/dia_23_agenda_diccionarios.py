# Primera clase del día 23 aprendiendo Python: Agenda de contactos con Diccionarios.
# Usaremos unicamente Diccionarios.

# Cada elemento del diccionario debe estar separado por una ,
# La sintaxis de los diccionarios es: <variable> = {<clave>: <valor>, <clave>: <valor>}
print("=== Agenda de Contactos ===")
agenda_principal = {
    "Carla": {
        "Telefono": "3665776",
        "Mail": "carla@mail.com",
        "Direccion": "Calle principal 164",
    },
    "Sebastian": {
        "Telefono": "2465234",
        "Mail": "sebastian@mail.com",
        "Direccion": "Avenida Sofía",
    },
    "Mario": {
        "Telefono": "8469506",
        "Mail": "mario@mail.com",
        "Direccion": "Plaza central",
    },
}

# Ahora vamos a imprimir diferentes valores del diccionario para verificar todo.
print(
    f"""Información de su contacto Carla:
Nombre: Carla
Telefono: {agenda_principal['Carla']['Telefono']}
Mail: {agenda_principal['Carla']['Mail']}
Dirección: {agenda_principal['Carla']['Direccion']}"""
)  # Para nada la primera vez imprimi los corchetes fuera de las llaves...

# Tambien se puede hacer uso del metodo .get() para buscar un valor en especifico dentro de una lista.
print(f"\nEl correo mail de Mario es: {agenda_principal.get('Mario').get('Mail')}")
# Segun investigue, el metodo get() suele ser el mejor debido a que devuelve None, mientras que [] devuelve error.
# Pero nunca los combines, o se usa get() o se usa [].

# Tal vez rompa el codigo con esto... Pero la experimentación vale mas.
# agenda_principal[input("¿Cual es el nuevo contacto que quiere añadir?")] = {
#    "Telefono": input("¿Cual es el numero de telefono?"),
#    "Mail": input("¿Cual es el mail"),
#    "Direccion": input("¿Cual es la dirección?"),
# }
# Claro, me dejo hacerlo, el problema es que como no lo guarde en variables ahora no se como podria llamarlo a print.
# Conclusiones del codigo: El primer input() se mando hasta el final de la impresión, ademas, no conseguí alguna forma de llamarlo.
# Para añadir algo asi, tendria que primero crear las variables para tener formas de llamarlo al codigo.

# Ahora si, hagamos el codigo correctamente:
nombre_nuevo_contacto = input(
    "¿Cual es el nombre de su nuevo contacto?: "
)  # Hoy no hare validación de datos.
telefono_nuevo_contacto = input("¿Cual es el telefono de su nuevo contacto?: ")
mail_nuevo_contacto = input("¿Cual es el mail de su nuevo contacto?: ")
direccion_nuevo_contacto = input("¿Cual es la direccion de su nuevo contacto?: ")
agenda_principal[nombre_nuevo_contacto] = {
    "Telefono": telefono_nuevo_contacto,
    "Mail": mail_nuevo_contacto,
    "Direccion": direccion_nuevo_contacto,
}
# Si el nombre que el usuario proporcional es el mismo que alguno de los que estan en el diccionario
# Todos los datos de ese contacto se reemplazan.
# Si en cambio, los datos son nuevos, se creara un nuevo elemento en el diccionario.

print(f"""\nInformación del nuevo contacto:
Nombre: {nombre_nuevo_contacto}
Telefono: {agenda_principal.get(nombre_nuevo_contacto).get("Telefono")}
Mail: {agenda_principal.get(nombre_nuevo_contacto).get("Mail")}
Direccion: {agenda_principal.get(nombre_nuevo_contacto).get("Direccion")}""")

# Para eliminar un metodo ya existente, usaremos el metodo .pop()
eliminar_contacto = input("¿Cual es el contacto que quiere eliminar?: ")
agenda_principal.pop(
    eliminar_contacto
)  # Si el usuario proporciona un valor que no se encuentra en el diccionario, devuelve KeyError.

# Verificamos si se elimino correctamente.
se_encuentra = eliminar_contacto in agenda_principal
print(f"¿{eliminar_contacto} se encuetra en la agenda?: {se_encuentra}")

# <diccionario>.pop(<valor que no existe en el diccionario>) -> Devolvera un NameError.
# Pero podemos hacer que nos vuelva un valor en especifico con una coma:
eliminar_valor_inexistente = agenda_principal.pop("Sacchi", None)
print(eliminar_valor_inexistente)  # -> Devuelve None.

# Tambien podemos usar del para eliminar partes de un diccionario.
del agenda_principal[
    "Sebastian"
]  # A diferencia de .pop(), del no permite el segundo argumento. De manera en la que devolvera KeyError si no existe la clave.
# Idealmente, .pop() se usa para extraer el valor hacia otra operacion, mientras que del la elimina directamente
# carla = agenda_principal.pop("Carla")
# print(carla)

print("\nContactos en la agenda")
for nombre, detalles in agenda_principal.items():
    print(f"""
Nombre: {nombre}
    Telefono: {detalles.get('Telefono')}
    Mail: {detalles.get('Mail')}
    Direccion: {detalles.get('Direccion')}""")

# ¡Muchas gracias por acompañarme en la lección de hoy! Hasta aquí la leccion de agenda, y nos vemos pronto. :D
