from typing import List, Optional
from pptx.oxml.xmlchemy import BaseOxmlElement, OneAndOnlyOne, ZeroOrMore, ZeroOrOne

class CT_AxDataSource(BaseOxmlElement):
    multiLvlStrRef: Optional[BaseOxmlElement]
    @property
    def lvls(self) -> List["CT_Lvl"]: ...

class CT_DPt(BaseOxmlElement):
    idx: BaseOxmlElement
    marker: Optional[BaseOxmlElement]
    spPr: Optional[BaseOxmlElement]
    @classmethod
    def new_dPt(cls) -> "CT_DPt": ...

class CT_Lvl(BaseOxmlElement):
    pt: List[BaseOxmlElement]

class CT_NumDataSource(BaseOxmlElement):
    numRef: BaseOxmlElement
    @property
    def ptCount_val(self) -> int: ...
    def pt_v(self, idx: int) -> Optional[float]: ...

class CT_SeriesComposite(BaseOxmlElement):
    idx: BaseOxmlElement
    order: BaseOxmlElement
    tx: Optional[BaseOxmlElement]
    spPr: Optional[BaseOxmlElement]
    invertIfNegative: Optional[BaseOxmlElement]
    marker: Optional[BaseOxmlElement]
    dPt: List[CT_DPt]
    dLbls: Optional[BaseOxmlElement]
    cat: Optional[CT_AxDataSource]
    val: Optional[CT_NumDataSource]
    xVal: Optional[CT_NumDataSource]
    yVal: Optional[CT_NumDataSource]
    smooth: Optional[BaseOxmlElement]
    bubbleSize: Optional[CT_NumDataSource]
    @property
    def bubbleSize_ptCount_val(self) -> int: ...
    @property
    def cat_ptCount_val(self) -> int: ...
    def get_dLbl(self, idx: int) -> Optional[BaseOxmlElement]: ...
    def get_or_add_dLbl(self, idx: int) -> BaseOxmlElement: ...
    def get_or_add_dPt_for_point(self, idx: int) -> CT_DPt: ...
    @property
    def xVal_ptCount_val(self) -> int: ...
    @property
    def yVal_ptCount_val(self) -> int: ...
    def _new_dLbls(self) -> BaseOxmlElement: ...
    def _new_dPt(self) -> CT_DPt: ...

class CT_StrVal_NumVal_Composite(BaseOxmlElement):
    v: BaseOxmlElement
    idx: int
    @property
    def value(self) -> float: ...
