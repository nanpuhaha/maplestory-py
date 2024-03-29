from datetime import datetime

from pydantic import BaseModel, field_validator

import maplestory.utils.kst as kst
from maplestory.models.ranking.common import RankingModel
from maplestory.utils.repr import DatetimeRepresentation


class TheSeedRankingInfo(DatetimeRepresentation, BaseModel):
    """더 시드 랭킹 상세 정보

    Attributes:
        date: 랭킹 업데이트 일자 (KST, 일 단위 데이터로 시, 분은 일괄 0으로 표기)
        ranking: 더 시드 랭킹 순위
        character_name: 캐릭터 명
        world_name: 월드 명
        class_name: 직업 명
        sub_class_name: 전직 직업 명
        character_level: 캐릭터 레벨
        theseed_floor: 더 시드 층수
        theseed_time_record: 더 시드 클리어 시간 기록 (초 단위)
    """

    date: kst.KSTAwareDatetime
    ranking: int
    character_name: str
    world_name: str
    class_name: str
    sub_class_name: str
    character_level: int
    theseed_floor: int
    theseed_time_record: int

    @field_validator("date", mode="before")
    @classmethod
    def change_date(cls, v: str) -> kst.KSTAwareDatetime:
        dt = datetime.strptime(v, "%Y-%m-%d")
        return kst.datetime(dt.year, dt.month, dt.day)


class TheSeedRanking(RankingModel[TheSeedRankingInfo]):
    """더 시드 랭킹 정보

    Attributes:
        ranking: 더 시드 랭킹 정보
    """
