from typing import Optional
from pptx.oxml.xmlchemy import BaseOxmlElement
from pptx.oxml.simpletypes import ST_LayoutMode

class CT_Boolean(BaseOxmlElement):
    val: bool

class CT_Boolean_Explicit(BaseOxmlElement):
    _val: bool
    @property
    def val(self) -> bool: ...
    @val.setter
    def val(self, value: bool) -> None: ...

class CT_Double(BaseOxmlElement):
    val: float

class CT_Layout(BaseOxmlElement):
    manualLayout: Optional["CT_ManualLayout"]
    @property
    def horz_offset(self) -> float: ...
    @horz_offset.setter
    def horz_offset(self, offset: float) -> None: ...

class CT_LayoutMode(BaseOxmlElement):
    val: ST_LayoutMode

class CT_ManualLayout(BaseOxmlElement):
    xMode: Optional[CT_LayoutMode]
    x: Optional[CT_Double]
    @property
    def horz_offset(self) -> float: ...
    @horz_offset.setter
    def horz_offset(self, offset: float) -> None: ...

class CT_NumFmt(BaseOxmlElement):
    formatCode: str
    sourceLinked: Optional[bool]

class CT_Title(BaseOxmlElement):
    tx: Optional["CT_Tx"]
    spPr: Optional[BaseOxmlElement]
    def get_or_add_tx_rich(self) -> BaseOxmlElement: ...
    @property
    def tx_rich(self) -> Optional[BaseOxmlElement]: ...
    @staticmethod
    def new_title() -> "CT_Title": ...

class CT_Tx(BaseOxmlElement):
    strRef: Optional[BaseOxmlElement]
    rich: Optional[BaseOxmlElement]
    def _new_rich(self) -> BaseOxmlElement: ...

class CT_UnsignedInt(BaseOxmlElement):
    val: int
