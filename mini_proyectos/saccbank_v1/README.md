# 🏦 SaccBank v1: Simulación de Gestión Bancaria

¡Hola! Aquí Sacc reportándose en el Día 23 de mi aventura con Python. SaccBank es un script interactivo diseñado para simular la creación de un perfil bancario, validación de identidad y gestión de movimientos financieros básicos.

> **Estado del proyecto:** Completado / Versión de aprendizaje 1.0.

## 🚀 ¿Qué hace este script?
Este programa pone a prueba mis primeros pasos en la lógica de programación, con una fuerte inclinación hacia la validación exhaustiva de datos y la implementación de flujos con múltiples opciones.
### Características principales:
- **Registro Seguro**: Validación de nombre y apellido (mínimo 3 caracteres, sin números).

- **Generación de Identidad**: Creación automática de un ID único combinando iniciales y un token numérico aleatorio.

- **Gestión de Depósitos**: Filtro de seguridad que garantiza que solo se procesen valores numéricos.

- **Seguridad Activa**: Simulación de un retiro del 12% del saldo, con verificación de identidad obligatoria.

- **Protocolo de Vulnerabilidad**: Sistema de respuesta ante movimientos no autorizados para bloquear la cuenta o regenerar credenciales.

## 💡 Decisiones de Diseño (¿Por qué lo hice así?)
En este proyecto, tomé decisiones específicas para garantizar la robustez del sistema:
#### 1. Manejo de Identidad Aleatoria
```python
numeros_aleatorio = (
    str(random.randint(0, 9)) + str(random.randint(0, 9)) + 
    str(random.randint(0, 9)) + str(random.randint(0, 9))
)
```
**Motivo**: Decidí usar cuatro randint individuales para que el sistema sea capaz de declarar el número cero a la izquierda. Con un rango como randint(1000, 9999), perdería esa posibilidad, limitando la variedad de los IDs.

#### 2. Normalización de Strings
```python
nombre_usuario = input("...").replace(" ", "")
```
**Motivo**: Opté por .replace(" ", "") en lugar de .strip(). Dado que SaccBank no permite espacios internos en nombres o apellidos para que .isalpha() funcione correctamente, esto elimina errores tipográficos accidentales y asegura que el ID final sea compacto y sin errores.

#### 3. Simulación de Ciberseguridad

```python
else:
    vulnerabilidad = input("""¡Cuenta vulnerada!
Por favor, ingrese '1' si quiere bloquear su cuenta.
Ingrese '2' si quiere cambiar de identidad de usuario.
Ingrese su respuesta: """)
```

**Motivo**: El sistema asume que si el usuario no reconoce un retiro, la cuenta ha sido vulnerada. Esto me permitió practicar la lógica de estados (cambiar cuenta_operativa a False) y ofrecer al usuario caminos alternativos de recuperación.

## 🛠️ Conceptos Aplicados
Para construir esta simulación, utilicé:

**Librería random**: Para generar los tokens de seguridad.

**Bucles Infinitos (while True)**: Para garantizar que el usuario ingrese datos válidos antes de continuar.

**Métodos de String**: ``.isalpha()``, ``.isdigit()``, ``.replace()``, ``.upper()`` y ``.lower()`` para limpiar y formatear entradas.

**Casteo de datos**: Conversión entre strings y floats para cálculos matemáticos precisos.

## 📂 Cómo ejecutarlo
1.  Asegúrate de tener instalado Python **3.14+**.
2. Clona este repositorio o descarga el archivo ``saccbank_v1.py``.
3. Ejecuta en tu terminal:
```python
python saccbank_v1.py
```

## 📘 Mi Objetivo con este Proyecto
Buscaba poner a prueba mi capacidad para crear un flujo donde el usuario tenga **libertad de movimiento** pero dentro de un entorno seguro. Validar datos es mi parte **favorita** del código, y este es el primer paso para construir sistemas que permitan al usuario elegir su propio camino de forma robusta.

------------

> Si quieres charlar sobre validación de datos o lógica en Python, ¡puedes encontrarme en mis redes en el perfil principal!