from pydantic import BaseSettings, Extra, Field


class Time(BaseSettings):
    hour: int = Field(0,env="HOUR")
    minute: int = Field(0,env="MINUTE")

    class Config:
        extra = "allow"
        case_sensitive = False
        anystr_lower = True


class Config(BaseSettings):
    # plugin custom config
    plugin_setting: str = "default"

    read_qq_friends: list[int]
    read_qq_groups: list[int]

    read_inform_time: list[Time()] = []

    class Config:
        extra = Extra.allow
        case_sensitive = False
