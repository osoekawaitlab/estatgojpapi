import re

import estatgojpapi


def test_estatgojpapi_has_version() -> None:
    assert re.match(r"\d+\.\d+\.\d+", estatgojpapi.__version__)
