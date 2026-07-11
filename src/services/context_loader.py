from pathlib import Path


class ContextLoader:

    @staticmethod
    def load_context():

        project_root = Path(__file__).resolve().parent.parent.parent

        context_path = project_root / "00_CONTEXT" / "PROJECT_CONTEXT.md"

        if not context_path.exists():
            raise FileNotFoundError(
                f"Context file not found: {context_path}"
            )

        with open(context_path, "r", encoding="utf-8") as file:
            return file.read()