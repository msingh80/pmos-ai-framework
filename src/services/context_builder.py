from src.services.prompt_loader import PromptLoader
from src.services.template_loader import TemplateLoader
from src.services.document_loader import DocumentLoader
from src.services.document_reader import DocumentReader


class ContextBuilder:

    @staticmethod
    def build_context(state):

        prompt = PromptLoader.get_prompt(
            state.current_activity
        )

        template = TemplateLoader.get_template(
            state.current_activity
        )

        documents = DocumentLoader.get_documents()

        document_content = (
            DocumentReader.read_documents()
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

AVAILABLE DOCUMENTS:
"""

        for document in documents:

            context += (
                f"\n- {document['name']}"
            )

        context += f"""

==================================================

DOCUMENT CONTENT:

{document_content}

==================================================
"""

        return context