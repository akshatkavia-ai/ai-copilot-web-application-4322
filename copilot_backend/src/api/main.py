# This thin wrapper keeps compatibility with existing tooling generating openapi.json
from app.main import app  # re-export for generate_openapi.py tooling

# Explicitly export app to avoid linter 'imported but unused' warning
__all__ = ["app"]
