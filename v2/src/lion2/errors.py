from typing import Any

from lionfuncs.errors import LionError


class vynixError(LionError):
    """Base class for all vynix errors."""

    pass


class ItemNotFoundError(vynixError):
    """Raised when an item is not found in a collection."""

    def __init__(
        self,
        message,
        *,
        items: Any = None,
    ):
        if items is not None:
            items = str(items)
            if len(items) > 50:
                items = f"{items[:50]}..."
            message = f"{message} (items: {items})"

        super().__init__(message)


class ItemExistsError(vynixError):
    """Raised when an item already exists in a collection."""

    def __init__(
        self,
        message,
        *,
        items: Any = None,
    ):
        if items is not None:
            items = str(items)
            if len(items) > 50:
                items = f"{items[:50]}..."
            message = f"{message} (items: {items})"

        super().__init__(message)


class ToolParameterValidationError(vynixError):
    """Custom exception for tool parameter validation errors."""

    pass
