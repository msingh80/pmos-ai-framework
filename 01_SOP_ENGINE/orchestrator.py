from src.services.context_loader import ContextLoader
from src.parsers.context_parser import ContextParser

from src.sop_engine.sop_loader import SopLoader


class PMOrchestrator:

    def identify_current_activity(self):

        context = ContextLoader.load_context()

        state = ContextParser.parse(context)

        registry = SopLoader.load()

        sop = registry.get(state.current_activity)

        if sop:

            state.current_phase = sop["phase"]

            state.assigned_agent = sop["agent"]

        return state