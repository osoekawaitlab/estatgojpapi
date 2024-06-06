from pytest_mock import MockerFixture

from estatgojpapi.settings import MemoryStorageSettings
from estatgojpapi.storages.factory import create_storage


def test_create_storage_creates_memory_storage(mocker: MockerFixture) -> None:
    MemoryStorage = mocker.patch("estatgojpapi.storages.factory.MemoryStorage")
    settings = MemoryStorageSettings()
    actual = create_storage(settings=settings)
    assert actual == MemoryStorage.return_value
    MemoryStorage.assert_called_once_with()
