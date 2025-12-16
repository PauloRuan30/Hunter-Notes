from pydantic import BaseModel, Field
from schemas.enums import StatusEffectWeakness, MonsterElementType

class ElementWeaknessSeverity(BaseModel):
    element: MonsterElementType
    severity: int

class StatusEffectWeaknessSeverity(BaseModel):
    status_effect: StatusEffectWeakness
    severity: int

class Weaknesses(BaseModel):
    element_weaknesses: list[ElementWeaknessSeverity]
    status_effect_weaknesses: list[StatusEffectWeaknessSeverity]