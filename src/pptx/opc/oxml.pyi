from typing import Callable, Dict, List, Optional

from pptx.opc.packuri import PackURI
from pptx.oxml.xmlchemy import BaseOxmlElement

nsmap: Dict[str, str]

def oxml_to_encoded_bytes(
    element: BaseOxmlElement, encoding: str = ..., pretty_print: bool = ..., standalone: Optional[bool] = ...
) -> bytes: ...
def oxml_tostring(
    elm: BaseOxmlElement,
    encoding: Optional[str] = ...,
    pretty_print: bool = ...,
    standalone: Optional[bool] = ...,
) -> bytes: ...
def serialize_part_xml(part_elm: BaseOxmlElement) -> bytes: ...

class CT_Default(BaseOxmlElement):
    extension: str
    contentType: str

class CT_Override(BaseOxmlElement):
    partName: str
    contentType: str

class CT_Relationship(BaseOxmlElement):
    rId: str
    reltype: str
    target_ref: str
    targetMode: str
    @classmethod
    def new(cls, rId: str, reltype: str, target_ref: str, target_mode: str = ...) -> "CT_Relationship": ...

class CT_Relationships(BaseOxmlElement):
    relationship_lst: List[CT_Relationship]
    _insert_relationship: Callable[[CT_Relationship], CT_Relationship]
    def add_rel(self, rId: str, reltype: str, target: str, is_external: bool = ...) -> CT_Relationship: ...
    @classmethod
    def new(cls) -> "CT_Relationships": ...
    @property
    def xml_file_bytes(self) -> bytes: ...

class CT_Types(BaseOxmlElement):
    default_lst: List[CT_Default]
    override_lst: List[CT_Override]
    _add_default: Callable[..., CT_Default]
    _add_override: Callable[..., CT_Override]
    def add_default(self, ext: str, content_type: str) -> CT_Default: ...
    def add_override(self, partname: PackURI, content_type: str) -> CT_Override: ...
    @classmethod
    def new(cls) -> "CT_Types": ...
