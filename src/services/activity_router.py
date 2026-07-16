import importlib

from src.services.sop_registry_service import (
    SOPRegistryService
)


class ActivityRouter:

    @staticmethod
    def get_agent(activity):

        config = (

            SOPRegistryService.get_activity(

                activity

            )

        )

        agent_name = config.get(

            "agent"
        )

        phase = config.get(

            "phase",

            ""

        ).lower()

        module_name = (

            agent_name

            .replace(

                "Agent",

                ""

            )

            .lower()

        )

        module_path = (

            f"src.agents."

            f"{phase}."

            f"{module_name}_agent"

        )

        try:

            module = importlib.import_module(

                module_path

            )

            agent_class = getattr(

                module,

                agent_name

            )

            return agent_class()

        except Exception as error:

            print(

                f"\nERROR LOADING AGENT:\n"

                f"{error}"

            )

            return None