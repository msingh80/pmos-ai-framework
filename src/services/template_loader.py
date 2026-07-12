import json
from pathlib import Path


class TemplateLoader:

    @staticmethod
    def get_template(activity_id):

        root = Path(__file__).resolve().parents[2]

        registry_file = root / "03_TEMPLATES" / "template_registry.json"

        
        if not registry_file.exists():

            return "Template registry not found"

        with open(
            registry_file,
            "r",
            encoding="utf-8"
        ) as file:

            registry = json.load(file)

        return registry.get(
            activity_id,
            "Template not configured"
        )