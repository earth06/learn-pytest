import pytest


def test_cfg(cfg):
    assert cfg.get_configA()==1
