from typing import Dict, Optional

from pptx.oxml.xmlchemy import BaseOxmlElement

class CT_Hyperlink(BaseOxmlElement):
    rId: str
    action: Optional[str]

    @property
    def action_fields(self) -> Dict[str, str]: ...
    @property
    def action_verb(self) -> Optional[str]: ...
