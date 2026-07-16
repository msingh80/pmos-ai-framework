import json
from pathlib import Path


class SOPRegistryService:

    @staticmethod
    def get_activity(activity_id):

        root = Path(__file__).resolve().parents[2]

        registry_file = (

            root
            / "01_SOP_ENGINE"
            / "sop_registry.json"

        )

        if not registry_file.exists():

            return {}

        with open(

            registry_file,

            "r",

            encoding="utf-8"

        ) as file:

            registry = json.load(

                file

            )

        return registry.get(

            activity_id,

            {}

        )