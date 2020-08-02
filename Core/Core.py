from API import IRuler


class Core(IRuler.IRuler):
    def verify_rulers(self):
        print("Soy "+self.__class__.__name__)
