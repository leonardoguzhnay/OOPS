import pytest

from cola import Cola


def test_cola_inicia_vacia():
    cola = Cola()

    assert cola.esta_vacia() is True
    assert cola.obtener_cantidad() == 0


def test_agregar_elementos():
    cola = Cola()

    cola.agregar("Laptop")
    cola.agregar("Monitor")

    assert cola.esta_vacia() is False
    assert cola.obtener_cantidad() == 2
    assert cola.consultar_siguiente() == "Laptop"


def test_eliminar_elemento():
    cola = Cola()

    cola.agregar("Laptop")

    elemento = cola.eliminar()

    assert elemento == "Laptop"
    assert cola.esta_vacia() is True
    assert cola.obtener_cantidad() == 0


def test_cola_respeta_orden_fifo():
    cola = Cola()

    cola.agregar("Laptop")
    cola.agregar("Monitor")
    cola.agregar("Teclado")

    assert cola.eliminar() == "Laptop"
    assert cola.eliminar() == "Monitor"
    assert cola.eliminar() == "Teclado"


def test_consultar_no_elimina():
    cola = Cola()

    cola.agregar("Laptop")

    assert cola.consultar_siguiente() == "Laptop"
    assert cola.obtener_cantidad() == 1


def test_eliminar_cola_vacia():
    cola = Cola()

    with pytest.raises(IndexError):
        cola.eliminar()


def test_consultar_cola_vacia():
    cola = Cola()

    with pytest.raises(IndexError):
        cola.consultar_siguiente()


def test_eliminar_segun_condicion():
    cola = Cola()

    cola.agregar(1001)
    cola.agregar(1002)
    cola.agregar(1003)

    cola.eliminar_si(
        lambda codigo: codigo == 1002
    )

    assert cola.obtener_elementos() == [
        1001,
        1003,
    ]

    assert cola.obtener_cantidad() == 2