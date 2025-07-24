from src.mlproject.utils.common import read_yaml
from pathlib import Path


def test_read_yaml():
    config = read_yaml(Path("config/config.yaml"))
    assert isinstance(config, dict)
