
class ApplicationState:
    instance = None
    
    def __init__(self):
        self.isLoggedIn = False

    @staticmethod
    def getAppstate():
        
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState() 
        return ApplicationState.instance
        
appState1 = ApplicationState.getAppstate()
print(appState1.isLoggedIn)
appState1.isLoggedIn = True

appState2 = ApplicationState.getAppstate()
print(appState2.isLoggedIn)
print(appState1.isLoggedIn)

