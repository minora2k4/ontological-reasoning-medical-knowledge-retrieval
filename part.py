from __future__ import annotations
from typing import List
from dataclasses import dataclass, field


@dataclass
class Part:
    partID: str
    text: str
    child: list[Part] = field(default_factory=list)