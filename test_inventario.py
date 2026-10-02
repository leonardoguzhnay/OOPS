from inventario import Inventario

from producto import (
    ProductoElectronico,
    ProductoAlimenticio,
)


class RepositoryMemoria:
    def __init__(self):
        self.productos = []

    def obtener_todos(self):
        return list(self.productos)

    def guardar_todos(self, productos):
        self.productos = list(productos)


def test_agregar_producto():
    repository = RepositoryMemoria()
    inventario = Inventario(repository)

    producto = ProductoElectronico(
        1001,
        "Laptop Dell",
        1200.00,
        10,
    )

    resultado, mensaje = (
        inventario.agregar_producto(
            producto
        )
    )

    assert resultado is True

    assert (
        inventario.buscar_producto(1001)
        is producto
    )

    assert len(repository.productos) == 1


def test_no_permite_codigos_duplicados():
    repository = RepositoryMemoria()
    inventario = Inventario(repository)

    producto_uno = ProductoElectronico(
        1001,
        "Laptop Dell",
        1200.00,
        10,
    )

    producto_dos = ProductoElectronico(
        1001,
        "Monitor Dell",
        300.00,
        5,
    )

    inventario.agregar_producto(
        producto_uno
    )

    resultado, mensaje = (
        inventario.agregar_producto(
            producto_dos
        )
    )

    assert resultado is False

    assert mensaje == (
        "Ya existe un producto con ese código."
    )


def test_buscar_producto():
    repository = RepositoryMemoria()
    inventario = Inventario(repository)

    producto = ProductoAlimenticio(
        2001,
        "Arroz integral",
        2.50,
        30,
    )

    inventario.agregar_producto(
        producto
    )

    encontrado = (
        inventario.buscar_producto(2001)
    )

    assert encontrado is producto

    assert (
        encontrado.nombre
        == "Arroz integral"
    )


def test_actualizar_producto():
    repository = RepositoryMemoria()
    inventario = Inventario(repository)

    producto = ProductoElectronico(
        1001,
        "Laptop Dell",
        1200.00,
        10,
    )

    inventario.agregar_producto(
        producto
    )

    resultado, mensaje = (
        inventario.actualizar_producto(
            1001,
            "Laptop Lenovo",
            1300.00,
            15,
        )
    )

    actualizado = (
        inventario.buscar_producto(1001)
    )

    assert resultado is True

    assert (
        actualizado.nombre
        == "Laptop Lenovo"
    )

    assert actualizado.precio == 1300.00
    assert actualizado.stock == 15


def test_eliminar_producto():
    repository = RepositoryMemoria()
    inventario = Inventario(repository)

    producto = ProductoElectronico(
        1001,
        "Laptop Dell",
        1200.00,
        10,
    )

    inventario.agregar_producto(
        producto
    )

    resultado, mensaje = (
        inventario.eliminar_producto(
            1001
        )
    )

    assert resultado is True

    assert (
        inventario.buscar_producto(1001)
        is None
    )

    assert len(repository.productos) == 0


def test_producto_sin_stock_ingresa_cola():
    repository = RepositoryMemoria()
    inventario = Inventario(repository)

    producto = ProductoElectronico(
        1001,
        "Laptop Dell",
        1200.00,
        0,
    )

    inventario.agregar_producto(
        producto
    )

    siguiente = (
        inventario
        .consultar_siguiente_reposicion()
    )

    assert siguiente is producto

    assert (
        inventario.cantidad_reposiciones()
        == 1
    )


def test_cola_reposicion_respeta_fifo():
    repository = RepositoryMemoria()
    inventario = Inventario(repository)

    producto_uno = ProductoElectronico(
        1001,
        "Laptop Dell",
        1200.00,
        0,
    )

    producto_dos = ProductoElectronico(
        1002,
        "Monitor Dell",
        300.00,
        0,
    )

    inventario.agregar_producto(
        producto_uno
    )

    inventario.agregar_producto(
        producto_dos
    )

    siguiente = (
        inventario
        .consultar_siguiente_reposicion()
    )

    assert siguiente is producto_uno

    inventario.atender_siguiente_reposicion()

    siguiente = (
        inventario
        .consultar_siguiente_reposicion()
    )

    assert siguiente is producto_dos


def test_no_duplica_producto_en_cola():
    repository = RepositoryMemoria()
    inventario = Inventario(repository)

    producto = ProductoElectronico(
        1001,
        "Laptop Dell",
        1200.00,
        0,
    )

    inventario.agregar_producto(
        producto
    )

    resultado, mensaje = (
        inventario.encolar_reposicion(
            1001
        )
    )

    assert resultado is False

    assert (
        inventario.cantidad_reposiciones()
        == 1
    )


def test_actualizar_stock_retira_de_cola():
    repository = RepositoryMemoria()
    inventario = Inventario(repository)

    producto = ProductoElectronico(
        1001,
        "Laptop Dell",
        1200.00,
        0,
    )

    inventario.agregar_producto(
        producto
    )

    inventario.actualizar_stock(
        1001,
        10,
    )

    assert (
        inventario.cola_reposicion_vacia()
        is True
    )

    assert (
        inventario.cantidad_reposiciones()
        == 0
    )