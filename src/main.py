from src.agents.orchestrator import PMOrchestrator


def main():

    orchestrator = PMOrchestrator()

    state = orchestrator.identify_current_activity()

    print("\n========== PMOS ==========\n")

    print(f"Project           : {state.project_name}")
    print(f"Current Phase     : {state.current_phase}")
    print(f"Current Activity  : {state.current_activity}")
    print(f"Assigned Agent    : {state.assigned_agent}")

    print("\n==========================\n")


if __name__ == "__main__":
    main()