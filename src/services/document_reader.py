from pathlib import Path


class DocumentReader:

    @staticmethod
    def read_documents():

        root = Path(__file__).resolve().parents[2]

        input_folder = root / "INPUT_DOCUMENTS"

        content = ""

        if not input_folder.exists():

            return content

        for file in input_folder.iterdir():

            if file.is_file():

                if file.suffix == ".md":

                    with open(
                        file,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        content += (
                            f"\n\n===== {file.name} =====\n\n"
                        )

                        content += f.read()

        return content