from pydantic import BaseModel


class ProjectState(BaseModel):

    project_name: str = ""

    current_phase: str = ""

    current_activity: str = ""

    assigned_agent: str = ""