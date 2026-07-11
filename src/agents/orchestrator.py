from src.services.context_loader import ContextLoader
from src.parsers.context_parser import ContextParser


class PMOrchestrator:

    def identify_current_activity(self):

        context = ContextLoader.load_context()

        state = ContextParser.parse(context)

        return state