import os
import sys
from pdb import set_trace as pst

sys.path.append(os.path.join(os.path.abspath(__file__), ".."))
from download import hello, load_json


def test_hello_world():
    assert hello() == "hello world"


def test_load_json():
    assert type(load_json("seeeeeeed.json")) is dict
