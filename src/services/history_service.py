import json
from pathlib import Path
from datetime import datetime


class HistoryService:

    @staticmethod
    def save_execution(
        state,
        output_file
    ):

        root = Path(__file__).resolve().parents[2]

        memory_folder = root / "08_MEMORY"

        memory_folder.mkdir(
            exist_ok=True
        )

        history_file = (
            memory_folder /
            "history.json"
        )

        execution = {

            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "project_name": (
                state.project_name
            ),

            "phase": (
                state.current_phase
            ),

            "activity": (
                state.current_activity
            ),

            "agent": (
                state.assigned_agent
            ),

            "output_file": (
                str(output_file)
            )
        }

        history = []

        if history_file.exists():

            with open(
                history_file,
                "r",
                encoding="utf-8"
            ) as file:

                try:

                    history = json.load(
                        file
                    )

                except:

                    history = []

        history.append(
            execution
        )

        with open(
            history_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                history,
                file,
                indent=4
            )