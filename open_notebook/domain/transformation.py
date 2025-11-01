from typing import ClassVar, Optional, List, Any

from pydantic import Field

from open_notebook.domain.base import ObjectModel, RecordModel
from open_notebook.database.repository import repo_query


class Transformation(ObjectModel):
    table_name: ClassVar[str] = "transformation"
    name: str
    title: str
    description: str
    prompt: str
    apply_default: bool

    @classmethod
    async def get_by_attribute(cls, key: str, value: Any) -> List["Transformation"]:
        """Return all transformations where attribute equals value.

        Validates the attribute name against the model fields to avoid invalid queries.
        """
        # Ensure the key is a valid field on the model to prevent bad queries
        if key not in cls.model_fields:
            raise ValueError(f"Invalid attribute '{key}' for Transformation")

        query = f"SELECT * FROM {cls.table_name} WHERE {key} = $value;"
        rows = await repo_query(query, {"value": value})
        return [cls(**row) for row in rows]


class DefaultPrompts(RecordModel):
    record_id: ClassVar[str] = "open_notebook:default_prompts"
    transformation_instructions: Optional[str] = Field(
        None, description="Instructions for executing a transformation"
    )
