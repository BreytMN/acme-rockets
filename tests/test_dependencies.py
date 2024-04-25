from app.dependencies import dependencies


def test_dependencies():
    deps = dependencies()
    for key, value in deps.items():
        assert isinstance(key, str)
        assert isinstance(value, list)

        for item in value:
            assert isinstance(item, dict)
