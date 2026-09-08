import json
import os


class Transaccion:

    def __init__(self, id, titular, valor, hora, pais, dispositivo_conocido):
        self.id = id
        self.titular = titular
        self.valor = valor
        self.hora = hora
        self.pais = pais
        self.dispositivo_conocido = dispositivo_conocido

        self.puntaje_riesgo = self.calcular_riesgo()
        self.clasificacion = self.clasificar()

    def calcular_riesgo(self):
        puntaje = 0

        if self.valor >= 2000000:
            puntaje += 30

        if 0 <= self.hora <= 5:
            puntaje += 20

        if self.pais.lower() != "colombia":
            puntaje += 25

        if self.dispositivo_conocido == False:
            puntaje += 30

        return puntaje

    def clasificar(self):
        if self.puntaje_riesgo <= 29:
            return "NORMAL"
        elif self.puntaje_riesgo <= 59:
            return "SOSPECHOSA"
        else:
            return "ALTO RIESGO"

    def to_dict(self):
        return {
            "id": self.id,
            "titular": self.titular,
            "valor": self.valor,
            "hora": self.hora,
            "pais": self.pais,
            "dispositivo_conocido": self.dispositivo_conocido,
            "puntaje_riesgo": self.puntaje_riesgo,
            "clasificacion": self.clasificacion
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos["id"],
            datos["titular"],
            datos["valor"],
            datos["hora"],
            datos["pais"],
            datos["dispositivo_conocido"]
        )


def cargar_transacciones():
    if os.path.exists("transacciones.json"):
        try:
            with open("transacciones.json", "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            transacciones = []

            for dato in datos:
                transaccion = Transaccion.from_dict(dato)
                transacciones.append(transaccion)

            return transacciones

        except (json.JSONDecodeError, KeyError):
            print("El archivo JSON tiene un formato incorrecto.")
            return []

    return []


def guardar_transacciones(transacciones):
    datos = []

    for transaccion in transacciones:
        datos.append(transaccion.to_dict())

    with open("transacciones.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def pedir_transaccion():
    while True:
        titular = input("Ingrese el titular: ").strip()

        if titular != "":
            break

        print("El titular no puede estar vacío.")

    while True:
        try:
            valor = float(input("Ingrese el valor: "))

            if valor > 0:
                break

            print("El valor debe ser mayor que cero.")

        except ValueError:
            print("Ingrese un valor numérico válido.")

    while True:
        try:
            hora = int(input("Ingrese la hora (0-23): "))

            if 0 <= hora <= 23:
                break

            print("La hora debe estar entre 0 y 23.")

        except ValueError:
            print("Ingrese una hora válida.")

    while True:
        pais = input("Ingrese el país: ").strip()

        if pais != "":
            break

        print("El país no puede estar vacío.")

    while True:
        dispositivo = input(
            "¿El dispositivo es conocido? (True/False): "
        ).strip().lower()

        if dispositivo == "true":
            dispositivo_conocido = True
            break

        elif dispositivo == "false":
            dispositivo_conocido = False
            break

        else:
            print("Debe escribir True o False.")

    return titular, valor, hora, pais, dispositivo_conocido


def mostrar_transaccion(transaccion):
    print("------------------------------")
    print("ID:", transaccion.id)
    print("Titular:", transaccion.titular)
    print("Puntaje de riesgo:", transaccion.puntaje_riesgo)
    print("Clasificación:", transaccion.clasificacion)


# PROGRAMA PRINCIPAL

transacciones = cargar_transacciones()

# Caso 1
caso1 = Transaccion(
    1,
    "Laura Gómez",
    3500000,
    2,
    "Colombia",
    False
)

# Caso 2
caso2 = Transaccion(
    2,
    "Carlos Pérez",
    500000,
    14,
    "Colombia",
    True
)

# Caso 3
caso3 = Transaccion(
    3,
    "Ana Torres",
    2500000,
    10,
    "Perú",
    True
)

transacciones.append(caso1)
transacciones.append(caso2)
transacciones.append(caso3)


for transaccion in transacciones:
    mostrar_transaccion(transaccion)


guardar_transacciones(transacciones)

print("------------------------------")
print("Transacciones guardadas correctamente.")