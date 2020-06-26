from os import getcwd
from pathlib import Path

import pytest

from terminal_marks.api.input import Input, get_input


@pytest.fixture(scope='function')
def input_instance() -> Input:
    return Input(cwd_fn=getcwd)


def test_input_init(input_instance: Input):
    assert input_instance._mark_name is None
    assert input_instance._directory is None
    assert input_instance._get_cwd_fn == getcwd


def test_mark_name(input_instance: Input):
    assert input_instance.mark_name is None
    input_instance.mark_name = 'test'
    assert input_instance.mark_name == 'test'


def test_directory(input_instance: Input):
    assert input_instance.directory is None
    input_instance.read_cwd()
    assert isinstance(input_instance.directory, Path)
    assert input_instance.directory.as_posix() == getcwd()


def test_get_input_factory_fn():
    _input = get_input()
    assert isinstance(_input, Input)
    assert _input._get_cwd_fn == getcwd
