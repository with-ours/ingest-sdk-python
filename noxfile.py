import nox


@nox.session(reuse_venv=True, name="test-pydantic-v1", venv_backend="uv")
def test_pydantic_v1(session: nox.Session) -> None:
    session.install("-r", "requirements-dev.lock")
    session.install("pydantic==1.10.26")

    session.run("pytest", "--showlocals", "--ignore=tests/functional", *session.posargs)
