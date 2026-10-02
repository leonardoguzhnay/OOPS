from producto import (
    ProductoElectronico,
    ProductoAlimenticio,
)

from repository import JsonProductoRepository


def test_guardar_y_recuperar_productos(
    tmp_path,
):
    ruta = tmp_path / "productos_prueba.json"

    repository = JsonProductoRepository(
        ruta
    )

    productos_originales = [
        ProductoElectronico(
            1001,
            "Laptop Dell",
            1200.00,
            10,
        ),
        ProductoAlimenticio(
            2001,
            "Arroz integral",
            2.50,
            30,
        ),
    ]

    repository.guardar_todos(
        productos_originales
    )

    productos_recuperados = (
        repository.obtener_todos()
    )

    assert len(productos_recuperados) == 2

    assert (
        productos_recuperados[0].codigo
        == 1001
    )

    assert (
        productos_recuperados[0].tipo
        == "Electrónico"
    )

    assert (
        productos_recuperados[1].codigo
        == 2001
    )

    assert (
        productos_recuperados[1].tipo
        == "Alimenticio"
    )


def test_archivo_inexistente(
    tmp_path,
):
    ruta = tmp_path / "no_existe.json"

    repository = JsonProductoRepository(
        ruta
    )

    productos = repository.obtener_todos()

    assert productos == []


def test_archivo_vacio(
    tmp_path,
):
    ruta = tmp_path / "archivo_vacio.json"

    ruta.write_text(
        "",
        encoding="utf-8",
    )

    repository = JsonProductoRepository(
        ruta
    )

    productos = repository.obtener_todos()

    assert productos == []