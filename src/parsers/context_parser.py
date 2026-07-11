print("CONTEXT PARSER LOADED")

from src.models.project_state import ProjectState


class ContextParser:

    @staticmethod
    def parse(context: str):

        state = ProjectState()

        print("\n===== START OF CONTEXT =====")
        print(context[:500])
        print("===== END OF CONTEXT =====\n")

        lines = context.splitlines()

        for line in lines:

            print(f"LINE -> [{line}]")

            if line.startswith("Project Name:"):

                value = line.replace("Project Name:", "").strip()

                print(f"PROJECT VALUE = [{value}]")

                if value:
                    state.project_name = value

            elif line.startswith("Current SDLC Phase:"):

                value = line.replace(
                    "Current SDLC Phase:",
                    ""
                ).strip()

                print(f"PHASE VALUE = [{value}]")

                if value:
                    state.current_phase = value

            elif line.startswith("Current Activity:"):

                value = line.replace(
                    "Current Activity:",
                    ""
                ).strip()

                print(f"ACTIVITY VALUE = [{value}]")

                if value:
                    state.current_activity = value

            elif line.startswith("Assigned Agent:"):

                value = line.replace(
                    "Assigned Agent:",
                    ""
                ).strip()

                print(f"AGENT VALUE = [{value}]")

                if value:
                    state.assigned_agent = value

        print("\nFINAL STATE:", state)

        return state