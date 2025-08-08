from typing import Iterator, List, Optional, Sequence, Tuple
from pptx.oxml.simpletypes import ST_BarDir, ST_BubbleScale, ST_GapAmount, ST_Grouping, ST_Overlap
from pptx.oxml.xmlchemy import BaseOxmlElement, OneAndOnlyOne, ZeroOrMore, ZeroOrOne

class BaseChartElement(BaseOxmlElement):
    @property
    def cat(self) -> Optional[BaseOxmlElement]: ...
    @property
    def cat_pt_count(self) -> int: ...
    @property
    def cat_pts(self) -> List[Optional[BaseOxmlElement]]: ...
    @property
    def grouping_val(self) -> ST_Grouping: ...
    def iter_sers(self) -> Iterator[BaseOxmlElement]: ...
    @property
    def sers(self) -> Tuple[BaseOxmlElement, ...]: ...
    def _new_dLbls(self) -> BaseOxmlElement: ...

class CT_Area3DChart(BaseChartElement):
    grouping: Optional["CT_Grouping"]

class CT_AreaChart(BaseChartElement):
    grouping: Optional["CT_Grouping"]
    varyColors: Optional[BaseOxmlElement]
    ser: List[BaseOxmlElement]
    dLbls: Optional[BaseOxmlElement]

class CT_BarChart(BaseChartElement):
    barDir: "CT_BarDir"
    grouping: Optional["CT_Grouping"]
    varyColors: Optional[BaseOxmlElement]
    ser: List[BaseOxmlElement]
    dLbls: Optional[BaseOxmlElement]
    gapWidth: Optional["CT_GapAmount"]
    overlap: Optional["CT_Overlap"]
    @property
    def grouping_val(self) -> ST_Grouping: ...

class CT_BarDir(BaseOxmlElement):
    val: ST_BarDir

class CT_BubbleChart(BaseChartElement):
    ser: List[BaseOxmlElement]
    dLbls: Optional[BaseOxmlElement]
    bubble3D: Optional[BaseOxmlElement]
    bubbleScale: Optional["CT_BubbleScale"]

class CT_BubbleScale(BaseChartElement):
    val: ST_BubbleScale

class CT_DoughnutChart(BaseChartElement):
    varyColors: Optional[BaseOxmlElement]
    ser: List[BaseOxmlElement]
    dLbls: Optional[BaseOxmlElement]

class CT_GapAmount(BaseOxmlElement):
    val: ST_GapAmount

class CT_Grouping(BaseOxmlElement):
    val: Optional[ST_Grouping]

class CT_LineChart(BaseChartElement):
    grouping: Optional[CT_Grouping]
    varyColors: Optional[BaseOxmlElement]
    ser: List[BaseOxmlElement]
    dLbls: Optional[BaseOxmlElement]

class CT_Overlap(BaseOxmlElement):
    val: ST_Overlap

class CT_PieChart(BaseChartElement):
    varyColors: Optional[BaseOxmlElement]
    ser: List[BaseOxmlElement]
    dLbls: Optional[BaseOxmlElement]

class CT_RadarChart(BaseChartElement):
    varyColors: Optional[BaseOxmlElement]
    ser: List[BaseOxmlElement]
    dLbls: Optional[BaseOxmlElement]

class CT_ScatterChart(BaseChartElement):
    varyColors: Optional[BaseOxmlElement]
    ser: List[BaseOxmlElement]
