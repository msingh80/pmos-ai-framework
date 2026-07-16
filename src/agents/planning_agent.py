from src.services.context_builder import ContextBuilder
from src.services.export_service import ExportService
from src.services.history_service import HistoryService

from src.services.document_loader import DocumentLoader
from src.services.document_classifier import DocumentClassifier
from src.services.document_filter import DocumentFilter
from src.services.document_reader import DocumentReader

from src.services.activity_router import (
    ActivityRouter
)

from src.services.artifact_exporter import (
    ArtifactExporter
)


class PlanningAgent:

    def execute(self, state):

        context = ContextBuilder.build_context(

            state

        )

        ai_package = ExportService.export_context(

            state.current_activity,

            context

        )

        all_documents = (

            DocumentClassifier.classify(

                DocumentLoader.get_documents()

            )

        )

        documents = (

            DocumentFilter.get_relevant_documents(

                state.current_activity,

                all_documents

            )

        )

        document_content = (

            DocumentReader.read_documents(

                documents

            )

        )

        activity_agent = (

            ActivityRouter.get_agent(

                state.current_activity

            )

        )

        if activity_agent:

            artifact = (

                activity_agent.generate(

                    state,

                    documents,

                    document_content

                )

            )

            artifact_file = (

                ArtifactExporter.export(

                    state.current_activity,

                    artifact

                )

            )

            print(

                "\nArtifact Created:\n"

                f"{artifact_file}"

            )

        HistoryService.save_execution(

            state,

            ai_package

        )

        print(

            "\n===== Planning Agent =====\n"

        )

        print(

            f"Executing Activity : "

            f"{state.current_activity}"

        )

        print(

            f"Project            : "

            f"{state.project_name}"

        )

        print(

            f"\nAI Package:\n"

            f"{ai_package}"

        )

        print(

            "\nPlanning activity completed.\n"

        )