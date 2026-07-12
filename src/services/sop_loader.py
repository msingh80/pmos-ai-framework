from pathlib import Path


class SopLoader:

    @staticmethod
    def load_sop(activity_id: str):

        project_root = Path(__file__).resolve().parent.parent.parent

        sop_file = project_root / "01_SOP_ENGINE" / f"{activity_id}_PROJECT_CHARTER.md"

        if not sop_file.exists():

            return f"SOP not found: {sop_file}"

        with open(sop_file, "r", encoding="utf-8") as file:

            return file.read()