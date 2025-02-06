import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from MainWindow import Ui_MainWindow
from ProductClasses import OfficialProduct, NonOfficialProduct
from ProductManager import ProductManager


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.product_manager = ProductManager()

        # Connect buttons
        self.ui.pushButtonSave.clicked.connect(self.save_product)
        self.ui.pushButtonRemove.clicked.connect(self.remove_product)
        self.ui.pushButtonSearchName.clicked.connect(self.search_product)
        self.ui.pushButtonFilterPrice.clicked.connect(self.filter_products)

    def save_product(self):
        product_id = self.ui.lineEditId.text()
        name = self.ui.lineEditName.text()
        try:
            price = float(self.ui.lineEditPrice.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Price must be a number")
            return

        if self.ui.radioButtonOfficial.isChecked():
            product = OfficialProduct(product_id, name, price)
        else:
            product = NonOfficialProduct(product_id, name, price)

        self.product_manager.add_product(product)
        self.refresh_products()

    def remove_product(self):
        product_id = self.ui.lineEditId.text()
        self.product_manager.remove_product(product_id)
        self.refresh_products()

    def search_product(self):
        keyword = self.ui.lineEditName.text()
        products = self.product_manager.search_by_name(keyword)
        self.display_products(products)

    def filter_products(self):
        try:
            min_price = float(self.ui.lineEditPrice.text())
            max_price = float(self.ui.lineEditDiscount.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Price range must be numbers")
            return
        products = self.product_manager.filter_by_price(min_price, max_price)
        self.display_products(products)

    def refresh_products(self):
        self.display_products(self.product_manager.get_all_products())

    def display_products(self, products):
        self.ui.label_2.clear()
        for product in products:
            self.ui.label_2.setText(self.ui.label_2.text() + str(product) + '\n')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
