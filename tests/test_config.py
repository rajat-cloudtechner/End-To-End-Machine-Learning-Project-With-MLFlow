from src.mlproject.utils.common import read_yaml

def test_read_yaml():
    config = read_yaml("config/config.yaml")
    assert isinstance(config, dict)
