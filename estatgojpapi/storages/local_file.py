from pydantic import DirectoryPath, FilePath, NewPath

from ..models import GetMetaInfoResponse, GetStatsDataResponse, GetStatsListResponse
from ..settings import NewOrExistingDirectoryPath
from .base import BaseStorage

NewOrExistingFilePath = FilePath | NewPath


class LocalFileStorage(BaseStorage):
    def __init__(self, path: NewOrExistingDirectoryPath):
        self._path = path

    @property
    def _root_dir(self) -> DirectoryPath:
        if not self._path.exists():
            self._path.mkdir(parents=True)
        if not self._path.is_dir():
            raise ValueError(f"Path is not a directory: {self._path}")
        return self._path

    @property
    def _meta_info_path(self) -> DirectoryPath:
        if not (self._root_dir / "meta_info").exists():
            (self._root_dir / "meta_info").mkdir()
        if not (self._root_dir / "meta_info").is_dir():
            raise ValueError(f"Path is not a directory: {self._root_dir / 'meta_info'}")
        return self._root_dir / "meta_info"

    @property
    def _stats_data_path(self) -> DirectoryPath:
        if not (self._root_dir / "stats_data").exists():
            (self._root_dir / "stats_data").mkdir()
        if not (self._root_dir / "stats_data").is_dir():
            raise ValueError(f"Path is not a directory: {self._root_dir / 'stats_data'}")
        return self._root_dir / "stats_data"

    @property
    def _stats_list_path(self) -> NewOrExistingFilePath:
        return self._root_dir / "stats_list.json"

    def has_stats_list(self) -> bool:
        return self._stats_list_path.exists()

    def get_stats_list(self) -> GetStatsListResponse:
        try:
            with open(self._stats_list_path, "r", encoding="utf-8") as file:
                return GetStatsListResponse.model_validate_json(file.read())
        except FileNotFoundError:
            raise KeyError("Stats list not found")

    def store_stats_list(self, stats_list: GetStatsListResponse) -> None:
        with open(self._stats_list_path, "w", encoding="utf-8") as file:
            file.write(stats_list.model_dump_json())

    def has_meta_info(self, stats_data_id: str) -> bool:
        return (self._meta_info_path / f"{stats_data_id}.json").exists()

    def get_meta_info(self, stats_data_id: str) -> GetMetaInfoResponse:
        try:
            with open(self._meta_info_path / f"{stats_data_id}.json", "r", encoding="utf-8") as file:
                return GetMetaInfoResponse.model_validate_json(file.read())
        except FileNotFoundError:
            raise KeyError("Meta info not found")

    def store_meta_info(self, meta_info: GetMetaInfoResponse) -> None:
        with open(
            self._meta_info_path / f"{meta_info.get_meta_info.metadata_inf.table_inf.id}.json", "w", encoding="utf-8"
        ) as file:
            file.write(meta_info.model_dump_json())

    def has_stats_data(self, stats_data_id: str) -> bool:
        return (self._stats_data_path / f"{stats_data_id}.json").exists()

    def get_stats_data(self, stats_data_id: str) -> GetStatsDataResponse:
        try:
            with open(self._stats_data_path / f"{stats_data_id}.json", "r", encoding="utf-8") as file:
                return GetStatsDataResponse.model_validate_json(file.read())
        except FileNotFoundError:
            raise KeyError("Stats data not found")

    def store_stats_data(self, stats_data: GetStatsDataResponse) -> None:
        with open(
            self._stats_data_path / f"{stats_data.get_stats_data.statistical_data.table_inf.id}.json",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(stats_data.model_dump_json())
