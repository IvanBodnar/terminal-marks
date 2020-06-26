from pathlib import Path
from typing import Union


class Mark:
    def __init__(self):
        self._mark_name: Union[str, None] = None
        self._directory: Union[Path, None] = None

    @property
    def mark_name(self) -> str:
        return self._mark_name

    @mark_name.setter
    def mark_name(self, name: str):
        self._mark_name = name

    @property
    def directory(self) -> Path:
        return self._directory

    @directory.setter
    def directory(self, directory_path: str):
        self._directory = Path(directory_path)
