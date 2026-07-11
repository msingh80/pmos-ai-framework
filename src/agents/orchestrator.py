from src.models.project_state import ProjectState
from src.services.context_loader import ContextLoader


class PMOrchestrator:

    def identify_current_activity(self):

        context = ContextLoader.load_context()

        print("\n========== PROJECT CONTEXT ==========\n")

        print(context[:1000])

        print("\n=====================================\n")

        state = ProjectState()

        return state