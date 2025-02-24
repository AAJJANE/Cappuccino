import sqlite3

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QTableWidgetItem, QMainWindow, QMessageBox, QWidget
from release.UI.add_edit_coffee_form_ui import Ui_AddCoffee
from release.UI.main_ui import Ui_qwidget


class CoffeeApp(QMainWindow, Ui_qwidget):
    def __init__(self):
        super(CoffeeApp, self).__init__()
        self.setupUi(self)
        self.load_data()

        self.addButton.clicked.connect(self.open_add_edit_form)

    def load_data(self):
        conn = sqlite3.connect('release/data/coffee.sqlite')
        cursor = conn.cursor()
        coffee_data = cursor.execute("SELECT * FROM info").fetchall()
        self.tableWidget.setRowCount(len(coffee_data))
        self.tableWidget.setColumnCount(len(coffee_data[0]))
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах(1/0)',
             'Описание вкуса', 'Цена', 'Объем упаковки'])
        for i, row in enumerate(coffee_data):
            for j, value in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))
        conn.close()

    def open_add_edit_form(self):
        try:
            self.add_edit_form = AddEditCoffeeForm()
            self.add_edit_form.show()
            self.destroy(True)
        except Exception as e:
            print(e)


class AddEditCoffeeForm(QWidget, Ui_AddCoffee):
    def __init__(self):
        super(AddEditCoffeeForm, self).__init__()
        self.setupUi(self)
        self.saveBtn.clicked.connect(self.save_data)
        self.main_win = None

    def save_data(self):
        conn = sqlite3.connect('release/data/coffee.sqlite')
        cursor = conn.cursor()
        name = self.sortLine.text()
        roast = self.roastCombo.currentText()
        ground = 1 if self.groundCheck.isChecked() else 0
        desc = self.descLine.text()
        price = self.priceLine.text()
        size = self.sizeCombo.currentText()
        from numpy._core.strings import isdigit
        if not isdigit(price):
            self.errorLine.setText("Введите число в строке цены!!!")
        else:
            try:
                if self.idLine.text() == '':
                    id = int(cursor.execute("SELECT COUNT(*) FROM info").fetchone()[0]) + 1
                    cursor.execute(
                        f"INSERT INTO info (id, sort, roasting, ground_grains, description, price, size)"
                                       f" VALUES ('{id}', '{name}', '{roast}', '{ground}', '{desc}', '{float(price)}', '{size}')")
                else:
                    if not isdigit(self.idLine.text()):
                        self.errorLine.setText("Введите число в строке ID!!!")
                    else:
                        id = int(self.idLine.text())
                        if id > int(cursor.execute("SELECT COUNT(*) FROM info").fetchone()[0]):
                            QMessageBox.about(self, "Error", "Невозможно обновить запись - её не существует!")
                        else:
                            cursor.execute("UPDATE info SET (id, sort, roasting, ground_grains, description, price, size)"
                                           f" = (SELECT'{id}', '{name}', '{roast}', '{ground}', '{desc}', '{float(price)}', '{size}') WHERE id = '{id}'",
                                )
            except Exception as e:
                print(e)
            conn.commit()
            conn.close()
            self.main_win = CoffeeApp()
            self.main_win.show()
            self.destroy()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = CoffeeApp()
    try:
        window.show()
        app.exec()
    except Exception as e:
        print(e)
