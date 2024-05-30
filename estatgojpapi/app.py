from urllib.parse import urljoin
from urllib.request import Request, urlopen

from pydantic import AnyHttpUrl

from .models import GetStatsListResponse


class App:
    def __init__(self, app_id: str, base_url: AnyHttpUrl) -> None:
        self._app_id = app_id
        self._base_url = base_url

    def get_stats_list(self) -> GetStatsListResponse:
        req = Request(urljoin(str(self._base_url), "getStatsList") + f"?appId={self._app_id}")
        with urlopen(req) as res:
            return GetStatsListResponse.model_validate_json(res.read().decode("utf-8"))
