#!/usr/bin/env bash
set -e

# 1. Read current version from setup.py using Python regex
CURRENT_VERSION=$(python3 -c "import re; f=open('setup.py').read(); m = re.search(r'VERSION\s*=\s*[\"']([^\"']+)[\"']', f); print(m.group(1) if m else '0.0.0')")
echo "Current version is: $CURRENT_VERSION"

# 2. Prompt for the next version
read -rp "Enter the next version (e.g., 1.0.1): " NEXT_VERSION

# 3. Prompt for release notes
echo "Enter release notes (press ENTER, then CTRL+D when done):"
RELEASE_NOTES=$(cat)

# 4. Update setup.py with the new version using sed (macOS version)
sed -i '' -E "s/^(VERSION\s*=\s*['\"])[^'\"]+(['\"])/\1${NEXT_VERSION}\2/" setup.py

echo "Updated setup.py to version ${NEXT_VERSION}"

# 5. Update or create CHANGELOG.md
if [ ! -f CHANGELOG.md ]; then
  echo "# Changelog" > CHANGELOG.md
fi

{
  echo ""
  echo "## [${NEXT_VERSION}] - $(date +%Y-%m-%d)"
  echo ""
  echo "${RELEASE_NOTES}"
} >> CHANGELOG.md

# 6. Commit changes and create a Git tag with the release notes
git add setup.py CHANGELOG.md
git commit -m "chore: release v${NEXT_VERSION}

${RELEASE_NOTES}"
git tag -a "v${NEXT_VERSION}" -m "${RELEASE_NOTES}"

# 7. Push the commit and tag
git push origin main
git push origin "v${NEXT_VERSION}"

# 8. PyPI Reminder
echo "Release v${NEXT_VERSION} is ready!"
echo "Remember to build and upload your package to PyPI (e.g., using 'python -m build' and 'twine upload dist/*')."