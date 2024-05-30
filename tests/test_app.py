from estatgojpapi.app import App
from estatgojpapi.models import GetStatsListResponse
from estatgojpapi.settings import AppSettings

from .fixtures import sample_get_stat_list_json


def test_app_get_stats_list(app_id_for_test: str, http_server_fixture: str) -> None:
    app_settings = AppSettings(app_id=app_id_for_test, base_url=http_server_fixture)
    app = App(app_id=app_settings.app_id, base_url=app_settings.base_url)
    stats_list = app.get_stats_list()
    assert isinstance(stats_list, GetStatsListResponse)
    assert stats_list == GetStatsListResponse.model_validate(sample_get_stat_list_json)
