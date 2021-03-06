from PyQt5.QtWidgets import QAction
from view.windows.dialogs.new_course_dialog import NewCourseDialog

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
    self.course_menu.addAction(self.new_course_action)

  def new_course_selected(self):
    print("new course invoked")
    NewCourseDialog(main_window=self.main_window)

  def _create_actions(self):
    self.new_course_action = QAction("New Course", self.main_window,
      statusTip="Create a new course", triggered=self.new_course_selected)
    self.new_course_action.setShortcut('Ctrl+C')

