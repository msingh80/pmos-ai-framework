from src.services.context_loader import ContextLoader
from src.parsers.context_parser import ContextParser
from src.agents.agent_factory import AgentFactory


class PMOrchestrator:

    def identify_current_activity(self):

        context = ContextLoader.load_context()

        state = ContextParser.parse(context)

        return state

    def run(self):

        state = self.identify_current_activity()

        
        agent = AgentFactory.get_agent(state.current_phase.strip())

        

        if agent:
            agent.execute(state)
        else:
            print("No Agent Found!")

        return state