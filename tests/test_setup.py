import pyconst


def test_get_version():
    # (1, 0, 5)
    version = pyconst.__version__
    str_version = '.'.join(map(str, version))
    assert pyconst.get_version() == str_version
