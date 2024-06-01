import re
from typing import Literal, Optional, TypeAlias

from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict
from pydantic.json_schema import JsonSchemaValue

IncEx: TypeAlias = "set[int] | set[str] | dict[int, IncEx] | dict[str, IncEx] | None"


def to_estat_attribute_name(name: str) -> str:
    """
    >>> to_estat_attribute_name('objectName')
    'OBJECT_NAME'
    >>> to_estat_attribute_name('object_name')
    'OBJECT_NAME'
    >>> to_estat_attribute_name('id')
    '@id'
    >>> to_estat_attribute_name('no')
    '@no'
    >>> to_estat_attribute_name('code')
    '@code'
    >>> to_estat_attribute_name('value')
    '$'
    >>> to_estat_attribute_name('name')
    '@name'
    >>> to_estat_attribute_name('class_')
    'CLASS'
    >>> to_estat_attribute_name('unit')
    '@unit'
    >>> to_estat_attribute_name('parent_code')
    '@parentCode'
    >>> to_estat_attribute_name('value_')
    'VALUE'
    >>> to_estat_attribute_name('cat01')
    '@cat01'
    >>> to_estat_attribute_name('cat02')
    '@cat02'
    >>> to_estat_attribute_name('time')
    '@time'
    >>> to_estat_attribute_name('char')
    '@char'
    """
    return {
        "id": "@id",
        "no": "@no",
        "code": "@code",
        "value": "$",
        "name": "@name",
        "class_": "CLASS",
        "unit": "@unit",
        "parent_code": "@parentCode",
        "value_": "VALUE",
        "cat01": "@cat01",
        "cat02": "@cat02",
        "time": "@time",
        "char": "@char",
    }.get(name, to_upper_snake(name))


def to_upper_snake(name: str) -> str:
    """
    >>> to_upper_snake('objectName')
    'OBJECT_NAME'
    >>> to_upper_snake('object_name')
    'OBJECT_NAME'
    """
    return re.sub(r"(?<!^)(?=[A-Z])", "_", name).upper()


class BaseModel(PydanticBaseModel):
    """
    >>> class Foo(BaseModel):
    ...     get_stats_list: str
    >>> x = Foo.model_validate_json('{"GET_STATS_LIST": "foo"}')
    >>> x
    Foo(get_stats_list='foo')
    >>> x.model_dump_json()
    '{"GET_STATS_LIST":"foo"}'
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_estat_attribute_name, validate_assignment=True)

    def model_dump_json(
        self,
        *,
        indent: int | None = None,
        include: IncEx = None,
        exclude: IncEx = None,
        context: JsonSchemaValue | None = None,
        by_alias: bool = True,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        round_trip: bool = False,
        warnings: bool | Literal["none"] | Literal["warn"] | Literal["error"] = True,
        serialize_as_any: bool = False,
    ) -> str:
        return super().model_dump_json(
            indent=indent,
            include=include,
            exclude=exclude,
            context=context,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            round_trip=round_trip,
            warnings=warnings,
            serialize_as_any=serialize_as_any,
        )


class CodeValue(BaseModel):
    code: str
    value: str


class StatName(CodeValue):
    """
    >>> x = StatName.model_validate_json('{"@code": "00020111","$": "民間企業の勤務条件制度等調査"}')
    >>> x
    StatName(code='00020111', value='民間企業の勤務条件制度等調査')
    >>> x.model_dump_json()
    '{"@code":"00020111","$":"民間企業の勤務条件制度等調査"}'
    """


class GovOrg(CodeValue):
    """
    >>> x = GovOrg.model_validate_json('{"@code": "00020","$": "人事院"}')
    >>> x
    GovOrg(code='00020', value='人事院')
    >>> x.model_dump_json()
    '{"@code":"00020","$":"人事院"}'
    """


class Title(BaseModel):
    """
    >>> x = Title.model_validate_json('{"@no": "1","$": "全国"}')
    >>> x
    Title(no='1', value='全国')
    >>> x.model_dump_json()
    '{"@no":"1","$":"全国"}'
    """

    no: str
    value: str


class MainCategory(CodeValue):
    """
    >>> x = MainCategory.model_validate_json('{"@code": "03","$": "労働・賃金"}')
    >>> x
    MainCategory(code='03', value='労働・賃金')
    >>> x.model_dump_json()
    '{"@code":"03","$":"労働・賃金"}'
    """


class SubCategory(CodeValue):
    """
    >>> x = SubCategory.model_validate_json('{"@code": "02","$": "賃金・労働条件"}')
    >>> x
    SubCategory(code='02', value='賃金・労働条件')
    >>> x.model_dump_json()
    '{"@code":"02","$":"賃金・労働条件"}'
    """


class StatisticsNameSpec(BaseModel):
    """
    >>> x = StatisticsNameSpec.model_validate_json('{"TABULATION_CATEGORY": "民間企業の勤務条件制度等調査（民間企業退職給付調査）","TABULATION_SUB_CATEGORY1": "統計表","TABULATION_SUB_CATEGORY2": "１　定年制と定年退職者の継続雇用の状況"}')
    >>> x
    StatisticsNameSpec(tabulation_category='民間企業の勤務条件制度等調査（民間企業退職給付調査）', tabulation_sub_category1='統計表', tabulation_sub_category2='１\u3000定年制と定年退職者の継続雇用の状況')
    >>> x.model_dump_json()
    '{"TABULATION_CATEGORY":"民間企業の勤務条件制度等調査（民間企業退職給付調査）","TABULATION_SUB_CATEGORY1":"統計表","TABULATION_SUB_CATEGORY2":"１\u3000定年制と定年退職者の継続雇用の状況"}'
    """  # noqa: E501

    tabulation_category: str
    tabulation_sub_category1: Optional[str] = None
    tabulation_sub_category2: Optional[str] = None


class TitleSpec(BaseModel):
    """
    >>> x = TitleSpec.model_validate_json('{"TABLE_CATEGORY": "（推計値）","TABLE_NAME": "定年制の状況","TABLE_EXPLANATION": "１　事務・技術関係職種の従業員がいる企業41,314社について集計した。２　「定年年齢」内の数値は定年制がある企業を100とした場合の割合を示す。"}')
    >>> x
    TitleSpec(table_category='（推計値）', table_name='定年制の状況', table_explanation='１\u3000事務・技術関係職種の従業員がいる企業41,314社について集計した。２\u3000「定年年齢」内の数値は定年制がある企業を100とした場合の割合を示す。')
    >>> x.model_dump_json()
    '{"TABLE_CATEGORY":"（推計値）","TABLE_NAME":"定年制の状況","TABLE_EXPLANATION":"１\u3000事務・技術関係職種の従業員がいる企業41,314社について集計した。２\u3000「定年年齢」内の数値は定年制がある企業を100とした場合の割合を示す。"}'
    """  # noqa: E501

    table_category: Optional[str | int] = None
    table_name: str
    table_explanation: Optional[str] = None


class DetailedDescription(BaseModel):
    tabulation_category_explanation: Optional[str] = None
    tabulation_sub_category_explanation1: Optional[str] = None
    tabulation_sub_category_explanation2: Optional[str] = None


class TableInf(BaseModel):
    id: str
    stat_name: StatName
    gov_org: GovOrg
    statistics_name: str
    title: Title | str
    cycle: str
    survey_date: str | int
    open_date: str
    small_area: int
    collect_area: str
    main_category: MainCategory
    sub_category: SubCategory
    overall_total_number: int
    updated_date: str
    statistics_name_spec: StatisticsNameSpec
    description: str | DetailedDescription
    title_spec: TitleSpec


class ResultInf(BaseModel):
    total_number: Optional[int] = None
    from_number: int
    to_number: int


class DatalistInf(BaseModel):
    number: int
    result_inf: ResultInf
    table_inf: list[TableInf]


class Parameter(BaseModel):
    lang: str
    data_format: str


class Result(BaseModel):
    status: int
    error_msg: str
    date: str


class GetStatsList(BaseModel):
    result: Result
    parameter: Parameter
    datalist_inf: DatalistInf


class GetStatsListResponse(BaseModel):
    get_stats_list: GetStatsList


class Class(BaseModel):
    code: str
    name: str
    level: Optional[str] = None
    unit: Optional[str] = None
    parent_code: Optional[str] = None


class ClassObj(BaseModel):
    id: str
    name: str
    class_: list[Class] | Class


class ClassInf(BaseModel):
    class_obj: list[ClassObj]


class MetadataInf(BaseModel):
    table_inf: TableInf
    class_inf: ClassInf


class GetMetaInfo(BaseModel):
    result: Result
    parameter: Parameter
    metadata_inf: MetadataInf


class GetMetaInfoResponse(BaseModel):
    get_meta_info: GetMetaInfo


class Note(BaseModel):
    char: str
    value: str


class Value(BaseModel):
    cat01: str
    cat02: str
    time: str
    unit: str
    value: str


class DataInf(BaseModel):
    note: Note
    value_: list[Value]


class StatisticalData(BaseModel):
    result_inf: ResultInf
    table_inf: TableInf
    class_inf: ClassInf
    data_inf: DataInf


class GetStatsData(BaseModel):
    result: Result
    parameter: Parameter
    statistical_data: StatisticalData


class GetStatsDataResponse(BaseModel):
    get_stats_data: GetStatsData
