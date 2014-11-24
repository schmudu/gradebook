from PyQt5.QtWidgets import QMainWindow
from view.menus.menu_controller import MenuController

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Hello")

    MenuController(main_window=self)

