from model.application_model import ApplicationModel
from view.windows.main_window import MainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':

    # model
    app_model = ApplicationModel()
    app_model.init()

    # view 
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())