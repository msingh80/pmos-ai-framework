from pathlib import Path


class DocumentLoader:

    @staticmethod
    def get_documents():

        root = Path(__file__).resolve().parents[2]

        input_folder = root / "INPUT_DOCUMENTS"

        documents = []

        if not input_folder.exists():

            return documents

        for file in input_folder.rglob("*"):

            if file.is_file():

                documents.append(

                    {
                        "name": file.name,

                        "path": str(file),

                        "extension": file.suffix
                    }

                )

        return documents