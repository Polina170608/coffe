import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.show)

    def show(self):
        self.con = sqlite3.connect('coffe.sqlite')
        cur = self.con.cursor()
        req = (f"SELECT * FROM information")
        self.result = cur.execute(req).fetchall()
        self.textEdit.setText(self.result)

    def closeEvent(self, event):
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
