from src.services.template_loader import TemplateLoader
from src.services.prompt_loader import PromptLoader


class PlanningAgent:

    def execute(self, state):

        template = TemplateLoader.get_template(
            state.current_activity
        )

        prompt = PromptLoader.get_prompt(
            state.current_activity
        )

        print("\n===== Planning Agent =====\n")

        print(
            f"Executing Activity : "
            f"{state.current_activity}"
        )

        print(
            f"Project            : "
            f"{state.project_name}"
        )

        print(
            f"\nTemplate Details:\n"
            f"{template}"
        )

        print(
            f"\nPrompt:\n"
            f"{prompt[:300]}"
        )

        print(
            "\nPlanning activity completed.\n"
        )