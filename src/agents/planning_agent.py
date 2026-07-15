from src.services.context_builder import ContextBuilder
from src.services.export_service import ExportService


class PlanningAgent:

    def execute(self, state):

        context = ContextBuilder.build_context(
            state
        )

        output_file = ExportService.export_context(
            state.current_activity,
            context
        )

        print("\n===== Planning Agent =====\n")

        print(
            f"Executing Activity : "
            f"{state.current_activity}"
        )

        print(
            f"Project            : "
            f"{state.project_name}"
        )

        print(
            f"\nAI package exported to:\n"
            f"{output_file}"
        )

        print("\n===== AI PACKAGE =====\n")

        print(context)

        print(
            "\n===== END AI PACKAGE =====\n"
        )

        print(
            "\nPlanning activity completed.\n"
        )