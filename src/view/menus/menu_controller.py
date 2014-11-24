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
    self._create_actions()

    self.course_menu = self.main_window.menuBar().addMenu("&Course")
    self.course_menu.addAction(self.new_course)

  def new_course_selected(self):
    print("new course invoked")

  def _create_actions(self):
    self.new_course = QAction("&New Course", self.main_window, shortcut=QKeySequence.New,
      statusTip="Create a new course", triggered=self.new_course_selected)
