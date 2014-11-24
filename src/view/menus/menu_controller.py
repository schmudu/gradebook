from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QKeySequence

class MenuController  :
  _instance = None

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      if('main_window' in kwargs):
        cls._instance = super().__new__(cls)
        cls._instance.main_window = kwargs['main_window']
        return cls._instance
      else:
        raise ValueError("MenuController must be passed a reference to tkinter.Tk() for initialization")
    else:
      if(bool(kwargs) == False):
        return cls._instance
      else:
        raise ValueError("MenuController does not need to be passed arguments after initialization.")

  def __init__(self, *args, **kwargs):
    self.newAct = QAction("&New", self.main_window, shortcut=QKeySequence.New,
    statusTip="Create a new file", triggered=self.new_file)
    self.file_menu = self.main_window.menuBar().addMenu("&File")
    print("==main window:{0}".format(self.main_window))
    self.file_menu.addAction(self.newAct)

  def new_file(self):
    print("new file invoked")