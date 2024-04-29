from dataclasses import dataclass
from typing import List, Dict


@dataclass(frozen=True, slots=True)
class ResponseMessage:
    success: bool
    message: str
    data: List | Dict | None


