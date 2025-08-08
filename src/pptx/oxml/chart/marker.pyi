from typing import Optional
from pptx.enum.chart import XL_MARKER_STYLE
from pptx.oxml.simpletypes import ST_MarkerSize
from pptx.oxml.xmlchemy import BaseOxmlElement, ZeroOrOne

class CT_Marker(BaseOxmlElement):
    symbol: Optional["CT_MarkerStyle"]
    size: Optional["CT_MarkerSize"]
    spPr: Optional[BaseOxmlElement]

    @property
    def size_val(self) -> Optional[int]: ...
    @property
    def symbol_val(self) -> Optional[XL_MARKER_STYLE]: ...

class CT_MarkerSize(BaseOxmlElement):
    val: ST_MarkerSize

class CT_MarkerStyle(BaseOxmlElement):
    val: XL_MARKER_STYLE
