from src.services.prompt_loader import PromptLoader
from src.services.template_loader import TemplateLoader
from src.services.document_loader import DocumentLoader
from src.services.document_reader import DocumentReader
from src.services.document_filter import DocumentFilter
from src.services.document_classifier import DocumentClassifier


class ContextBuilder:

    @staticmethod
    def build_context(state):

        prompt = PromptLoader.get_prompt(

            state.current_activity

        )

        template = TemplateLoader.get_template(

            state.current_activity

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

        context = f"""
==================================================

PROJECT NAME:
{state.project_name}

CURRENT PHASE:
{state.current_phase}

CURRENT ACTIVITY:
{state.current_activity}

ASSIGNED AGENT:
{state.assigned_agent}

==================================================

TEMPLATE DETAILS:

{template}

==================================================

PROMPT:

{prompt}

==================================================

RELEVANT DOCUMENTS:
"""

        for document in documents:

            context += (

                f"\n- {document['name']}"

                f" ({document['type']})"

            )

        context += f"""

==================================================

DOCUMENT CONTENT:

{document_content}

==================================================
"""

        return context