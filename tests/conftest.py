import http.server
import json
import socketserver
import threading
from typing import Generator
from urllib.parse import parse_qs, urlparse

from pytest import fixture
from pytest_mock import MockerFixture

from estatgojpapi.storages.base import BaseStorage

from .fixtures import (
    sample_get_meta_info_json,
    sample_get_stat_list_json,
    sample_get_stats_data_0_json,
    sample_get_stats_data_1_json,
    sample_get_stats_data_2_json,
    sample_get_stats_data_json,
)


@fixture
def app_id_for_test() -> Generator[str, None, None]:
    yield "test_app_id"


@fixture
def http_server_fixture(app_id_for_test: str) -> Generator[str, None, None]:

    class Handler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self) -> None:
            parsed = urlparse(self.path)
            query = parse_qs(parsed.query)
            path = parsed.path
            if "appId" not in query or query["appId"][0] != app_id_for_test:
                self.send_response(403)
                self.send_header("Content-type", "text/plain; charset=utf-8")
                self.end_headers()
                self.wfile.write("Forbidden".encode("utf-8"))
                return
            if path == "/getMetaInfo":
                if "statsDataId" not in query or query["statsDataId"][0] != "0000000000":
                    self.send_response(400)
                    self.send_header("Content-type", "text/plain; charset=utf-8")
                    self.end_headers()
                    self.wfile.write("Bad Request".encode("utf-8"))
                    return
                self.send_response(200)
                self.send_header("Content-type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps(sample_get_meta_info_json).encode("utf-8"))
            elif path == "/getStatsData":
                if "statsDataId" not in query or query["statsDataId"][0] not in ("0000000000", "0000000001"):
                    self.send_response(400)
                    self.send_header("Content-type", "text/plain; charset=utf-8")
                    self.end_headers()
                    self.wfile.write("Bad Request".encode("utf-8"))
                    return
                if query["statsDataId"][0] == "0000000001":
                    if "startPosition" not in query:
                        self.send_response(200)
                        self.send_header("Content-type", "application/json; charset=utf-8")
                        self.end_headers()
                        self.wfile.write(json.dumps(sample_get_stats_data_0_json).encode("utf-8"))
                        return
                    if query["startPosition"][0] == "14":
                        self.send_response(200)
                        self.send_header("Content-type", "application/json; charset=utf-8")
                        self.end_headers()
                        self.wfile.write(json.dumps(sample_get_stats_data_1_json).encode("utf-8"))
                        return
                    if query["startPosition"][0] == "27":
                        self.send_response(200)
                        self.send_header("Content-type", "application/json; charset=utf-8")
                        self.end_headers()
                        self.wfile.write(json.dumps(sample_get_stats_data_2_json).encode("utf-8"))
                        return
                elif query["statsDataId"][0] == "0000000000":
                    self.send_response(200)
                    self.send_header("Content-type", "application/json; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(json.dumps(sample_get_stats_data_json).encode("utf-8"))
                else:
                    self.send_response(400)
                    self.send_header("Content-type", "text/plain; charset=utf-8")
                    self.end_headers()
                    self.wfile.write("Bad Request".encode("utf-8"))
            elif path == "/getStatsList":
                self.send_response(200)
                self.send_header("Content-type", "application/json; charset=utf-8")
                self.end_headers()
                self.wfile.write(json.dumps(sample_get_stat_list_json).encode("utf-8"))
            else:
                print(f"404 Not Found: {self.path}")
                self.send_response(404)
                self.send_header("Content-type", "text/plain; charset=utf-8")
                self.end_headers()
                self.wfile.write("Not Found".encode("utf-8"))

    with socketserver.TCPServer(("localhost", 0), Handler) as httpd:
        port = httpd.server_address[1]
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.start()
        yield f"http://localhost:{port}"
        httpd.shutdown()
        server_thread.join()


@fixture
def mock_storage(mocker: MockerFixture) -> Generator[BaseStorage, None, None]:
    yield mocker.MagicMock(spec=BaseStorage)
