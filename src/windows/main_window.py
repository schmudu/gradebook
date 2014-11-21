from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QKeySequence

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Hello")

    self.newAct = QAction("&New", self, shortcut=QKeySequence.New,
      statusTip="Create a new file", triggered=self.new_file)
    self.file_menu = self.menuBar().addMenu("&File")
    self.file_menu.addAction(self.newAct)

  def new_file(self):
    print("new file invoked")