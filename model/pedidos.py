from model.database import get_connection

class Pedidos:
    def __init__(self, idpedido, fecha_pedido, idcliente, idproducto, cantidad, nombre):
        self.idpedido = idpedido
        self.fecha_pedido = fecha_pedido
        self.idcliente = idcliente
        self.idproducto = idproducto
        self.cantidad = cantidad
        self.nombre = nombre

    @staticmethod
    def fetch_all():
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT idpedido, fecha_pedido, idcliente, idproducto, cantidad, nombre FROM pedido order by idpedido asc")
            rows = cursor.fetchall()
            return [Pedidos(*row) for row in rows]
        except Exception as e:
            print(f"Error al obtener los pedidos: {str(e)}")
            return []
        finally:
            if conn:
                conn.close()

    @staticmethod
    def create(idpedido, fecha_pedido, idcliente, idproducto, cantidad, nombre):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO pedido (idpedido, fecha_pedido, idcliente, idproducto, cantidad, nombre) 
                VALUES (?, ?, ?, ?, ?, ?)""",
                (idpedido, fecha_pedido, idcliente, idproducto, cantidad, nombre))
            conn.commit()

    @staticmethod
    def update(idpedido, fecha_pedido, idcliente, idproducto, cantidad, nombre):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE pedido 
                SET fecha_pedido = ?, idcliente = ?, idproducto = ?, cantidad = ?, nombre = ? 
                WHERE idpedido = ?""",
                (fecha_pedido, idcliente, idproducto, cantidad, nombre, idpedido))
            conn.commit()

    @staticmethod
    def search(idpedido):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT idpedido, fecha_pedido, idcliente, idproducto, cantidad, nombre FROM pedido WHERE idpedido = ?", (idpedido,))
            row = cursor.fetchone()
            if row:
                return Pedidos(*row)
            return None

    @staticmethod
    def delete(idpedido):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM pedido WHERE idpedido = ?", (idpedido,))
            conn.commit()
