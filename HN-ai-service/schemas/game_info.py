from pydantic import BaseModel, Field

class HabitatInfo(BaseModel):
    habitat_name: str = Field(..., title="Habitat Name")
    habitat_type: str = Field(..., title="Habitat Type")

class GameInfo(BaseModel):
    game_name: str = Field(..., title="Game Name")
    release_date: str = Field(..., title="Release Date")
    habitats: list[HabitatInfo] = Field(..., title="Habitats")