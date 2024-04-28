from app.dependencies import dependencies, static_paths


def test_dependencies():
    deps = dependencies()
    for key, value in deps.items():
        assert isinstance(key, str)
        assert isinstance(value, list | dict)

        for item in value:
            assert isinstance(item, str | dict)


def test_static_paths():
    sp = static_paths()
    assert isinstance(sp, dict)
    for key, value in sp.items():
        assert isinstance(key, str)
        assert isinstance(value, str)
