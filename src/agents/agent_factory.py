from src.agents.planning_agent import PlanningAgent
from src.agents.execution_agent import ExecutionAgent
from src.agents.monitoring_agent import MonitoringAgent
from src.agents.closure_agent import ClosureAgent


class AgentFactory:

    @staticmethod
    def get_agent(phase):

        agents = {

            "Initiation": PlanningAgent(),

            "Planning": PlanningAgent(),

            "Execution": ExecutionAgent(),

            "Monitoring": MonitoringAgent(),

            "Closure": ClosureAgent()
        }

        return agents.get(phase)