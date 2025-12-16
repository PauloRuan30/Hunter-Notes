from schemas.enums import MonsterType, MonsterElementType, MonsterStatusEffects
from schemas.weakness import Weaknesses
from schemas.game_info import GameInfo
from pydantic import BaseModel, Field

class MonsterName(BaseModel):
    name: str = Field(..., title="Name")

class MonsterNameList(BaseModel):
    names: list[MonsterName] = Field(..., title="Names")

class MonsterInfo(BaseModel):
    name: str = Field(..., title="Name")
    monster_type: MonsterType = Field(..., title="Type")
    monster_type_description: str = Field(..., title="Type Description")
    physical_description: str = Field(..., title="Physical Description")
    monster_element: MonsterElementType = Field(..., title="Element")
    second_stage: bool = Field(..., title="Second Stage")
    weakness_base: Weaknesses = Field(..., title="Weakness Base")
    weakness_second: Weaknesses = Field(..., title="Weakness Second")
    game_info: GameInfo = Field(..., title="Game Info")

class MonsterInfoList(BaseModel):
    infos: list[MonsterInfo] = Field(..., title="Infos")