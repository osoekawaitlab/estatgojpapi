from urllib.parse import urljoin
from urllib.request import Request, urlopen

from pydantic import AnyHttpUrl

from .models import GetMetaInfoResponse, GetStatsListResponse
from .settings import AppSettings


class App:
    def __init__(self, app_id: str, base_url: AnyHttpUrl) -> None:
        self._app_id = app_id
        self._base_url = base_url

    def get_stats_list(self) -> GetStatsListResponse:
        req = Request(urljoin(str(self.base_url), "getStatsList") + f"?appId={self.app_id}")
        with urlopen(req) as res:
            return GetStatsListResponse.model_validate_json(res.read().decode("utf-8"))

    def get_meta_info(self, statsDataId: str) -> GetMetaInfoResponse:
        req = Request(urljoin(str(self.base_url), "getMetaInfo") + f"?appId={self.app_id}&statsDataId={statsDataId}")
        with urlopen(req) as res:
            return GetMetaInfoResponse.model_validate_json(res.read().decode("utf-8"))

    @property
    def app_id(self) -> str:
        return self._app_id

    @property
    def base_url(self) -> AnyHttpUrl:
        return self._base_url

    @classmethod
    def create(cls, settings: AppSettings) -> "App":
        return cls(app_id=settings.app_id, base_url=settings.base_url)
