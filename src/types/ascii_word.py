from typing_extensions import Annotated
from pydantic.functional_validators import AfterValidator


def check_ascii(value: str) -> str:
    ord_values = [ord(r) for r in value]
    invalid_values = [hex(r) for r in ord_values if r < 0 or r > 255]

    assert len(invalid_values) == 0, f"{invalid_values} are invalid Ascii values"
    return value


AsciiWord = Annotated[str, AfterValidator(check_ascii)]
