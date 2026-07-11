from src.config.settings import CONTEXT_FILE


class ContextLoader:

    @staticmethod
    def load_context():

        print(f"\nLOADING FILE: {CONTEXT_FILE}\n")

        if not CONTEXT_FILE.exists():

            raise FileNotFoundError(
                f"Context file not found: {CONTEXT_FILE}"
            )

        with open(CONTEXT_FILE, "r", encoding="utf-8") as file:

            return file.read()