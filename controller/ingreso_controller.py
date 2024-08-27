from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from views.product_management_view import ProductManagementView
from model.product import Productos
import openpyxl
from PyQt5.QtWidgets import QFileDialog

class IngresoController:
    def __init__(self):
        self.view = ProductManagementView()
        self.load_product()
        self.view.addButton.clicked.connect(self.add_product)
        self.view.salidaButton.clicked.connect(self.salida_product)
        self.view.editButton.clicked.connect(self.update_product)
        self.view.BuscarButton.clicked.connect(self.search_product)
        self.view.newButton.clicked.connect(self.clear_fields)
        self.view.productTable.cellClicked.connect(self.on_table_cell_clicked)
        self.view.btnSalir.clicked.connect(self.salir)
        self.view.reporte.clicked.connect(self.generate_report)



    def salir(self):
        self.view.close()

    def load_product(self):
        products = Productos.fetch_all()

        self.view.productTable.setRowCount(0)
        for product in products:
            rowPosition = self.view.productTable.rowCount()
            self.view.productTable.insertRow(rowPosition)
            self.view.productTable.setItem(rowPosition, 0, QTableWidgetItem(str(product.idproducto)))
            self.view.productTable.setItem(rowPosition, 1, QTableWidgetItem(product.nombre))
            self.view.productTable.setItem(rowPosition, 2, QTableWidgetItem(str(product.idpresentacion)))
            self.view.productTable.setItem(rowPosition, 3, QTableWidgetItem(str(product.idcapacidad)))
            self.view.productTable.setItem(rowPosition, 4, QTableWidgetItem(str(product.idcategoria)))
            self.view.productTable.setItem(rowPosition, 5, QTableWidgetItem(str(product.precio)))
            self.view.productTable.setItem(rowPosition, 6, QTableWidgetItem(str(product.stock)))

    def add_product(self):
        try:
            idproducto = self.view.idproductoInput.text()
            nombre = self.view.nombreInput.text()
            idpresentacion = self.view.idpresentacionInput.text()
            idcapacidad = self.view.idcapacidadInput.text()
            idcategoria = self.view.idcategoriaInput.text()
            precio = float(self.view.precioInput.text())  
            stock = int(self.view.stockInput.text())      

            Productos.create(idproducto, nombre, idpresentacion, idcapacidad, idcategoria, precio, stock)
            QMessageBox.information(self.view, "Sistema", "Producto agregado con éxito")
            self.load_product()
        except ValueError:
            QMessageBox.warning(self.view, "Error de Datos", "Favor de ingresar el dato correctamente")

    def salida_product(self):
        try:
            idproducto = self.view.idproductoInput.text()
            nombre = self.view.nombreInput.text()
            cantidad_salida = int(self.view.stockInput.text())  
            
            producto = Productos.search(idproducto)
            if producto:
                stock_actual = producto.stock
                
                if cantidad_salida > stock_actual:
                    QMessageBox.warning(self.view, "Error de Stock", "La cantidad de salida es mayor que el stock actual.")
                    return
                  
                nuevo_stock = stock_actual - cantidad_salida
                
                Productos.update(idproducto, nombre, producto.idpresentacion, producto.idcapacidad, producto.idcategoria, producto.precio, nuevo_stock)
                QMessageBox.information(self.view, "Sistema", "Stock actualizado con éxito")
                self.load_product()
            else:
                QMessageBox.warning(self.view, "Error", "Producto no encontrado.")
        except ValueError:
            QMessageBox.warning(self.view, "Error de Datos", "Favor de ingresar la cantidad correctamente.")
    def update_product(self):
        try:
            idproducto = self.view.idproductoInput.text()
            nombre = self.view.nombreInput.text()
            idpresentacion = self.view.idpresentacionInput.text()
            idcapacidad = self.view.idcapacidadInput.text()
            idcategoria = self.view.idcategoriaInput.text()
            precio = float(self.view.precioInput.text())  
            stock = int(self.view.stockInput.text())      
            Productos.update(idproducto, nombre, idpresentacion, idcapacidad, idcategoria, precio, stock)
            QMessageBox.information(self.view, "Sistema", "Producto actualizado con éxito")
            self.load_product()
        except ValueError:
            QMessageBox.warning(self.view, "Error de Datos", "Favor de ingresar el dato correctamente")

    def delete_product(self):
        idproducto = self.view.idproductoInput.text()
        Productos.delete(idproducto)
        QMessageBox.information(self.view, "Éxito", "Producto eliminado con éxito")
        self.load_product()

    def search_product(self):
        idproducto = self.view.idproductoInput.text()
        product = Productos.search(idproducto)
        if product:
            self.view.idproductoInput.setText(str(product.idproducto))  
            self.view.nombreInput.setText(product.nombre)
            self.view.idpresentacionInput.setText(str(product.idpresentacion))  
            self.view.idcapacidadInput.setText(str(product.idcapacidad))  
            self.view.idcategoriaInput.setText(str(product.idcategoria)) 
            self.view.precioInput.setText(str(product.precio))  
            self.view.stockInput.setText(str(product.stock))  
            QMessageBox.information(self.view, "Encontrado", "Producto encontrado")
        else:
            QMessageBox.warning(self.view, "No Encontrado", "Producto no encontrado")

    def clear_fields(self):
        self.view.idproductoInput.clear()
        self.view.nombreInput.clear()
        self.view.idpresentacionInput.clear()
        self.view.idcapacidadInput.clear()
        self.view.idcategoriaInput.clear()
        self.view.precioInput.clear()
        self.view.stockInput.clear()

    def on_table_cell_clicked(self, row, column):
        idproducto = self.view.productTable.item(row, 0).text()
        nombre = self.view.productTable.item(row, 1).text()
        idpresentacion = self.view.productTable.item(row, 2).text()
        idcapacidad = self.view.productTable.item(row, 3).text()
        idcategoria = self.view.productTable.item(row, 4).text()
        precio = self.view.productTable.item(row, 5).text()
        stock = self.view.productTable.item(row, 6).text()
        self.view.idproductoInput.setText(idproducto)
        self.view.nombreInput.setText(nombre)
        self.view.idpresentacionInput.setText(idpresentacion)
        self.view.idcapacidadInput.setText(idcapacidad)
        self.view.idcategoriaInput.setText(idcategoria)
        self.view.precioInput.setText(precio)
        self.view.stockInput.setText(stock)
    def generate_report(self):
        try:
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(self.view, "Guardar Reporte", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
            if not file_path:
                return  

            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.title = "Reporte de Productos"
            headers = ["ID Producto", "Nombre", "ID Presentación", "ID Capacidad", "ID Categoría", "Precio", "Stock"]
            sheet.append(headers)
            products = Productos.fetch_all()
            for product in products:
                sheet.append([
                    product.idproducto,
                    product.nombre,
                    product.idpresentacion,
                    product.idcapacidad,
                    product.idcategoria,
                    product.precio,
                    product.stock
                ])
            workbook.save(file_path)
            QMessageBox.information(self.view, "Éxito", "Reporte generado con éxito")

        except Exception as e:
            QMessageBox.warning(self.view, "Error", f"Ocurrió un error al generar el reporte: {str(e)}")
