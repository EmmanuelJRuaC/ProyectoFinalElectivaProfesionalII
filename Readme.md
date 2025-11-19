# Modelo: Categoria
Representa el tipo o grupo al que pertenece un producto (Ej: Electrónica, Ropa, Hogar).
Cada categoría puede tener muchos productos.

### Atributos:
- Id: Identificador único.
- Nombre: Nombre de la categoría.


# Modelo: Producto
Contiene la información de cada artículo disponible en el marketplace.
Un producto pertenece a una sola categoría, pero una categoría puede tener múltiples productos.

### Atributos:
- Id: Identificador único.
- Nombre: Nombre del producto.
- Precio: Valor unitario del producto.
- Categoria (FK): Relación hacia la tabla Categoria.

# Modelo: Cliente
Modelo que almacena los datos de los usuarios que realizan pedidos.

### Atributos:
- Id: Identificador único.
- Nombre: Nombre del cliente.
- Email: Correo electrónico.
- Telefono: Número de contacto.

# Modelo: Pedido
Registra las compras realizadas dentro del sistema.
Un pedido está asociado a un cliente y también a un producto.

### Atributos:
- Id: Identificador único del pedido.
- Cliente (FK): Cliente que realiza el pedido.
- Producto (FK): Producto comprado.
- Cantidad: Número de unidades del producto adquiridas.
- Total: Valor total calculado (precio × cantidad).