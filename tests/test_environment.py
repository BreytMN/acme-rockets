from app.environment import static_paths


def test_static_paths():
    sp = static_paths()
    assert isinstance(sp, dict)
    for key, value in sp.items():
        assert isinstance(key, str)
        assert isinstance(value, str)
