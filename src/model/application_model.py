from src.lib.dispatcher import Dispatcher

class ApplicationModel(Dispatcher):
  _instance = None

  EVENT_ADD_COURSE = "event.application_model.add_course"

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super().__new__(
                          cls, *args, **kwargs)
    return cls._instance

  def init(self):
    print("==Initializing model.")

  def add_course(self):
    self.notify_observers(ApplicationModel.EVENT_ADD_COURSE)
