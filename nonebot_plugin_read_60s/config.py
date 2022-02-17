from pydantic import BaseSettings, Extra, Field


class Time(BaseSettings):
    hour: int = Field(0,alias="HOUR")
    minute: int = Field(0,alias="MINUTE")

    class Config:
        extra = "allow"
        case_sensitive = False
        anystr_lower = True


class Config(BaseSettings):
    # plugin custom config
    plugin_setting: str = "default"

    leetcode_qq_friends: list[int]
    leetcode_qq_groups: list[int]

    leetcode_inform_time: list[Time()] = []

    class Config:
        extra = Extra.allow
        case_sensitive = False