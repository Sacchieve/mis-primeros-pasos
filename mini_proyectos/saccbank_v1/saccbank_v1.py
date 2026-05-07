# Simulacion de sistema de gestión de banco "SaccBank" v1 con validacion de datos.
import random

numeros_aleatorio = (
    str(random.randint(0, 9))
    + str(random.randint(0, 9))
    + str(random.randint(0, 9))
    + str(random.randint(0, 9))
)

# Pedido de datos para el perfil del usuario y validacion de datos.
while True:
    nombre_usuario = input("Por favor ingrese su primer nombre: ").replace(" ", "")
    if not nombre_usuario.isalpha():
        print("No puede hacer uso de numeros en el nombre.")
    elif len(nombre_usuario) < 3:
        print("El nombre debe de contener 3 caracteres o mas.")
    else:
        break

while True:
    apellido_usuario = input("Por favor ingrese su primer apellido: ").replace(" ", "")
    if not apellido_usuario.isalpha():
        print("No puede hacer uso de numeros en el apellido.")
    elif len(apellido_usuario) < 3:
        print("El apellido debe de contener 3 caracteres o mas.")
    else:
        break

# Creación del perfil del usuario en el banco e impresion del mismo.
nombre_operativo = nombre_usuario.upper()[:3] + apellido_usuario.upper()[:3]
identidad_de_usuario = nombre_operativo + numeros_aleatorio
cuenta_operativa = True
estado_de_cuenta = "Operativa." if cuenta_operativa else "Restringida."
monto_de_cuenta = 0.00

print(f"""       ¡Bienvenido a SaccBank! 
Por favor recuerde su identidad de usuario, ya que si la pierde por cualquier motivo
¡Usted podria perder acceso a nuestros servicios!
Nombre registrado: {nombre_usuario}
Apellido registrado: {apellido_usuario}
Numero de Identidad creado: {numeros_aleatorio}
Identidad de usuario final: {identidad_de_usuario}""")

# Empezamos a formar movimiento en la cuenta del usuario.
depositar = input("¿Cuanto sera el monto de su primer deposito?: ")

while not depositar.replace(".", "", 1).isdigit():
    depositar = input("¡Valor no valido! Por favor ingrese unicamente numeros: ")
monto_de_cuenta += float(depositar)
print(
    f"¡Deposito completado con exito! Usted ahora tiene {monto_de_cuenta}$ en su cuenta"
)
monto_retirar = monto_de_cuenta * 0.12
retiro = (
    input(
        f"Nos ha llegado una solicitud con un retiro de {monto_retirar}$, ¿confirma usted el deposito (Si/No)?: "
    )
    .lower()
    .replace(" ", "")
)

while retiro not in ["si", "no"]:
    retiro = (
        input(
            "Respuesta no valida. Por favor ingrese 'Si' o 'No' como respuesta valida: "
        )
        .lower()
        .replace(" ", "")
    )
if retiro == "si":
    print(
        "Por favor, por su seguridad y la nuestra, primero debe verificar su identidad"
    )
    verificacion = input("Ingrese por favor su identidad de usuario: ")
    while verificacion != identidad_de_usuario:
        verificacion = input("Identidad de usuario incorrecta, intentelo otra vez: ")
    if verificacion == identidad_de_usuario:
        monto_de_cuenta -= monto_retirar
        print(
            f"Pago procesado, el dinero se retirara en un lapso de 72 horas habiles. Monto a retirar: {monto_retirar}. Saldo restante en su cuenta: {monto_de_cuenta}"
        )
else:
    vulnerabilidad = input("""¡Cuenta vulnerada!
Por favor, ingrese '1' si quiere bloquear su cuenta.
Ingrese '2' si quiere cambiar de identidad de usuario.
Ingrese su respuesta: """)
    while vulnerabilidad not in ["1", "2"]:
        vulnerabilidad = input(
            "Respuesta no valida, por favor ingrese 1 o 2 para alguna de las dos opciones mencionadas: "
        )
    if vulnerabilidad == "1":
        cuenta_operativa = False
        estado_de_cuenta = "Operativa" if cuenta_operativa else "Restringida"
        print(f"Defensa exitosa. Estado de la cuenta: {estado_de_cuenta}")
    else:
        identidad_de_usuario = nombre_operativo + (
            str(random.randint(0, 9))
            + str(random.randint(0, 9))
            + str(random.randint(0, 9))
            + str(random.randint(0, 9))
        )
        print(
            f"¡Identidad de usuario cambiada! Su nueva identidad de usuario en nuestro banco es: {identidad_de_usuario}"
        )
