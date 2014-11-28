from PyQt5.QtWidgets import QDialog

class NewCourseDialog(QDialog):
  def __init__(self, *args, **kwargs):
    super().__init__(kwargs['main_window'])
    #self.setParent(kwargs['main_window'])
    self.setModal(True)
    self.show()
    #self.setVisible(True)
