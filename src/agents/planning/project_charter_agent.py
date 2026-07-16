import re


class ProjectCharterAgent:

    def extract_section(

        self,

        text,

        keywords

    ):

        lines = text.split("\n")

        result = []

        capture = False

        for line in lines:

            current_line = line.strip()

            if any(

                keyword.lower()

                in current_line.lower()

                for keyword in keywords

            ):

                capture = True

                result.append(

                    current_line

                )

                continue

            if capture:

                if (

                    current_line.startswith("#")

                    or current_line.startswith("=====")

                    or current_line == ""

                ):

                    break

                result.append(

                    current_line

                )

        return "\n".join(

            result

        ) or "Not found"

    def generate(

        self,

        state,

        documents,

        document_content

    ):

        objective = self.extract_section(

            document_content,

            [

                "Business Objective",

                "Business Objectives"

            ]

        )

        scope = self.extract_section(

            document_content,

            [

                "Scope"

            ]

        )

        deliverables = self.extract_section(

            document_content,

            [

                "Deliverables",

                "Key Deliverables"

            ]

        )

        timeline = self.extract_section(

            document_content,

            [

                "Duration",

                "Timeline",

                "Development"

            ]

        )

        charter = f"""
# PROJECT CHARTER

------------------------------------------------

## Project Information

Project Name:

{state.project_name}

Current Phase:

{state.current_phase}

Current Activity:

{state.current_activity}

------------------------------------------------

## Business Objective

{objective}

------------------------------------------------

## Scope

{scope}

------------------------------------------------

## Timeline

{timeline}

------------------------------------------------

## Deliverables

{deliverables}

------------------------------------------------

## Stakeholders

[TO BE EXTRACTED]

------------------------------------------------

## Risks & Assumptions

[TO BE EXTRACTED]

------------------------------------------------

## Source Documents
"""

        for document in documents:

            charter += (

                f"\n- "

                f"{document['name']}"

                f" ({document['type']})"

            )

        return charter