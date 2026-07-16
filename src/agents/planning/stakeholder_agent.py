class StakeholderAgent:

    def extract_people(

        self,

        document_content

    ):

        stakeholders = []

        lines = document_content.split(
            "\n"
        )

        for line in lines:

            line = line.strip()

            if (

                line.startswith("- ")

                and len(line) > 3

            ):

                stakeholders.append(

                    line.replace(

                        "- ",

                        ""

                    )

                )

        return stakeholders

    def generate(

        self,

        state,

        documents,

        document_content

    ):

        stakeholders = (

            self.extract_people(

                document_content

            )

        )

        artifact = f"""
# STAKEHOLDER REGISTER

------------------------------------------------

## Project Information

Project Name:

{state.project_name}

Current Activity:

{state.current_activity}

------------------------------------------------

## Stakeholders

"""

        if stakeholders:

            for person in stakeholders:

                artifact += f"""

Name:

{person}

Role:

[TO BE IDENTIFIED]

Organization:

[TO BE IDENTIFIED]

RACI:

[TO BE IDENTIFIED]

------------------------------------------------
"""

        else:

            artifact += """

No stakeholders found.

"""

        artifact += """

## Source Documents

"""

        for document in documents:

            artifact += (

                f"\n- "

                f"{document['name']}"

                f" ({document['type']})"

            )

        return artifact