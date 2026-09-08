# Parcial — Detector de Transmisiones Sospechosas

Nombre:  Saray Natalia Duarte Florez


## 1. ¿Qué debe hacer el programa?

Escriba en maximo 3 o 4 lineas cual es el objetivo del programa.

Respuesta:

Menciona que registra trnasmiciones, 
analiza si el mensaje es sospechoso,
calcula un puntaje y asigna una calificacion 

---

## 2. Clase `Transmision`

La clase tendra los siguientes atributos:

- `id`:
- `origen`:
- `mensaje`:
- `puntaje`:
- `clasificacion`:

Escriba brevemente que representa cada uno.

"id": identifica de manera unica la transmision.
"origen":  ¿de donde viene o quien la envia?
"mensaje":  ¿que informacion contiene?
"puntaje": ¿que tan sospechosa resulto?
"clasificacion":  ¿como queda catalogada segun el puntaje?

---

## 3. Métodos

### `analizar()`


Responsabilidad: revisa el mensaje y calcula el puntaje

### `clasificar()`

Responsabilidad: toma el puntaje y decide la categoría

### `to_dict()`

Responsabilidad: convierte el objeto en un diccionario para poder guardarlo

### `from_dict()`

Responsabilidad: hace lo contrario: recibe un diccionario y crea nuevamente un objeto

---

## 4. Algoritmo de análisis

Complete el siguiente pseudocódigo:

```text
puntaje = 0

SI el valor es mayor o igual a $2.000.000
    sumar 30 puntos

SI la hora está entre 0 y 5
    sumar 20 puntos

SI el país es diferente de Colombia
    sumar 25 puntos

SI el dispositivo NO es conocido
    sumar 30 puntos
```

---

## 5. Persistencia

Explique brevemente qué ocurre al iniciar el programa:

```text
JSON
 ↓
diccionarios
 ↓
objetos Transmision
```

Explique qué ocurre al guardar:

```text
Objetos
 ↓
diccionarios
 ↓
JSON
```

---

## 6. Menú

Indique qué debe hacer cada opción:

### Opción 1 — Registrar transmisión

1.  Pedir los datos.
2. Crear la transmisión y analizarla.
3. Agregarla a la lista

### Opción 2 — Listar transmisiones

1.  Recorrer la lista.
2. Mostrar los datos de cada transmisión 

### Opción 3 — Salir

Acción:  terminar el programa

---

## Nota

Este archivo debe completarse durante los primeros 15 minutos del parcial, antes de comenzar la implementación.