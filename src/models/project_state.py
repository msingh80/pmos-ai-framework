from pydantic import BaseModel


class ProjectState(BaseModel):

    project_name: str = "PMOS AI Framework"

    current_phase: str = "Initiation"

    current_activity: str = "PM-01"

    assigned_agent: str = "Planning Agent"