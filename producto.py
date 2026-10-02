class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError(
                "El código debe ser un número entero mayor que cero."
            )

        self.__codigo = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str):
            raise ValueError(
                "El nombre debe ser una cadena de texto."
            )

        valor = valor.strip()

        if len(valor) < 3:
            raise ValueError(
                "El nombre debe tener mínimo 3 caracteres."
            )

        self.__nombre = valor

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        try:
            valor = float(valor)

        except (TypeError, ValueError) as error:
            raise ValueError(
                "El precio debe ser un número válido."
            ) from error

        if valor <= 0:
            raise ValueError(
                "El precio debe ser mayor que cero."
            )

        self.__precio = valor

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError(
                "El stock debe ser un número entero no negativo."
            )

        self.__stock = valor

    @property
    def tipo(self):
        return "Producto"

    def mostrar_info(self):
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock} | "
            f"Tipo: {self.tipo}"
        )


class ProductoElectronico(Producto):
    @property
    def tipo(self):
        return "Electrónico"


class ProductoAlimenticio(Producto):
    @property
    def tipo(self):
        return "Alimenticio"