from game.action.action import Action

class Stage(Action):
    def __init__(self):
        super().__init__()
    
class RoundStartStage(Stage):
    def __init__(self):
        super().__init__()
        
class DrawCardStage(Stage):
    def __init__(self):
        super().__init__()

class DiscardStage(Stage):
    def __init__(self):
        super().__init__()

class RoundEndStage(Stage):
    def __init__(self):
        super().__init__()