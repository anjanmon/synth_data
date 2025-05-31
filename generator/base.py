from typing import Optional, Dict, Any
from abc import ABC, abstractmethod

class BaseGenerator(ABC):
    def __init__(self, name:str, params:Optional[Dict[str,Any]]=None):
        self.name = name
        self.parms = params or {}

    def __repr__(self):
        return f"{self.__class__.__name__}"