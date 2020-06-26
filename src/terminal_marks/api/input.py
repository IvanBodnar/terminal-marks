from os import getcwd
from pathlib import Path
from typing import Union, Callable


class Input:
    def __init__(self, cwd_fn: Callable[[], str]):
        self._mark_name: Union[str, None] = None
        self._directory: Union[Path, None] = None
        self._get_cwd_fn = cwd_fn

    @property
    def mark_name(self) -> str:
        return self._mark_name

    @mark_name.setter
    def mark_name(self, name: str):
        self._mark_name = name

    @property
    def directory(self) -> Path:
        return self._directory

    def read_cwd(self):
        self._directory = Path(getcwd())


def get_input() -> Input:
    return Input(cwd_fn=getcwd)
