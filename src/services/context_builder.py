from src.services.prompt_loader import PromptLoader
from src.services.template_loader import TemplateLoader
from src.services.document_loader import DocumentLoader


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

            context += f"\n- {document['name']}"

        return context