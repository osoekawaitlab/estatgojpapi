from estatgojpapi.models import GetMetaInfoResponse, GetStatsListResponse

from .fixtures import sample_get_meta_info_json, sample_get_stat_list_json


def test_get_stat_list_response() -> None:
    sut = GetStatsListResponse.model_validate(sample_get_stat_list_json)
    assert sut.get_stats_list.datalist_inf.number == 3
    assert sut.get_stats_list.datalist_inf.result_inf.from_number == 1
    assert sut.get_stats_list.datalist_inf.result_inf.to_number == 3
    assert sut.get_stats_list.datalist_inf.table_inf[0].stat_name.code == "00020111"
    assert sut.get_stats_list.datalist_inf.table_inf[0].stat_name.value == "民間企業の勤務条件制度等調査"
    assert sut.get_stats_list.datalist_inf.table_inf[0].gov_org.code == "00020"
    assert sut.get_stats_list.datalist_inf.table_inf[0].gov_org.value == "＊＊＊"
    assert sut.get_stats_list.datalist_inf.table_inf[0].statistics_name == "＊＊＊ 統計表 １　＊＊＊の状況"


def test_get_meta_info_response() -> None:
    sut = GetMetaInfoResponse.model_validate(sample_get_meta_info_json)
    assert sut.get_meta_info.result.status == 0
