from typing import Optional
from pptx.enum.chart import XL_LEGEND_POSITION
from pptx.oxml.xmlchemy import BaseOxmlElement, ZeroOrOne

class CT_Legend(BaseOxmlElement):
    legendPos: Optional["CT_LegendPos"]
    layout: Optional[BaseOxmlElement]
    overlay: Optional[BaseOxmlElement]
    txPr: Optional[BaseOxmlElement]
    @property
    def defRPr(self) -> BaseOxmlElement: ...
    @property
    def horz_offset(self) -> float: ...
    @horz_offset.setter
    def horz_offset(self, offset: float) -> None: ...
    def _new_txPr(self) -> BaseOxmlElement: ...

class CT_LegendPos(BaseOxmlElement):
    val: XL_LEGEND_POSITION
