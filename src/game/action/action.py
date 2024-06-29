from game.action.actionConfig import ActionConfig

class Action:
    def __init__(self):
        self.name = self.__class__.__name__
        self.monitorBefore = ActionConfig().getMonitorBefore(self.name)
        self.monitorAfter = ActionConfig().getMonitorAfter(self.name)
        
    def addMonitorBefore(self, monitor):
        self.monitorBefore.append(monitor)
        
    def addMonitorAfter(self, monitor):
        self.monitorAfter.append(monitor)
    
    def execute(self):
        self.executeMonitorBefore()
        self.effect()
        self.executeMonitorAfter()
        
    def effect(self):
        print(f"{self.name} works!")
        
    def executeMonitorBefore(self):
        for monitor in self.monitorBefore:
            monitor.execute()
            
    def executeMonitorAfter(self):
        for monitor in self.monitorAfter:
            monitor.execute()
        
        