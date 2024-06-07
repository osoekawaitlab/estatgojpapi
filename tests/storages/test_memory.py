import pytest

from estatgojpapi.storages.memory import MemoryStorage

from ..fixtures import sample_get_meta_info, sample_get_stat_list, sample_get_stats_data


def test_memory_storage_stats_list_io() -> None:
    sut = MemoryStorage()
    assert not sut.has_stats_list()
    with pytest.raises(KeyError):
        sut.get_stats_list()
    sut.store_stats_list(stats_list=sample_get_stat_list)
    assert sut.has_stats_list()
    assert sut.get_stats_list() == sample_get_stat_list


def test_memory_storage_meta_info_io() -> None:
    sut = MemoryStorage()
    assert not sut.has_meta_info(stats_data_id=sample_get_meta_info.get_meta_info.metadata_inf.table_inf.id)
    with pytest.raises(KeyError):
        sut.get_meta_info(stats_data_id=sample_get_meta_info.get_meta_info.metadata_inf.table_inf.id)
    sut.store_meta_info(meta_info=sample_get_meta_info)
    assert sut.has_meta_info(stats_data_id=sample_get_meta_info.get_meta_info.metadata_inf.table_inf.id)
    assert (
        sut.get_meta_info(stats_data_id=sample_get_meta_info.get_meta_info.metadata_inf.table_inf.id)
        == sample_get_meta_info
    )
    assert not sut.has_meta_info(stats_data_id="9" + sample_get_meta_info.get_meta_info.metadata_inf.table_inf.id[1:])
    with pytest.raises(KeyError):
        sut.get_meta_info(stats_data_id="9" + sample_get_meta_info.get_meta_info.metadata_inf.table_inf.id[1:])


def test_memory_storage_stats_data_io() -> None:
    sut = MemoryStorage()
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
        sut.get_stats_data(stats_data_id="9" + sample_get_stats_data.get_stats_data.statistical_data.table_inf.id[1:])
