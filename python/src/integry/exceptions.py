class NotFound(Exception):
    pass


class FunctionCallError(Exception):
    errors = list[str]

    def __init__(self, message: str, errors: list[str]):
        self.errors = errors
        super().__init__(message)

    def __str__(self) -> str:
        return super().__str__() + f"\nErrors: {self.errors}"
