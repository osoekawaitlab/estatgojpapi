from typing import Dict, List

from .models import StatisticalData


def process_statistical_data(data: StatisticalData) -> List[Dict[str, str]]:
    category_name_map = {d.id: d.name for d in data.class_inf.class_obj}
    code_detail_map = {
        d.id: (
            {c.code: c.model_dump() for c in (d.class_ if isinstance(d.class_, list) else [d.class_])}
            if d.class_
            else {}
        )
        for d in data.class_inf.class_obj
    }
    return [
        {category_name_map.get(k, k): code_detail_map.get(k, {v: v})[v] for k, v in val.model_dump().items()}
        for val in data.data_inf.value_
    ]
