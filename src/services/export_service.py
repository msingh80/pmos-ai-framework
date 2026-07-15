from pathlib import Path


class ExportService:

    @staticmethod
    def export_context(activity_id, content):

        root = Path(__file__).resolve().parents[2]

        output_folder = root / "06_OUTPUTS"

        output_folder.mkdir(
            exist_ok=True
        )

        output_file = (
            output_folder /
            f"{activity_id}_AI_PACKAGE.md"
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)

        return output_file