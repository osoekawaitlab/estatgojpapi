from urllib.parse import urljoin
from urllib.request import Request, urlopen

from pydantic import AnyHttpUrl

from .models import GetMetaInfoResponse, GetStatsDataResponse, GetStatsListResponse
from .settings import AppSettings
from .storages.base import BaseStorage
from .storages.factory import create_storage


class App:
    def __init__(self, app_id: str, base_url: AnyHttpUrl) -> None:
        self._app_id = app_id
        self._base_url = base_url

    def get_stats_list(self) -> GetStatsListResponse:
        req = Request(urljoin(str(self.base_url), "getStatsList") + f"?appId={self.app_id}")
        with urlopen(req) as res:
            return GetStatsListResponse.model_validate_json(res.read().decode("utf-8"))

    def get_meta_info(self, stats_data_id: str) -> GetMetaInfoResponse:
        req = Request(urljoin(str(self.base_url), "getMetaInfo") + f"?appId={self.app_id}&statsDataId={stats_data_id}")
        with urlopen(req) as res:
            return GetMetaInfoResponse.model_validate_json(res.read().decode("utf-8"))

    def get_stats_data(self, stats_data_id: str) -> GetStatsDataResponse:
        req = Request(urljoin(str(self.base_url), "getStatsData") + f"?appId={self.app_id}&statsDataId={stats_data_id}")
        with urlopen(req) as res:
            return GetStatsDataResponse.model_validate_json(res.read().decode("utf-8"))

    @property
    def app_id(self) -> str:
        return self._app_id

    @property
    def base_url(self) -> AnyHttpUrl:
        return self._base_url

    @classmethod
    def create(cls, settings: AppSettings) -> "App":
        if settings.storage_settings is not None:
            storage = create_storage(settings=settings.storage_settings)
            return AppWithStorage(app_id=settings.app_id, base_url=settings.base_url, storage=storage)
        return cls(app_id=settings.app_id, base_url=settings.base_url)


class AppWithStorage(App):
    def __init__(self, app_id: str, base_url: AnyHttpUrl, storage: BaseStorage) -> None:
        super(AppWithStorage, self).__init__(app_id=app_id, base_url=base_url)
        self._storage = storage

    @property
    def storage(self) -> BaseStorage:
        return self._storage

    def get_stats_list(self) -> GetStatsListResponse:
        if self.storage.has_stats_list():
            return self.storage.get_stats_list()
        stats_list = super(AppWithStorage, self).get_stats_list()
        self.storage.store_stats_list(stats_list)
        return stats_list

    def get_meta_info(self, stats_data_id: str) -> GetMetaInfoResponse:
        if self.storage.has_meta_info(stats_data_id=stats_data_id):
            return self.storage.get_meta_info(stats_data_id=stats_data_id)
        meta_info = super(AppWithStorage, self).get_meta_info(stats_data_id=stats_data_id)
        self.storage.store_meta_info(meta_info=meta_info)
        return meta_info
