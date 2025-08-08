from typing import Optional
from pptx.enum.chart import XL_AXIS_CROSSES, XL_TICK_LABEL_POSITION, XL_TICK_MARK
from pptx.oxml.chart.shared import CT_Title
from pptx.oxml.simpletypes import ST_AxisUnit, ST_LblOffset, ST_Orientation
from pptx.oxml.xmlchemy import BaseOxmlElement, OneAndOnlyOne, ZeroOrOne

class BaseAxisElement(BaseOxmlElement):
    @property
    def defRPr(self) -> BaseOxmlElement: ...
    @property
    def orientation(self) -> ST_Orientation: ...
    @orientation.setter
    def orientation(self, value: ST_Orientation) -> None: ...
    def _new_title(self) -> CT_Title: ...
    def _new_txPr(self) -> BaseOxmlElement: ...

class CT_AxisUnit(BaseOxmlElement):
    val: float

class CT_CatAx(BaseAxisElement):
    scaling: "CT_Scaling"
    delete_: Optional[BaseOxmlElement]
    majorGridlines: Optional["CT_ChartLines"]
    minorGridlines: Optional["CT_ChartLines"]
    title: Optional[CT_Title]
    numFmt: Optional[BaseOxmlElement]
    majorTickMark: Optional["CT_TickMark"]
    minorTickMark: Optional["CT_TickMark"]
    tickLblPos: Optional["CT_TickLblPos"]
    spPr: Optional[BaseOxmlElement]
    txPr: Optional[BaseOxmlElement]
    crosses: Optional["CT_Crosses"]
    crossesAt: Optional[BaseOxmlElement]
    lblOffset: Optional["CT_LblOffset"]

class CT_ChartLines(BaseOxmlElement):
    spPr: Optional[BaseOxmlElement]

class CT_Crosses(BaseOxmlElement):
    val: XL_AXIS_CROSSES

class CT_DateAx(BaseAxisElement):
    scaling: "CT_Scaling"
    delete_: Optional[BaseOxmlElement]
    majorGridlines: Optional["CT_ChartLines"]
    minorGridlines: Optional["CT_ChartLines"]
    title: Optional[CT_Title]
    numFmt: Optional[BaseOxmlElement]
    majorTickMark: Optional["CT_TickMark"]
    minorTickMark: Optional["CT_TickMark"]
    tickLblPos: Optional["CT_TickLblPos"]
    spPr: Optional[BaseOxmlElement]
    txPr: Optional[BaseOxmlElement]
    crosses: Optional[CT_Crosses]
    crossesAt: Optional[BaseOxmlElement]
    lblOffset: Optional["CT_LblOffset"]

class CT_LblOffset(BaseOxmlElement):
    val: ST_LblOffset

class CT_Orientation(BaseOxmlElement):
    val: ST_Orientation

class CT_Scaling(BaseOxmlElement):
    orientation: Optional[CT_Orientation]
    max: Optional[BaseOxmlElement]
    min: Optional[BaseOxmlElement]
    @property
    def maximum(self) -> Optional[float]: ...
    @maximum.setter
    def maximum(self, value: Optional[float]) -> None: ...
    @property
    def minimum(self) -> Optional[float]: ...
    @minimum.setter
    def minimum(self, value: Optional[float]) -> None: ...

class CT_TickLblPos(BaseOxmlElement):
    val: Optional[XL_TICK_LABEL_POSITION]

class CT_TickMark(BaseOxmlElement):
    val: XL_TICK_MARK

class CT_ValAx(BaseAxisElement):
    scaling: CT_Scaling
    delete_: Optional[BaseOxmlElement]
    majorGridlines: Optional[CT_ChartLines]
    minorGridlines: Optional[CT_ChartLines]
    title: Optional[CT_Title]
    numFmt: Optional[BaseOxmlElement]
    majorTickMark: Optional[CT_TickMark]
    minorTickMark: Optional[CT_TickMark]
    tickLblPos: Optional[CT_TickLblPos]
    spPr: Optional[BaseOxmlElement]
    txPr: Optional[BaseOxmlElement]
    crossAx: Optional[BaseOxmlElement]
    crosses: Optional[CT_Crosses]
    crossesAt: Optional[BaseOxmlElement]
    majorUnit: Optional[CT_AxisUnit]
    minorUnit: Optional[CT_AxisUnit]
