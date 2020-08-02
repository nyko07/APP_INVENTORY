from API import INotifier


class Notification(INotifier.INotifier):
    def notify(self):
        print("Soy " + self.__class__.__name__)