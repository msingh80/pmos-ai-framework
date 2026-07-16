from pathlib import Path


class CharterExportService:

    @staticmethod
    def export(charter):

        root = Path(__file__).resolve().parents[2]

        output_folder = root / "09_OUTPUTS"

        output_folder.mkdir(

            exist_ok=True

        )

        output_file = (

            output_folder /

            "PROJECT_CHARTER.md"

        )

        with open(

            output_file,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(charter)

        return output_file