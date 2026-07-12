import json
from pathlib import Path


class SopLoader:

    @staticmethod
    def load():

        root = Path(__file__).resolve().parents[1]

        file = root / "01_SOP_ENGINE" / "SOP_REGISTRY.json"

        with open(file, "r", encoding="utf-8") as f:

            return json.load(f)