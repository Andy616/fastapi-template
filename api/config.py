from schemas.response import ErrorResponse


Responses = {
    400: {"model": ErrorResponse},
    422: {"model": ErrorResponse},
    404: {"model": ErrorResponse},
    500: {"model": ErrorResponse},
}
