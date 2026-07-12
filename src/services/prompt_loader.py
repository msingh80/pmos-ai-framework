from pathlib import Path


class PromptLoader:

    @staticmethod
    def get_prompt(activity_id):

        root = Path(__file__).resolve().parents[2]

        prompt_file = (
            root / "02_PROMPTS" / f"{activity_id}.md"
        )

        if not prompt_file.exists():

            return "Prompt not found"

        with open(
            prompt_file,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()