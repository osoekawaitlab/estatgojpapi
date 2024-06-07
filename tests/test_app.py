from unittest.mock import MagicMock

from pydantic import AnyHttpUrl
from pytest_mock import MockerFixture

from estatgojpapi.app import App, AppWithStorage
from estatgojpapi.models import (
    GetMetaInfoResponse,
    GetStatsDataResponse,
    GetStatsListResponse,
)
from estatgojpapi.settings import AppSettings

from .fixtures import (
    sample_get_meta_info_json,
    sample_get_stat_list_json,
    sample_get_stats_data_json,
)


def test_app_get_stats_list(app_id_for_test: str, http_server_fixture: str) -> None:
    app_settings = AppSettings(app_id=app_id_for_test, base_url=http_server_fixture)
    app = App(app_id=app_settings.app_id, base_url=app_settings.base_url)
    stats_list = app.get_stats_list()
    assert isinstance(stats_list, GetStatsListResponse)
    assert stats_list == GetStatsListResponse.model_validate(sample_get_stat_list_json)


def test_app_get_meta_info(app_id_for_test: str, http_server_fixture: str) -> None:
    app_settings = AppSettings(app_id=app_id_for_test, base_url=http_server_fixture)
    app = App(app_id=app_settings.app_id, base_url=app_settings.base_url)
    meta_info = app.get_meta_info(stats_data_id="0000000000")
    assert isinstance(meta_info, GetMetaInfoResponse)
    assert meta_info == GetMetaInfoResponse.model_validate(sample_get_meta_info_json)


def test_app_create_without_storage(mocker: MockerFixture) -> None:
    create_storage = mocker.patch("estatgojpapi.app.create_storage")
    settings = AppSettings(app_id="test", base_url="http://example.com")
    app = App.create(settings=settings)
    assert isinstance(app, App)
    assert app.app_id == "test"
    assert app.base_url == AnyHttpUrl("http://example.com")
    create_storage.assert_not_called()


def test_app_create_with_storage(mocker: MockerFixture) -> None:
    create_storage = mocker.patch("estatgojpapi.app.create_storage")
    settings = AppSettings(app_id="test", base_url="http://example.com", storage_settings={"type": "MEMORY"})
    app = App.create(settings=settings)
    assert isinstance(app, App)
    assert app.app_id == "test"
    assert app.base_url == AnyHttpUrl("http://example.com")
    create_storage.assert_called_once_with(settings=settings.storage_settings)


def test_app_get_stats_data(app_id_for_test: str, http_server_fixture: str) -> None:
    app_settings = AppSettings(app_id=app_id_for_test, base_url=http_server_fixture)
    app = App(app_id=app_settings.app_id, base_url=app_settings.base_url)
    stats_data = app.get_stats_data(stats_data_id="0000000000")
    assert isinstance(stats_data, GetStatsDataResponse)
    assert stats_data == GetStatsDataResponse.model_validate(sample_get_stats_data_json)


def test_app_with_storage_get_stats_list_from_saved_value(
    app_id_for_test: str, http_server_fixture: str, mock_storage: MagicMock, mocker: MockerFixture
) -> None:
    mock_storage.has_stats_list.return_value = True
    mocked_base_method = mocker.patch.object(App, "get_stats_list")
    sut = AppWithStorage(app_id=app_id_for_test, base_url=AnyHttpUrl(http_server_fixture), storage=mock_storage)
    actual = sut.get_stats_list()
    assert actual == mock_storage.get_stats_list.return_value
    mock_storage.has_stats_list.assert_called_once_with()
    mock_storage.get_stats_list.assert_called_once_with()
    mocked_base_method.assert_not_called()


def test_app_with_storage_get_stats_list_from_api(
    app_id_for_test: str, http_server_fixture: str, mock_storage: MagicMock, mocker: MockerFixture
) -> None:
    mock_storage.has_stats_list.return_value = False
    mocked_base_method = mocker.patch.object(App, "get_stats_list")
    sut = AppWithStorage(app_id=app_id_for_test, base_url=AnyHttpUrl(http_server_fixture), storage=mock_storage)
    actual = sut.get_stats_list()
    assert actual == mocked_base_method.return_value
    mock_storage.has_stats_list.assert_called_once_with()
    mock_storage.get_stats_list.assert_not_called()
    mock_storage.store_stats_list.assert_called_once_with(mocked_base_method.return_value)
    mocked_base_method.assert_called_once_with()


def test_app_with_storage_get_meta_info_from_api(
    app_id_for_test: str, http_server_fixture: str, mock_storage: MagicMock, mocker: MockerFixture
) -> None:
    mock_storage.has_meta_info.return_value = False
    mocked_base_method = mocker.patch.object(App, "get_meta_info")
    sut = AppWithStorage(app_id=app_id_for_test, base_url=AnyHttpUrl(http_server_fixture), storage=mock_storage)
    actual = sut.get_meta_info(stats_data_id="0000000000")
    assert actual == mocked_base_method.return_value
    mock_storage.has_meta_info.assert_called_once_with(stats_data_id="0000000000")
    mock_storage.get_meta_info.assert_not_called()
    mock_storage.store_meta_info.assert_called_once_with(meta_info=mocked_base_method.return_value)
    mocked_base_method.assert_called_once_with(stats_data_id="0000000000")


def test_app_with_storage_get_meta_info_from_saved_value(
    app_id_for_test: str, http_server_fixture: str, mock_storage: MagicMock, mocker: MockerFixture
) -> None:
    mock_storage.has_meta_info.return_value = True
    mocked_base_method = mocker.patch.object(App, "get_meta_info")
    sut = AppWithStorage(app_id=app_id_for_test, base_url=AnyHttpUrl(http_server_fixture), storage=mock_storage)
    actual = sut.get_meta_info(stats_data_id="0000000000")
    assert actual == mock_storage.get_meta_info.return_value
    mock_storage.has_meta_info.assert_called_once_with(stats_data_id="0000000000")
    mock_storage.get_meta_info.assert_called_once_with(stats_data_id="0000000000")
    mock_storage.store_meta_info.assert_not_called()
    mocked_base_method.assert_not_called()


def test_app_with_storage_get_stats_data_from_api(
    app_id_for_test: str, http_server_fixture: str, mock_storage: MagicMock, mocker: MockerFixture
) -> None:
    mock_storage.has_stats_data.return_value = False
    mocked_base_method = mocker.patch.object(App, "get_stats_data")
    sut = AppWithStorage(app_id=app_id_for_test, base_url=AnyHttpUrl(http_server_fixture), storage=mock_storage)
    actual = sut.get_stats_data(stats_data_id="0000000000")
    assert actual == mocked_base_method.return_value
    mock_storage.has_stats_data.assert_called_once_with(stats_data_id="0000000000")
    mock_storage.get_stats_data.assert_not_called()
    mock_storage.store_stats_data.assert_called_once_with(stats_data=mocked_base_method.return_value)
    mocked_base_method.assert_called_once_with(stats_data_id="0000000000")


def test_app_with_storage_get_stats_data_from_saved_value(
    app_id_for_test: str, http_server_fixture: str, mock_storage: MagicMock, mocker: MockerFixture
) -> None:
    mock_storage.has_stats_data.return_value = True
    mocked_base_method = mocker.patch.object(App, "get_stats_data")
    sut = AppWithStorage(app_id=app_id_for_test, base_url=AnyHttpUrl(http_server_fixture), storage=mock_storage)
    actual = sut.get_stats_data(stats_data_id="0000000000")
    assert actual == mock_storage.get_stats_data.return_value
    mock_storage.has_stats_data.assert_called_once_with(stats_data_id="0000000000")
    mock_storage.get_stats_data.assert_called_once_with(stats_data_id="0000000000")
    mock_storage.store_stats_data.assert_not_called()
    mocked_base_method.assert_not_called()
