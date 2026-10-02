class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Cola:
    """
    Cola FIFO implementada manualmente mediante nodos enlazados.

    FIFO significa:
    First In, First Out.
    El primero en entrar es el primero en salir.
    """

    def __init__(self):
        self.frente = None
        self.final = None
        self.cantidad = 0

    def agregar(self, elemento):
        nuevo_nodo = Nodo(elemento)

        if self.esta_vacia():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo

        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

        self.cantidad += 1

    def eliminar(self):
        if self.esta_vacia():
            raise IndexError(
                "No se puede eliminar de una cola vacía."
            )

        elemento = self.frente.dato
        self.frente = self.frente.siguiente
        self.cantidad -= 1

        if self.frente is None:
            self.final = None

        return elemento

    def consultar_siguiente(self):
        if self.esta_vacia():
            raise IndexError(
                "No existen elementos en la cola."
            )

        return self.frente.dato

    def esta_vacia(self):
        return self.frente is None

    def obtener_cantidad(self):
        return self.cantidad

    def contiene(self, condicion):
        actual = self.frente

        while actual is not None:
            if condicion(actual.dato):
                return True

            actual = actual.siguiente

        return False

    def obtener_elementos(self):
        elementos = []
        actual = self.frente

        while actual is not None:
            elementos.append(actual.dato)
            actual = actual.siguiente

        return elementos

    def eliminar_si(self, condicion):
        elementos_conservados = []

        while not self.esta_vacia():
            elemento = self.eliminar()

            if not condicion(elemento):
                elementos_conservados.append(elemento)

        for elemento in elementos_conservados:
            self.agregar(elemento)