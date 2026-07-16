import json
from pathlib import Path


class TimelineService:

    @staticmethod
    def show_history():

        root = Path(__file__).resolve().parents[2]

        history_file = (
            root /
            "08_MEMORY" /
            "history.json"
        )

        if not history_file.exists():

            print(
                "\nNo execution history found.\n"
            )

            return

        with open(
            history_file,
            "r",
            encoding="utf-8"
        ) as file:

            history = json.load(
                file
            )

        print(
            "\n===== PMOS Timeline =====\n"
        )

        for item in history:

            print(
                f"Date       : "
                f"{item['timestamp']}"
            )

            print(
                f"Activity   : "
                f"{item['activity']}"
            )

            print(
                f"Phase      : "
                f"{item['phase']}"
            )

            print(
                f"Agent      : "
                f"{item['agent']}"
            )

            print(
                f"Output     : "
                f"{item['output_file']}"
            )

            print(
                "\n--------------------------\n"
            )