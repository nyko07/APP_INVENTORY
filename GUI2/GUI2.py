from API import IOutput, IInput


class GUI2(IOutput.IOutput, IInput.IInput):
    def show(self):
        print("Soy salida de "+self.__class__.__name__)

    def get_data(self):
        print("Soy entrada de "+self.__class__.__name__)
