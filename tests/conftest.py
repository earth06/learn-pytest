import pytest

from mypackage.configure import Configure
import json

@pytest.fixture
def cfg():
    with open("./cfg/config.json", "rt") as f:
        cfgdata = json.load(f)
    with open("./cfg/params.json", "rt") as f:
        paramsdata = json.load(f)
    # 事前にインスタンスの生成をfixtureにやらせることができる
    # テストコードではこのインスタンスに対してテストを実施すればよい
    fix_config =  Configure(cfgdata, paramsdata)
    return fix_config

