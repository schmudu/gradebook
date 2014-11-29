from PyQt5.QtWidgets import QBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton, QDialog, QWidget

class NewCourseDialog(QDialog):
  def __init__(self, *args, **kwargs):
    # set parent
    super().__init__(kwargs['main_window'])

    self.setModal(True)
    self.show()
    
    self.setWindowTitle("New Course")

    self.setFixedSize(300, 200)

    # main widget
    #main_widget = QWidget()
    main_layout = QBoxLayout(QBoxLayout.TopToBottom, self)

    # form widget
    form_widget = QWidget()
    form_layout = QFormLayout()
    new_course_label = QLabel("Course Name:")
    new_course_entry = QLineEdit()
    form_layout.addRow(new_course_label, new_course_entry)
    form_widget.setLayout(form_layout)

    # action buttons
    action_widget = QWidget()
    add_course_button = QPushButton("Add Course")
    cancel_button = QPushButton("Cancel")
    action_layout = QBoxLayout(QBoxLayout.LeftToRight)
    action_layout.addWidget(add_course_button)
    action_layout.addWidget(cancel_button)
    action_widget.setLayout(action_layout)

    # add widgets
    main_layout.addWidget(form_widget)
    main_layout.addWidget(action_widget)
    self.setLayout(main_layout)
    #self.addWidget(main_widget)


