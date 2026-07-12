from src.models.project_state import ProjectState

class ContextParser:

    @staticmethod
    def parse(context: str):

        state = ProjectState()

        
        print(context[:500])
        

        lines = context.splitlines()

        for line in lines:

            

            if line.startswith("Project Name:"):

                value = line.replace("Project Name:", "").strip()

                

                if value:
                    state.project_name = value

            elif line.startswith("Current SDLC Phase:"):

                value = line.replace(
                    "Current SDLC Phase:",
                    ""
                ).strip()

                

                if value:
                    state.current_phase = value

            elif line.startswith("Current Activity:"):

                value = line.replace(
                    "Current Activity:",
                    ""
                ).strip()

                

                if value:
                    state.current_activity = value

            elif line.startswith("Assigned Agent:"):

                value = line.replace(
                    "Assigned Agent:",
                    ""
                ).strip()

                
                if value:
                    state.assigned_agent = value

        
        return state