from API import IModerator
from API.Loader import Loader
from Core.Core import Core
from GUI.GUI import GUI
from GUI2.GUI2 import GUI2
from Notification.Notification import Notification


class Orchestrator(IModerator.IModerator):
    def moderate(self):
        loader_back = Loader('Orchestrator/Back/dist')
        loader_front = Loader('Orchestrator/Front/dist')
        core = Core()
        core.verify_rulers()
        gui = GUI()
        gui.get_data()
        gui.show()
        gui2 = GUI2()
        gui2.get_data()
        gui2.show()
        notification = Notification()
        notification.notify()
o = Orchestrator()
o.moderate()