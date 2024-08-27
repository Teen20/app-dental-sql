from model.database import get_connection

class Productos:
    def __init__(self, idproducto, nombre, idpresentacion, idcapacidad, idcategoria, precio, stock):
        self.idproducto = idproducto
        self.nombre = nombre
        self.idpresentacion = idpresentacion
        self.idcapacidad = idcapacidad
        self.idcategoria = idcategoria
        self.precio = precio
        self.stock = stock


    @staticmethod
    def fetch_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT idproducto, nombre, idpresentacion, idcapacidad, idcategoria, precio, stock FROM producto order by nombre asc")
        rows = cursor.fetchall()
        products = [Productos(*row) for row in rows]
        conn.close()        
        return products


    @staticmethod
    def create(idproducto, nombre, idpresentacion, idcapacidad, idcategoria, precio, stock):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO producto (idproducto, nombre, idpresentacion, idcapacidad, idcategoria, precio, stock) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (idproducto, nombre, idpresentacion, idcapacidad, idcategoria, precio, stock))
        conn.commit()
        conn.close()

    @staticmethod
    def update(idproducto, nombre, idpresentacion, idcapacidad, idcategoria, precio, stock):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE producto SET nombre = ?, idpresentacion = ?, idcapacidad = ?, idcategoria = ?, precio = ?, stock = ? WHERE idproducto = ?",
                    (nombre, idpresentacion, idcapacidad, idcategoria, precio, stock, idproducto))
        conn.commit()
        conn.close()

    @staticmethod
    def search(idproducto):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT idproducto, nombre, idpresentacion, idcapacidad, idcategoria, precio, stock FROM producto WHERE idproducto = ? order by nombre asc", (idproducto,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Productos(*row)
        return None
