### How to deploy a new version

After making changes to the codebase,
1. Update the version number in `pyproject.toml`
2. Run `./deploy.sh` to publish the new version to PyPI.
   1. This will require you to have `twine` and `build` installed, and PyPI credentials set up in your environment
