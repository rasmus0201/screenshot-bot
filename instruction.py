from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, LetterCase
from typing import List
from typing import Optional

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class Instruction:
    title: str
    base_url: str
    device: str = "macbook13"
    headless: bool = False
    multi_thread: bool = True
    max_threads: int = 3
    pages: Optional[List[str]] = field(default_factory=list)
    levels: Optional[List[str]] = field(default_factory=list)
