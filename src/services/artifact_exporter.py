from pathlib import Path

from src.services.sop_registry_service import (
    SOPRegistryService
)


class ArtifactExporter:

    @staticmethod
    def export(

        activity,

        artifact

    ):

        config = (

            SOPRegistryService.get_activity(

                activity

            )

        )

        file_name = config.get(

            "artifact",

            f"{activity}_OUTPUT.md"

        )

        root = Path(__file__).resolve().parents[2]

        output_folder = root / "09_OUTPUTS"

        output_folder.mkdir(

            exist_ok=True

        )

        output_file = (

            output_folder /

            file_name

        )

        with open(

            output_file,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(

                artifact

            )

        return output_file