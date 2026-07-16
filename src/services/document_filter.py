from src.services.sop_registry_service import (
    SOPRegistryService
)


class DocumentFilter:

    @staticmethod
    def get_relevant_documents(

        activity_id,

        documents

    ):

        config = (

            SOPRegistryService.get_activity(

                activity_id

            )

        )

        keywords = config.get(

            "documents",

            []

        )

        filtered_documents = []

        for document in documents:

            for keyword in keywords:

                if keyword.lower() in (

                    document["name"].lower()

                ):

                    filtered_documents.append(

                        document

                    )

                    break

        return filtered_documents