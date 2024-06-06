from typing import Dict

from ..models import GetMetaInfoResponse, GetStatsDataResponse, GetStatsListResponse
from .base import BaseStorage


class MemoryStorage(BaseStorage):
    def __init__(self) -> None:
        self._stats_list: GetStatsListResponse | None = None
        self._meta_info: Dict[str, GetMetaInfoResponse] = {}
        self._stats_data: Dict[str, GetStatsDataResponse] = {}

    def has_stats_list(self) -> bool:
        return self._stats_list is not None

    def get_stats_list(self) -> GetStatsListResponse:
        if self._stats_list is None:
            raise KeyError("Stats list is not stored")
        return self._stats_list

    def store_stats_list(self, stats_list: GetStatsListResponse) -> None:
        self._stats_list = stats_list

    def has_meta_info(self, stats_data_id: str) -> bool:
        return stats_data_id in self._meta_info

    def get_meta_info(self, stats_data_id: str) -> GetMetaInfoResponse:
        return self._meta_info[stats_data_id]

    def store_meta_info(self, meta_info: GetMetaInfoResponse) -> None:
        self._meta_info[meta_info.get_meta_info.metadata_inf.table_inf.id] = meta_info

    def has_stats_data(self, stats_data_id: str) -> bool:
        return stats_data_id in self._stats_data

    def get_stats_data(self, stats_data_id: str) -> GetStatsDataResponse:
        return self._stats_data[stats_data_id]

    def store_stats_data(self, stats_data: GetStatsDataResponse) -> None:
        self._stats_data[stats_data.get_stats_data.statistical_data.table_inf.id] = stats_data
