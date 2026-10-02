from cola import Cola


class Inventario:
    def __init__(self, repository):
        self.repository = repository

        # Lista para almacenar y mostrar productos.
        self.productos = []

        # Diccionario para buscar productos por código.
        self.productos_por_codigo = {}

        # Set para evitar códigos duplicados.
        self.codigos_registrados = set()

        # Cola manual de productos pendientes de reposición.
        self.cola_reposicion = Cola()

        self.cargar_datos()

    def cargar_datos(self):
        productos_recuperados = (
            self.repository.obtener_todos()
        )

        for producto in productos_recuperados:
            if producto.codigo not in self.codigos_registrados:
                self._registrar_en_memoria(producto)

                if producto.stock == 0:
                    self.cola_reposicion.agregar(producto)

    def _registrar_en_memoria(self, producto):
        self.productos.append(producto)

        self.productos_por_codigo[
            producto.codigo
        ] = producto

        self.codigos_registrados.add(
            producto.codigo
        )

    def _guardar_cambios(self):
        self.repository.guardar_todos(
            self.productos
        )

    def agregar_producto(self, producto):
        if producto.codigo in self.codigos_registrados:
            return (
                False,
                "Ya existe un producto con ese código.",
            )

        self._registrar_en_memoria(producto)

        try:
            self._guardar_cambios()

            if producto.stock == 0:
                self.encolar_reposicion(
                    producto.codigo
                )

            return (
                True,
                "Producto agregado y guardado correctamente.",
            )

        except OSError as error:
            self.productos.remove(producto)

            del self.productos_por_codigo[
                producto.codigo
            ]

            self.codigos_registrados.remove(
                producto.codigo
            )

            return False, str(error)

    def listar_productos(self):
        return list(self.productos)

    def buscar_producto(self, codigo):
        return self.productos_por_codigo.get(
            codigo
        )

    def actualizar_producto(
        self,
        codigo,
        nuevo_nombre,
        nuevo_precio,
        nuevo_stock,
    ):
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False, "Producto no encontrado."

        nombre_anterior = producto.nombre
        precio_anterior = producto.precio
        stock_anterior = producto.stock

        try:
            producto.nombre = nuevo_nombre
            producto.precio = nuevo_precio
            producto.stock = nuevo_stock

            self._guardar_cambios()

            if nuevo_stock == 0:
                self.encolar_reposicion(codigo)

            else:
                self.retirar_de_reposicion(codigo)

            return (
                True,
                "Producto actualizado y guardado correctamente.",
            )

        except (ValueError, OSError) as error:
            producto.nombre = nombre_anterior
            producto.precio = precio_anterior
            producto.stock = stock_anterior

            return False, str(error)

    def actualizar_stock(
        self,
        codigo,
        nuevo_stock,
    ):
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False, "Producto no encontrado."

        stock_anterior = producto.stock

        try:
            producto.stock = nuevo_stock

            self._guardar_cambios()

            if nuevo_stock == 0:
                self.encolar_reposicion(codigo)

            else:
                self.retirar_de_reposicion(codigo)

            return (
                True,
                "Stock actualizado y guardado correctamente.",
            )

        except (ValueError, OSError) as error:
            producto.stock = stock_anterior

            return False, str(error)

    def eliminar_producto(self, codigo):
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False, "Producto no encontrado."

        posicion = self.productos.index(
            producto
        )

        self.productos.remove(producto)

        del self.productos_por_codigo[codigo]

        self.codigos_registrados.remove(codigo)

        try:
            self._guardar_cambios()

            self.retirar_de_reposicion(codigo)

            return (
                True,
                "Producto eliminado correctamente.",
            )

        except OSError as error:
            self.productos.insert(
                posicion,
                producto,
            )

            self.productos_por_codigo[
                codigo
            ] = producto

            self.codigos_registrados.add(codigo)

            return False, str(error)

    # OPERACIONES DE LA COLA

    def encolar_reposicion(self, codigo):
        producto = self.buscar_producto(codigo)

        if producto is None:
            return False, "Producto no encontrado."

        ya_esta_encolado = (
            self.cola_reposicion.contiene(
                lambda elemento:
                elemento.codigo == codigo
            )
        )

        if ya_esta_encolado:
            return (
                False,
                "El producto ya está pendiente "
                "de reposición.",
            )

        self.cola_reposicion.agregar(
            producto
        )

        return (
            True,
            "Producto enviado a la cola de reposición.",
        )

    def atender_siguiente_reposicion(self):
        if self.cola_reposicion.esta_vacia():
            return (
                False,
                "No existen productos pendientes "
                "de reposición.",
            )

        producto = self.cola_reposicion.eliminar()

        return (
            True,
            f"Producto atendido: {producto.nombre}.",
        )

    def consultar_siguiente_reposicion(self):
        if self.cola_reposicion.esta_vacia():
            return None

        return (
            self.cola_reposicion
            .consultar_siguiente()
        )

    def listar_reposiciones(self):
        return (
            self.cola_reposicion
            .obtener_elementos()
        )

    def cantidad_reposiciones(self):
        return (
            self.cola_reposicion
            .obtener_cantidad()
        )

    def cola_reposicion_vacia(self):
        return (
            self.cola_reposicion
            .esta_vacia()
        )

    def retirar_de_reposicion(self, codigo):
        self.cola_reposicion.eliminar_si(
            lambda producto:
            producto.codigo == codigo
        )