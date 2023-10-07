class BaseAction:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        self.name = name

    def __gt__(self, other):
        if self.name == 'Rock':
            if other.name == 'Scissors':
                return True
            else:
                return False
        elif self.name == 'Scissors':
            if other.name == 'Paper':
                return True
            else:
                return False
        elif self.name == 'Paper':
            if other.name == 'Rock':
                return True
            else:
                return False


class NothingAction(BaseAction):
    def __init__(self):
        super().__init__('Nothing')


class RockAction(BaseAction):
    def __init__(self):
        super().__init__('Rock')


class PaperAction(BaseAction):
    def __init__(self):
        super().__init__('Paper')


class ScissorsAction(BaseAction):
    def __init__(self):
        super().__init__('Scissors')
