from src.agents.orchestrator import PMOrchestrator
from src.services.timeline_service import TimelineService


def main():

    orchestrator = PMOrchestrator()

    state = orchestrator.run()

    print("\n========== PMOS ==========\n")

    print(
        f"Project           : "
        f"{state.project_name}"
    )

    print(
        f"Current Phase     : "
        f"{state.current_phase}"
    )

    print(
        f"Current Activity  : "
        f"{state.current_activity}"
    )

    print(
        f"Assigned Agent    : "
        f"{state.assigned_agent}"
    )

    TimelineService.show_history()

    print(
        "\n==========================\n"
    )


if __name__ == "__main__":

    main()