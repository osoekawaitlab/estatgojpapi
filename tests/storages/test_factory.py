import tempfile

import pytest
from pytest_mock import MockerFixture

from estatgojpapi.settings import (
    BaseStorageSettings,
    LocalFileStorageSettings,
    MemoryStorageSettings,
)
from estatgojpapi.storages.factory import create_storage


def test_create_storage_creates_memory_storage(mocker: MockerFixture) -> None:
    MemoryStorage = mocker.patch("estatgojpapi.storages.factory.MemoryStorage")
    settings = MemoryStorageSettings()
    actual = create_storage(settings=settings)
    assert actual == MemoryStorage.return_value
    MemoryStorage.assert_called_once_with()


def test_create_storage_creates_local_file_storage(mocker: MockerFixture) -> None:
    LocalFileStorage = mocker.patch("estatgojpapi.storages.factory.LocalFileStorage")
    with tempfile.TemporaryDirectory() as tmpdir:
        settings = LocalFileStorageSettings(path=tmpdir)
        actual = create_storage(settings=settings)
        assert actual == LocalFileStorage.return_value
        LocalFileStorage.assert_called_once_with(settings.path)


def test_create_storage_raises_error_when_type_is_unknown(mocker: MockerFixture) -> None:
    settings = mocker.MagicMock(spec=BaseStorageSettings)
    settings.type = "UNKNOWN"
    with pytest.raises(ValueError):
        create_storage(settings=settings)
