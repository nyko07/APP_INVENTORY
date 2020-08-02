from API.Loader import Loader

loader_orchestrator = Loader('./Orchestrator/Orchestrator/dist')

try:
    from Orchestrator.Orchestrator import Orchestrator
    orchestrator = Orchestrator()
except Exception as e:
    print(e)




