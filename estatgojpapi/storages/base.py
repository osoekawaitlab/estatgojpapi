from abc import ABC, abstractmethod

from ..models import GetMetaInfoResponse, GetStatsDataResponse, GetStatsListResponse


class BaseStorage(ABC):
    @abstractmethod
    def has_stats_list(self) -> bool: ...

    @abstractmethod
    def get_stats_list(self) -> GetStatsListResponse: ...

    @abstractmethod
    def store_stats_list(self, stats_list: GetStatsListResponse) -> None: ...

    @abstractmethod
    def has_meta_info(self, stats_data_id: str) -> bool: ...

    @abstractmethod
    def get_meta_info(self, stats_data_id: str) -> GetMetaInfoResponse: ...

    @abstractmethod
    def store_meta_info(self, meta_info: GetMetaInfoResponse) -> None: ...

    @abstractmethod
    def has_stats_data(self, stats_data_id: str) -> bool: ...

    @abstractmethod
    def get_stats_data(self, stats_data_id: str) -> GetStatsDataResponse: ...

    @abstractmethod
    def store_stats_data(self, stats_data: GetStatsDataResponse) -> None: ...
