from typing import IO, Type
from lxml import etree
from pptx.oxml.xmlchemy import BaseOxmlElement

element_class_lookup: etree.ElementNamespaceClassLookup
oxml_parser: etree.XMLParser

def parse_from_template(template_file_name: str) -> BaseOxmlElement: ...
def parse_xml(xml: str | bytes) -> BaseOxmlElement: ...
def register_element_cls(nsptagname: str, cls: Type[BaseOxmlElement]) -> None: ...
