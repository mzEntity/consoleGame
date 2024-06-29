from others.singleton import singleton
import copy

@singleton
class ActionConfig:
    def __init__(self):
        self.monitorBeforeConfigMap = dict()
        self.monitorAfterConfigMap = dict()
    
    def addMonitorBefore(self, actionName, monitor):
        self.monitorBeforeConfigMap.setdefault(actionName, [])
        self.monitorBeforeConfigMap[actionName].append(monitor)
        
    def addMonitorAfter(self, actionName, monitor):
        self.monitorAfterConfigMap.setdefault(actionName, [])
        self.monitorAfterConfigMap[actionName].append(monitor)       
    
    def getMonitorBefore(self, name):
        if name not in self.monitorBeforeConfigMap.keys():
            return []
        backup = self.monitorBeforeConfigMap[name]
        monitorBefore = []
        for monitor in backup:
            monitorBefore.append(copy.deepcopy(monitor))
        return monitorBefore
    
    def getMonitorAfter(self, name):
        if name not in self.monitorAfterConfigMap.keys():
            return []
        backup = self.monitorAfterConfigMap[name]
        monitorAfter = []
        for monitor in backup:
            monitorAfter.append(copy.deepcopy(monitor))
        return monitorAfter