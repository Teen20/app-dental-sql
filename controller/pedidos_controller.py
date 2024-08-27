from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from views.pedidos_view import Pedidos_View 
from model.pedidos import Pedidos  
from datetime import datetime
from model.database import get_connection
import openpyxl
from PyQt5.QtWidgets import QFileDialog

class PedidosController:
    def __init__(self):
        self.view = Pedidos_View()
        self.load_product()
        self.view.addButton.clicked.connect(self.add_pedido)
        self.view.deleteButton.clicked.connect(self.delete_pedido)
        self.view.pedidosTable.cellClicked.connect(self.on_table_cell_clicked)
        self.view.btnSalir.clicked.connect(self.salir)
        self.view.reporte.clicked.connect(self.generate_report)

    def salir(self):
        self.view.close()

    def load_product(self):
        products = Pedidos.fetch_all()
        self.view.pedidosTable.setRowCount(0)
        for product in products:
            rowPosition = self.view.pedidosTable.rowCount()
            self.view.pedidosTable.insertRow(rowPosition)
            self.view.pedidosTable.setItem(rowPosition, 0, QTableWidgetItem(str(product.idpedido)))
            fecha_pedido_str = product.fecha_pedido.strftime("%Y-%m-%d") if product.fecha_pedido else ""
            self.view.pedidosTable.setItem(rowPosition, 1, QTableWidgetItem(fecha_pedido_str))
            self.view.pedidosTable.setItem(rowPosition, 2, QTableWidgetItem(str(product.idcliente)))
            self.view.pedidosTable.setItem(rowPosition, 3, QTableWidgetItem(str(product.idproducto)))
            self.view.pedidosTable.setItem(rowPosition, 4, QTableWidgetItem(str(product.nombre)))
            self.view.pedidosTable.setItem(rowPosition, 5, QTableWidgetItem(str(product.cantidad)))

    def add_pedido(self):
        try:
            idpedido = self.view.idpedidoInput.text()
            fecha_pedido = self.view.fechapedidoInput.text()
            idcliente = self.view.idclienteInput.text()
            idproducto = self.view.idproductoInput.text()
            nombre = self.view.nombreInput.text()
            cantidad = int(self.view.cantidadInput.text())
            try:
                fecha_pedido_dt = datetime.strptime(fecha_pedido, "%Y-%m-%d")
                fecha_pedido_str = fecha_pedido_dt.strftime("%Y-%m-%d")
            except ValueError:
                QMessageBox.warning(self.view, "Error de Datos", "La fecha debe estar en el formato YYYY-MM-DD")
                return

            Pedidos.create(idpedido, fecha_pedido_str, idcliente, idproducto, nombre, cantidad)
            QMessageBox.information(self.view, "Sistema", "Pedido agregado con éxito")
            self.load_product()
        except ValueError:
            QMessageBox.warning(self.view, "Error de Datos", "Favor de ingresar el dato correctamente")



    def delete_pedido(self):
        idpedido = self.view.idpedidoInput.text()
        Pedidos.delete(idpedido)
        QMessageBox.information(self.view, "Éxito", "Pedido eliminado con éxito")
        self.load_product()

    def clear_fields(self):
        self.view.idpedidoInput.clear()
        self.view.fechapedidoInput.clear()
        self.view.idclienteInput.clear()
        self.view.idproductoInput.clear()
        self.view.cantidadInput.clear()
        self.view.nombreInput.clear()
            
    def on_table_cell_clicked(self, row, column):
        idpedido = self.view.pedidosTable.item(row, 0).text()
        fecha_pedido = self.view.pedidosTable.item(row, 1).text()
        idcliente = self.view.pedidosTable.item(row, 2).text()
        idproducto = self.view.pedidosTable.item(row, 3).text()
        cantidad = self.view.pedidosTable.item(row, 4).text()  
        nombre = self.view.pedidosTable.item(row, 5).text()    


        self.view.idpedidoInput.setText(idpedido)
        self.view.fechapedidoInput.setText(fecha_pedido)
        self.view.idclienteInput.setText(idcliente)
        self.view.idproductoInput.setText(idproducto)
        self.view.cantidadInput.setText(cantidad)
        self.view.nombreInput.setText(nombre)
    def generate_report(self):
        try:

            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(self.view, "Guardar Reporte", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
            if not file_path:
                return 

            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.title = "Reporte de Pedidos"

            headers = ["ID Pedido", "Fecha de Pedido", "ID Cliente", "ID Producto", "Nombre Producto", "Cantidad"]
            sheet.append(headers)

            pedidos = Pedidos.fetch_all()
            for pedido in pedidos:
                fecha_pedido_str = pedido.fecha_pedido.strftime("%Y-%m-%d") if pedido.fecha_pedido else ""
                sheet.append([
                    pedido.idpedido,
                    fecha_pedido_str,
                    pedido.idcliente,
                    pedido.idproducto,
                    pedido.nombre,
                    pedido.cantidad
                ])
            workbook.save(file_path)
            QMessageBox.information(self.view, "Éxito", "Reporte de pedidos generado con éxito")

        except Exception as e:
            QMessageBox.warning(self.view, "Error", f"Ocurrió un error al generar el reporte: {str(e)}")