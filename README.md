# Sistema de Gestión de Inventario

## Descripción

Sistema desarrollado en Python para la administración de productos dentro de un inventario.

La aplicación permite registrar, buscar, actualizar y eliminar productos electrónicos y alimenticios mediante una interfaz gráfica desarrollada con Flet.

Además, incorpora persistencia de datos mediante archivos JSON, una cola FIFO implementada manualmente para la gestión de productos pendientes de reposición, el patrón de diseño Repository para la administración de datos y pruebas unitarias utilizando pytest.

---

## Objetivo del Proyecto

Desarrollar una aplicación de gestión de inventario que permita aplicar los conceptos de Programación Orientada a Objetos, estructuras de datos lineales, persistencia de datos, patrones de diseño y pruebas unitarias.

El sistema busca administrar productos de forma eficiente mediante operaciones CRUD y gestionar productos pendientes de reposición utilizando una cola FIFO.

---

## Funcionalidades Principales

- Registrar productos.
- Buscar productos por código.
- Actualizar información de productos.
- Eliminar productos.
- Visualizar productos registrados.
- Persistencia de datos mediante archivos JSON.
- Recuperación automática de información al iniciar la aplicación.
- Gestión de productos pendientes de reposición mediante una cola FIFO.
- Interfaz gráfica desarrollada con Flet.
- Validación de datos.
- Pruebas unitarias con pytest.

---

## Estructura del Proyecto

```text
proyecto-inventario/
│
├── main.py
├── producto.py
├── inventario.py
├── cola.py
├── repository.py
├── productos.json
├── requirements.txt
├── pytest.ini
├── README.md
│
└── tests/
    ├── test_cola.py
    ├── test_repository.py
    └── test_inventario.py
```

---

## Clases Implementadas

### Clase Producto

Clase base utilizada para representar un producto dentro del inventario.

Atributos:

- Código
- Nombre
- Precio
- Stock

Implementa encapsulación mediante propiedades (getters y setters) para validar la información almacenada.

---

### Clase ProductoElectronico

Hereda de la clase Producto.

Representa productos electrónicos y redefine la propiedad tipo.

---

### Clase ProductoAlimenticio

Hereda de la clase Producto.

Representa productos alimenticios y redefine la propiedad tipo.

---

### Clase Inventario

Administra todos los productos registrados.

Funciones principales:

- Agregar productos.
- Buscar productos.
- Actualizar productos.
- Actualizar stock.
- Eliminar productos.
- Gestionar la cola de reposición.
- Coordinar la persistencia utilizando Repository.

---

### Clase Cola

Implementa una cola FIFO (First In, First Out) mediante nodos enlazados.

La cola es utilizada para gestionar productos pendientes de reposición.

Operaciones implementadas:

- Agregar elementos.
- Eliminar elementos.
- Consultar siguiente elemento.
- Verificar si está vacía.
- Obtener cantidad de elementos.

---

### Clase JsonProductoRepository

Implementa el patrón Repository.

Su responsabilidad es almacenar y recuperar la información de productos desde el archivo JSON.

Permite separar la lógica de acceso a datos de la lógica de negocio del sistema.

---

## Interfaz Gráfica

La aplicación utiliza la librería Flet para proporcionar una interfaz gráfica moderna e intuitiva.

La interfaz incluye:

- Registro de productos.
- Búsqueda de productos.
- Actualización de datos.
- Eliminación de productos.
- Visualización de productos mediante tabla.
- Administración de cola de reposición.
- Mensajes informativos y validaciones.

---

## Persistencia de Datos

La persistencia se implementa mediante un archivo JSON.

Archivo utilizado:

```text
productos.json
```

Características:

- Los productos se guardan automáticamente.
- La información se recupera al iniciar la aplicación.
- Los datos permanecen disponibles después de cerrar el programa.

---

## Implementación de Cola FIFO

Para cumplir los requisitos de la asignatura se implementó manualmente una cola mediante nodos enlazados.

No se utilizaron estructuras de cola proporcionadas por bibliotecas externas.

La cola administra los productos pendientes de reposición.

Principio utilizado:

```text
FIFO
First In - First Out
Primero en entrar, primero en salir
```

Operaciones implementadas:

```python
agregar()
eliminar()
consultar_siguiente()
esta_vacia()
obtener_cantidad()
```

---

## Patrón de Diseño Repository

Se implementó el patrón Repository para desacoplar el acceso a los datos de la lógica principal.

Ventajas:

- Separación de responsabilidades.
- Mayor mantenibilidad.
- Facilita reemplazar JSON por base de datos en el futuro.
- Mejora la escalabilidad del sistema.

Clases involucradas:

- ProductoRepository
- JsonProductoRepository

---

## Conceptos de Programación Aplicados

### Programación Orientada a Objetos

La solución se estructura mediante clases y objetos.

### Encapsulación

Uso de atributos privados y propiedades para controlar el acceso a los datos.

Atributos encapsulados:

```python
__codigo
__nombre
__precio
__stock
```

### Herencia

Las clases:

- ProductoElectronico
- ProductoAlimenticio

heredan de:

```python
Producto
```

### Polimorfismo

Las clases derivadas redefinen la propiedad:

```python
tipo
```

permitiendo comportamientos específicos según el tipo de producto.

### Composición

La clase Inventario contiene una colección de objetos Producto.

### Manejo de Excepciones

Se utilizan bloques:

```python
try
except
```

para controlar errores y validar la información ingresada.

### CRUD

Operaciones implementadas:

- Crear.
- Consultar.
- Actualizar.
- Eliminar.

### Estructuras de Datos

#### Lista

```python
self.productos = []
```

Permite almacenar todos los productos.

#### Diccionario

```python
self.productos_por_codigo = {}
```

Permite búsquedas rápidas por código.

#### Set

```python
self.codigos_registrados = set()
```

Evita registros duplicados.

#### Cola FIFO

Implementada manualmente en:

```python
cola.py
```

para gestionar productos pendientes de reposición.

---

## Testing Unitario

Las pruebas unitarias fueron desarrolladas utilizando pytest.

Se validan:

### Cola

- Agregar elementos.
- Eliminar elementos.
- FIFO.
- Cola vacía.
- Consulta de elementos.

### Repository

- Guardar productos.
- Recuperar productos.
- Archivo inexistente.
- Archivo vacío.

### Inventario

- CRUD completo.
- Validación de códigos duplicados.
- Gestión de la cola.
- Persistencia de información.

---

## Tecnologías Utilizadas

- Python 3
- Flet
- JSON
- Pytest
- Programación Orientada a Objetos
- Patrón Repository

---

## Instalación

Crear y activar un entorno virtual:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución

Ejecutar la aplicación:

```bash
python main.py
```

---

## Ejecución de Pruebas

Ejecutar las pruebas unitarias:

```bash
pytest -v
```

---

## Ejemplo de Uso

1. Iniciar la aplicación.
2. Registrar un producto.
3. Visualizar el producto en la tabla.
4. Buscar un producto mediante su código.
5. Actualizar información.
6. Eliminar productos cuando sea necesario.
7. Enviar productos a la cola de reposición.
8. Atender productos pendientes según el orden FIFO.
9. Cerrar y volver a abrir la aplicación para verificar la persistencia de datos.

---

## Conclusión

Este proyecto permitió aplicar de forma práctica diversos conceptos fundamentales de Programación Orientada a Objetos, estructuras de datos lineales, patrones de diseño y pruebas unitarias.

Se desarrolló una solución completa para la gestión de inventario incorporando persistencia mediante JSON, una interfaz gráfica creada con Flet, una cola FIFO implementada manualmente y el patrón Repository para la administración de datos.

La aplicación cumple con los requisitos académicos establecidos y proporciona una solución funcional, organizada y escalable para la administración de productos.

---

## Lenguaje Utilizado

Python

---

## Autor

Leonardo Guzhñay