# Publishing Guide - Python SDK

This document describes how to build, version, and publish the OursPrivacy Python SDK to PyPI.

## Overview

- **Package Name**: `oursprivacy-client`
- **Target Registry**: PyPI (https://pypi.org/)
- **Current Status**: ✅ Published (https://pypi.org/project/oursprivacy-client/)
- **Build System**: setuptools + pyproject.toml
- **Publishing**: Manual with automated release script

## Prerequisites

### Tools Required
- Python 3.9+
- pip and setuptools
- build tools: `python -m pip install build twine`
- Access to PyPI account with publishing permissions

### Authentication Setup
1. **PyPI Account**: Create/access account at https://pypi.org/
2. **API Token**: Generate API token from https://pypi.org/manage/account/token/
3. **Configure credentials**:
   ```bash
   # Option 1: Using .pypirc file
   cat > ~/.pypirc << EOF
   [distutils]
   index-servers = pypi

   [pypi]
   username = __token__
   password = pypi-YOUR_API_TOKEN_HERE
   EOF

   # Option 2: Using environment variable
   export TWINE_PASSWORD=pypi-YOUR_API_TOKEN_HERE
   export TWINE_USERNAME=__token__
   ```

## Version Management

### Current Version
Check current version in multiple places:
- `setup.py`: `VERSION = "1.0.1"`
- `pyproject.toml`: `version = "1.0.1"`

### Automated Versioning
The repository includes `scripts/release.sh` which handles version management:

```bash
# Run the release script
bash ./scripts/release.sh
```

The script will:
1. Read current version from `setup.py`
2. Prompt for next version
3. Prompt for release notes  
4. Update version in `setup.py`
5. Update `CHANGELOG.md`
6. Commit changes and create git tag
7. Push to GitHub
8. Display PyPI publishing reminder

## Building the Package

### Local Build
```bash
# Install build dependencies
pip install build wheel twine

# Clean previous builds
rm -rf dist/ build/ *.egg-info/

# Build source distribution and wheel
python -m build

# This creates:
# dist/oursprivacy_client-X.X.X.tar.gz
# dist/oursprivacy_client-X.X.X-py3-none-any.whl
```

### Development Installation
```bash
# Install in development mode
pip install -e .

# Or with test dependencies
pip install -e ".[dev]"
```

## Publishing Process

### Automated Release (Recommended)

Use the provided release script:

```bash
# Make sure you're on main branch
git checkout main
git pull origin main

# Run release script
bash ./scripts/release.sh

# Follow prompts for version and release notes
# After script completes, publish to PyPI:
python -m build
twine upload dist/*
```

### Manual Publishing Process

1. **Update Version**:
   ```bash
   # Edit setup.py
   sed -i '' 's/VERSION = "[^"]*"/VERSION = "1.0.2"/' setup.py
   
   # Also update pyproject.toml if it contains version
   # Edit manually or use similar sed command
   ```

2. **Build Package**:
   ```bash
   rm -rf dist/ build/
   python -m build
   ```

3. **Test Package Locally**:
   ```bash
   # Test installation
   pip install dist/oursprivacy_client-*.whl
   
   # Test import
   python -c "import oursprivacy_client; print('Import successful')"
   ```

4. **Upload to PyPI**:
   ```bash
   # Upload to Test PyPI first (recommended)
   twine upload --repository testpypi dist/*
   
   # Test installation from Test PyPI
   pip install --index-url https://test.pypi.org/simple/ oursprivacy-client
   
   # If everything works, upload to production PyPI
   twine upload dist/*
   ```

5. **Tag and Push**:
   ```bash
   git add setup.py CHANGELOG.md
   git commit -m "chore: release v1.0.2"
   git tag -a v1.0.2 -m "Release v1.0.2 - Description"
   git push origin main
   git push origin v1.0.2
   ```

## Package Configuration

### setup.py Configuration
```python
NAME = "oursprivacy-client"
VERSION = "1.0.1"
PYTHON_REQUIRES = ">= 3.9"
REQUIRES = [
    "urllib3 >= 2.1.0, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Ours",
    author="OpenAPI Generator community",
    author_email="support@oursprivacy.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Ours"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description_content_type='text/markdown',
    python_requires=PYTHON_REQUIRES,
)
```

### pyproject.toml Configuration
```toml
[project]
name = "oursprivacy_client"
version = "1.0.1"
description = "Ours"
authors = [
  {name = "OpenAPI Generator Community", email = "support@oursprivacy.com"},
]
license = "MIT"
readme = "README.md"
keywords = ["OpenAPI", "OpenAPI-Generator", "Ours"]
requires-python = ">=3.9"

dependencies = [
  "urllib3 (>=2.1.0,<3.0.0)",
  "python-dateutil (>=2.8.2)",
  "pydantic (>=2)",
  "typing-extensions (>=4.7.1)"
]

[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
```

## Code Generation

This SDK is auto-generated from OpenAPI specifications. The generation process is not included in this repo, but typically involves:

```bash
# If OpenAPI generator is available
openapi-generator-cli generate \
  -i ./openapi.json \
  -g python \
  -o . \
  --additional-properties=packageName=oursprivacy_client,projectName=oursprivacy-client
```

**Important**: After regeneration, verify version numbers and package settings.

## Testing

### Run Tests
```bash
# Install test dependencies
pip install -e ".[dev]"

# Run tests with pytest
pytest

# Run with coverage
pytest --cov=oursprivacy_client

# Run with tox (multiple Python versions)
tox
```

### Type Checking
```bash
# Install mypy
pip install mypy

# Run type checking
mypy oursprivacy_client
```

## Version Guidelines

Follow semantic versioning:
- **Patch** (1.0.1): Bug fixes, small updates
- **Minor** (1.1.0): New features, backwards compatible
- **Major** (2.0.0): Breaking changes

## Troubleshooting

### Common Issues

1. **"Package already exists"**: Version number already published
2. **"Invalid credentials"**: Check PyPI token and configuration
3. **"Upload failed"**: May be network issue, try again
4. **"Metadata issues"**: Validate setup.py and pyproject.toml

### Validation Steps
```bash
# Check package metadata
python setup.py check

# Validate built package
twine check dist/*

# Test installation
pip install oursprivacy-client

# Test import
python -c "import oursprivacy_client; print(oursprivacy_client.__version__)"
```

### Environment Issues
```bash
# Check Python version
python --version

# Check pip version  
pip --version

# Upgrade build tools
pip install --upgrade build twine setuptools wheel
```

## Security Considerations

- Store PyPI tokens securely (use environment variables)
- Enable 2FA on PyPI account
- Regularly audit dependencies: `pip-audit`
- Sign releases with GPG (optional but recommended)

## CI/CD Integration

### GitHub Actions Example
```yaml
# .github/workflows/publish.yml
name: Publish to PyPI
on:
  push:
    tags:
      - 'v*'

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.9'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install build twine
      
      - name: Build package
        run: python -m build
      
      - name: Publish to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: twine upload dist/*
```

## Development Workflow

### Setup Development Environment
```bash
# Clone repository
git clone https://github.com/with-ours/ingest-sdk-python.git
cd ingest-sdk-python

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest
```

## Support

- **Documentation**: https://docs.oursprivacy.com/docs/python#/
- **PyPI Package**: https://pypi.org/project/oursprivacy-client/
- **Issues**: https://github.com/with-ours/ingest-sdk-python/issues
- **Repository**: https://github.com/with-ours/ingest-sdk-python

## Resources

- [PyPI Documentation](https://packaging.python.org/)
- [Python Packaging Guide](https://packaging.python.org/tutorials/packaging-projects/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Semantic Versioning](https://semver.org/)