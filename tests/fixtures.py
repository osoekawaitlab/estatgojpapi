sample_get_stat_list_json = {
    "GET_STATS_LIST": {
        "RESULT": {"STATUS": 0, "ERROR_MSG": "正常に終了しました。", "DATE": "2024-05-28T21:53:34.506+09:00"},
        "PARAMETER": {"LANG": "J", "DATA_FORMAT": "J"},
        "DATALIST_INF": {
            "NUMBER": 3,
            "RESULT_INF": {"FROM_NUMBER": 1, "TO_NUMBER": 3},
            "TABLE_INF": [
                {
                    "@id": "0003288322",
                    "STAT_NAME": {"@code": "00020111", "$": "民間企業の勤務条件制度等調査"},
                    "GOV_ORG": {"@code": "00020", "$": "＊＊＊"},
                    "STATISTICS_NAME": "＊＊＊ 統計表 １　＊＊＊の状況",
                    "TITLE": {"@no": "1", "$": "（推計値） ＊＊＊の状況"},
                    "CYCLE": "年次",
                    "SURVEY_DATE": "201601-201612",
                    "OPEN_DATE": "2019-03-20",
                    "SMALL_AREA": 0,
                    "COLLECT_AREA": "該当なし",
                    "MAIN_CATEGORY": {"@code": "03", "$": "労働・賃金"},
                    "SUB_CATEGORY": {"@code": "02", "$": "賃金・労働条件"},
                    "OVERALL_TOTAL_NUMBER": 25,
                    "UPDATED_DATE": "2019-03-30",
                    "STATISTICS_NAME_SPEC": {
                        "TABULATION_CATEGORY": "＊＊＊",
                        "TABULATION_SUB_CATEGORY1": "統計表",
                        "TABULATION_SUB_CATEGORY2": "１　＊＊＊の状況",
                    },
                    "DESCRIPTION": "",
                    "TITLE_SPEC": {
                        "TABLE_CATEGORY": "（推計値）",
                        "TABLE_NAME": "＊＊＊の状況",
                        "TABLE_EXPLANATION": "１　＊＊＊の従業員がいる企業41,314社について集計した。２　「＊＊＊」内の数値は＊＊＊企業を100とした場合の割合を示す。",
                    },
                },
                {
                    "@id": "0003288323",
                    "STAT_NAME": {"@code": "00020112", "$": "家計調査"},
                    "GOV_ORG": {"@code": "00021", "$": "＊＊＊"},
                    "STATISTICS_NAME": "家計調査 統計表 ２　＊＊＊の状況",
                    "TITLE": {"@no": "2", "$": "（推計値） ＊＊＊の状況"},
                    "CYCLE": "月次",
                    "SURVEY_DATE": "202301-202312",
                    "OPEN_DATE": "2024-01-20",
                    "SMALL_AREA": 0,
                    "COLLECT_AREA": "全国",
                    "MAIN_CATEGORY": {"@code": "04", "$": "家計・消費"},
                    "SUB_CATEGORY": {"@code": "01", "$": "家計"},
                    "OVERALL_TOTAL_NUMBER": 12,
                    "UPDATED_DATE": "2024-02-10",
                    "STATISTICS_NAME_SPEC": {
                        "TABULATION_CATEGORY": "＊＊＊",
                        "TABULATION_SUB_CATEGORY1": "統計表",
                        "TABULATION_SUB_CATEGORY2": "２　＊＊＊の状況",
                    },
                    "DESCRIPTION": "",
                    "TITLE_SPEC": {
                        "TABLE_CATEGORY": "（推計値）",
                        "TABLE_NAME": "＊＊＊の状況",
                        "TABLE_EXPLANATION": "１　全国の＊＊＊を対象に、月次で＊＊＊状況を調査。２　＊＊＊の平均値と中央値を算出。",
                    },
                },
                {
                    "@id": "0003288324",
                    "STAT_NAME": {"@code": "00020113", "$": "労働力調査"},
                    "GOV_ORG": {"@code": "00022", "$": "＊＊＊"},
                    "STATISTICS_NAME": "労働力調査 統計表 ３　＊＊＊の推移",
                    "TITLE": {"@no": "3", "$": "（推計値） ＊＊＊の推移"},
                    "CYCLE": "年次",
                    "SURVEY_DATE": "202101-202112",
                    "OPEN_DATE": "2022-06-20",
                    "SMALL_AREA": 1,
                    "COLLECT_AREA": "都道府県別",
                    "MAIN_CATEGORY": {"@code": "03", "$": "労働・賃金"},
                    "SUB_CATEGORY": {"@code": "01", "$": "労働力人口"},
                    "OVERALL_TOTAL_NUMBER": 47,
                    "UPDATED_DATE": "2022-07-01",
                    "STATISTICS_NAME_SPEC": {
                        "TABULATION_CATEGORY": "＊＊＊",
                        "TABULATION_SUB_CATEGORY1": "統計表",
                        "TABULATION_SUB_CATEGORY2": "３　＊＊＊の推移",
                    },
                    "DESCRIPTION": "",
                    "TITLE_SPEC": {
                        "TABLE_CATEGORY": "（推計値）",
                        "TABLE_NAME": "＊＊＊の推移",
                        "TABLE_EXPLANATION": "１　＊＊＊の推移を調査。２　年次で＊＊＊を分析。",
                    },
                },
            ],
        },
    }
}


sample_get_meta_info_json = {
    "GET_META_INFO": {
        "RESULT": {"STATUS": 0, "ERROR_MSG": "正常に終了しました。", "DATE": "2024-05-29T20:53:56.923+09:00"},
        "PARAMETER": {"LANG": "J", "STATS_DATA_ID": "0000000000", "DATA_FORMAT": "J"},
        "METADATA_INF": {
            "TABLE_INF": {
                "@id": "0000000000",
                "STAT_NAME": {"@code": "00000000", "$": "サンプル調査"},
                "GOV_ORG": {"@code": "00000", "$": "サンプル省庁"},
                "STATISTICS_NAME": "サンプル調査 若者に対する質問",
                "TITLE": "サンプル Q1a　あなたは、日常的にどのくらいの時間をスマホを使って過ごしますか。　性別",
                "CYCLE": "年度次",
                "SURVEY_DATE": "202104-202203",
                "OPEN_DATE": "2024-05-29",
                "SMALL_AREA": 0,
                "COLLECT_AREA": "全国",
                "MAIN_CATEGORY": {"@code": "99", "$": "教育・文化・スポーツ・生活"},
                "SUB_CATEGORY": {"@code": "99", "$": "文化・スポーツ・生活"},
                "OVERALL_TOTAL_NUMBER": 30,
                "UPDATED_DATE": "2024-05-30",
                "STATISTICS_NAME_SPEC": {
                    "TABULATION_CATEGORY": "サンプル調査",
                    "TABULATION_SUB_CATEGORY1": "若者に対する質問",
                },
                "DESCRIPTION": "",
                "TITLE_SPEC": {
                    "TABLE_CATEGORY": "若者",
                    "TABLE_NAME": "Q1a　あなたは、日常的にどのくらいの時間をスマホを使って過ごしますか。　性別",
                },
            },
            "CLASS_INF": {
                "CLASS_OBJ": [
                    {
                        "@id": "cat01",
                        "@name": "スマホ使用時間",
                        "CLASS": [
                            {"@code": "100", "@name": "総数", "@level": "1", "@unit": "人"},
                            {"@code": "110", "@name": "30分くらい", "@level": "2", "@unit": "%", "@parentCode": "100"},
                            {"@code": "120", "@name": "1時間くらい", "@level": "2", "@unit": "%", "@parentCode": "100"},
                            {"@code": "130", "@name": "2時間くらい", "@level": "2", "@unit": "%", "@parentCode": "100"},
                            {"@code": "140", "@name": "3時間くらい", "@level": "2", "@unit": "%", "@parentCode": "100"},
                            {"@code": "150", "@name": "4時間くらい", "@level": "2", "@unit": "%", "@parentCode": "100"},
                            {"@code": "160", "@name": "5時間以上", "@level": "2", "@unit": "%", "@parentCode": "100"},
                            {
                                "@code": "170",
                                "@name": "まったく使わない",
                                "@level": "2",
                                "@unit": "%",
                                "@parentCode": "100",
                            },
                            {"@code": "180", "@name": "わからない", "@level": "2", "@unit": "%", "@parentCode": "100"},
                        ],
                    },
                    {
                        "@id": "cat02",
                        "@name": "性別",
                        "CLASS": [
                            {"@code": "100", "@name": "総数", "@level": "1"},
                            {"@code": "110", "@name": "男性", "@level": "2", "@parentCode": "100"},
                            {"@code": "120", "@name": "女性", "@level": "2", "@parentCode": "100"},
                        ],
                    },
                    {
                        "@id": "time",
                        "@name": "時間軸(年度次)",
                        "CLASS": {"@code": "2021000000", "@name": "2021年度", "@level": "1"},
                    },
                ]
            },
        },
    }
}
