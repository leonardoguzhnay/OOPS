import json

from abc import ABC, abstractmethod
from pathlib import Path

from producto import (
    ProductoElectronico,
    ProductoAlimenticio,
)


class ProductoRepository(ABC):
    @abstractmethod
    def obtener_todos(self):
        pass

    @abstractmethod
    def guardar_todos(self, productos):
        pass


class JsonProductoRepository(ProductoRepository):
    def __init__(self, ruta_archivo=None):
        if ruta_archivo is None:
            self.archivo = (
                Path(__file__).resolve().parent
                / "productos.json"
            )

        else:
            self.archivo = Path(ruta_archivo)

    def obtener_todos(self):
        if not self.archivo.exists():
            return []

        try:
            contenido = self.archivo.read_text(
                encoding="utf-8"
            ).strip()

            if not contenido:
                return []

            datos = json.loads(contenido)

            if not isinstance(datos, list):
                raise ValueError(
                    "El contenido del archivo JSON "
                    "debe ser una lista."
                )

            productos = []

            for dato in datos:
                producto = self._crear_producto(dato)
                productos.append(producto)

            return productos

        except json.JSONDecodeError as error:
            raise ValueError(
                "El archivo productos.json tiene "
                "un formato incorrecto."
            ) from error

        except KeyError as error:
            raise ValueError(
                f"Falta el campo obligatorio: {error}."
            ) from error

        except OSError as error:
            raise OSError(
                "No se pudieron recuperar los productos: "
                f"{error}"
            ) from error

    def guardar_todos(self, productos):
        datos = []

        for producto in productos:
            datos.append(
                {
                    "codigo": producto.codigo,
                    "nombre": producto.nombre,
                    "precio": producto.precio,
                    "stock": producto.stock,
                    "tipo": producto.tipo,
                }
            )

        try:
            self.archivo.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            contenido = json.dumps(
                datos,
                ensure_ascii=False,
                indent=4,
            )

            self.archivo.write_text(
                contenido,
                encoding="utf-8",
            )

        except OSError as error:
            raise OSError(
                "No se pudieron guardar los productos: "
                f"{error}"
            ) from error

    def _crear_producto(self, dato):
        codigo = int(dato["codigo"])
        nombre = str(dato["nombre"])
        precio = float(dato["precio"])
        stock = int(dato["stock"])
        tipo = dato["tipo"]

        if tipo == "Electrónico":
            return ProductoElectronico(
                codigo,
                nombre,
                precio,
                stock,
            )

        if tipo == "Alimenticio":
            return ProductoAlimenticio(
                codigo,
                nombre,
                precio,
                stock,
            )

        raise ValueError(
            f"El tipo de producto '{tipo}' no es válido."
        )