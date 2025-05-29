class ClassroomNotExist(Exception):
    def init(self, message):
        self.message = message

class ClassroomAlreadyReserved(Exception):
    def init(self, message):
        self.message = message