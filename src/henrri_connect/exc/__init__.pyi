"""Stub de module d'exceptions personnalisées pour la bibliothèque henrri-connect."""
class HenrriError(Exception): ...   #pylint: disable=C0115

class HenrriHTTPError(HenrriError): #pylint: disable=C0115
    status_code: int
    body: object | None
    def __init__(self, status_code: int, message: str, body: object | None = ...) -> None: ... # pylint: disable=W0613

class HenrriAuthError(HenrriHTTPError): ... #pylint: disable=C0115
class HenrriForbiddenError(HenrriHTTPError): ...    #pylint: disable=C0115
class HenrriNotFoundError(HenrriHTTPError): ... #pylint: disable=C0115
class HenrriValidationError(HenrriHTTPError): ...   #pylint: disable=C0115
class HenrriServerError(HenrriHTTPError): ...   #pylint: disable=C0115
