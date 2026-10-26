FROM ghcr.io/astral-sh/uv:0.13.5 AS uv
FROM mcr.microsoft.com/devcontainers/python:3.13-bookworm
COPY --from=uv /uv /uvx /usr/local/bin/
ENV UV_MANAGED_PYTHON=true
USER vscode
RUN echo "[[ -d .venv ]] && source .venv/bin/activate || export PATH=\$PATH" >> /home/vscode/.bashrc
