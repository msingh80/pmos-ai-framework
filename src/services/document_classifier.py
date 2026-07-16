from pathlib import Path


class DocumentClassifier:

    @staticmethod
    def classify(documents):

        classified_documents = []

        document_rules = {

            "BRD": "Business Requirement Document",

            "FSD": "Functional Specification Document",

            "SOW": "Statement Of Work",

            "RAID": "Risk Register",

            "SPRINT": "Sprint Plan",

            "TRANSCRIPT": "Meeting Transcript",

            "MOM": "Minutes Of Meeting",

            "USER_STORY": "User Story",

            "WSR": "Weekly Status Report",

            "SOP": "Standard Operating Procedure"
        }

        for document in documents:

            document_type = "Unknown"

            file_name = (

                Path(
                    document["path"]
                ).stem.upper()

            )

            for keyword, doc_type in (

                document_rules.items()

            ):

                if keyword in file_name:

                    document_type = doc_type

                    break

            classified_documents.append(

                {

                    "name": document["name"],

                    "path": document["path"],

                    "extension": document["extension"],

                    "type": document_type
                }

            )

        return classified_documents