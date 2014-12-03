from PyQt5.QtWidgets import QLineEdit

class CustomLineEdit(QLineEdit):
  DEFAULT_ENTRY = "<Default Entry>"
  def __init__(self, *args, **kwargs):
    super().__init__()
    
    # set entry
    if ('default_entry' in kwargs):
      self.default_entry = kwargs.pop('default_entry')
    else:
      self.default_entry = CustomLineEdit.DEFAULT_ENTRY
    self.setText(self.default_entry)


