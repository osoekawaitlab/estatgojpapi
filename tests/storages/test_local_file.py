import tempfile
from pathlib import Path

import pytest

from estatgojpapi.storages.local_file import LocalFileStorage

from ..fixtures import sample_get_meta_info, sample_get_stat_list, sample_get_stats_data


def test_local_file_storage_root_dir() -> None:
    with tempfile.TemporaryDirectory() as temp_dir_str:
        temp_dir = Path(temp_dir_str)
        sut = LocalFileStorage(temp_dir)
        assert sut._root_dir == temp_dir
        assert sut._root_dir.exists()
        assert sut._root_dir.is_dir()
    with tempfile.TemporaryDirectory() as temp_dir_str:
        temp_dir = Path(temp_dir_str)
        sut = LocalFileStorage(temp_dir / "test")
        assert sut._root_dir == temp_dir / "test"
        assert sut._root_dir.exists()
        assert sut._root_dir.is_dir()


def test_local_file_storage_root_is_file() -> None:
    with tempfile.NamedTemporaryFile() as temp_file_buffer:
        temp_file = Path(temp_file_buffer.name)
        sut = LocalFileStorage(temp_file)
        with pytest.raises(ValueError):
            sut._root_dir


def test_local_file_storage_meta_info_dir() -> None:
    with tempfile.TemporaryDirectory() as temp_dir_str:
        temp_dir = Path(temp_dir_str)
        sut = LocalFileStorage(temp_dir)
        assert sut._meta_info_path == temp_dir / "meta_info"
        assert sut._meta_info_path.exists()
        assert sut._meta_info_path.is_dir()


def test_local_file_storage_meta_info_dir_is_file() -> None:
    with tempfile.TemporaryDirectory() as temp_dir_str:
        temp_dir = Path(temp_dir_str)
        with open(temp_dir / "meta_info", "w") as temp_file:
            temp_file.write("test")
        sut = LocalFileStorage(temp_dir)
        with pytest.raises(ValueError):
            sut._meta_info_path


def test_local_file_storage_stats_data_dir() -> None:
    with tempfile.TemporaryDirectory() as temp_dir_str:
        temp_dir = Path(temp_dir_str)
        sut = LocalFileStorage(temp_dir)
        assert sut._stats_data_path == temp_dir / "stats_data"
        assert sut._stats_data_path.exists()
        assert sut._stats_data_path.is_dir()


def test_local_file_storage_stats_data_dir_is_file() -> None:
    with tempfile.TemporaryDirectory() as temp_dir_str:
        temp_dir = Path(temp_dir_str)
        with open(temp_dir / "stats_data", "w") as temp_file:
            temp_file.write("test")
        sut = LocalFileStorage(temp_dir)
        with pytest.raises(ValueError):
            sut._stats_data_path


def test_local_file_storage_stats_list_io() -> None:
    with tempfile.TemporaryDirectory() as temp_dir_str:
        temp_dir = Path(temp_dir_str)
        sut = LocalFileStorage(temp_dir)
        assert not sut.has_stats_list()
        with pytest.raises(KeyError):
            sut.get_stats_list()
        sut.store_stats_list(stats_list=sample_get_stat_list)
        assert sut.has_stats_list()
        assert sut.get_stats_list() == sample_get_stat_list


def test_local_file_storage_meta_info_io() -> None:
    with tempfile.TemporaryDirectory() as temp_dir_str:
        temp_dir = Path(temp_dir_str)
        sut = LocalFileStorage(temp_dir)
        assert not sut.has_meta_info(stats_data_id=sample_get_meta_info.get_meta_info.metadata_inf.table_inf.id)
        with pytest.raises(KeyError):
            sut.get_meta_info(stats_data_id=sample_get_meta_info.get_meta_info.metadata_inf.table_inf.id)
        sut.store_meta_info(meta_info=sample_get_meta_info)
        assert sut.has_meta_info(stats_data_id=sample_get_meta_info.get_meta_info.metadata_inf.table_inf.id)
        assert (
            sut.get_meta_info(stats_data_id=sample_get_meta_info.get_meta_info.metadata_inf.table_inf.id)
            == sample_get_meta_info
        )
        assert not sut.has_meta_info(
            stats_data_id="9" + sample_get_meta_info.get_meta_info.metadata_inf.table_inf.id[1:]
        )
        with pytest.raises(KeyError):
            sut.get_meta_info(stats_data_id="9" + sample_get_meta_info.get_meta_info.metadata_inf.table_inf.id[1:])


def test_local_file_storage_stats_data_io() -> None:
    with tempfile.TemporaryDirectory() as temp_dir_str:
        temp_dir = Path(temp_dir_str)
        sut = LocalFileStorage(temp_dir)
        assert not sut.has_stats_data(stats_data_id=sample_get_stats_data.get_stats_data.statistical_data.table_inf.id)
        with pytest.raises(KeyError):
            sut.get_stats_data(stats_data_id=sample_get_stats_data.get_stats_data.statistical_data.table_inf.id)
        sut.store_stats_data(stats_data=sample_get_stats_data)
        assert sut.has_stats_data(stats_data_id=sample_get_stats_data.get_stats_data.statistical_data.table_inf.id)
        assert (
            sut.get_stats_data(stats_data_id=sample_get_stats_data.get_stats_data.statistical_data.table_inf.id)
            == sample_get_stats_data
        )
        assert not sut.has_stats_data(
            stats_data_id="9" + sample_get_stats_data.get_stats_data.statistical_data.table_inf.id[1:]
        )
        with pytest.raises(KeyError):
            sut.get_stats_data(
                stats_data_id="9" + sample_get_stats_data.get_stats_data.statistical_data.table_inf.id[1:]
            )
