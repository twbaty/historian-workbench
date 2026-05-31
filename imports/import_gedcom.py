from pathlib import Path
from gedcom.parser import Parser

base_dir = Path(__file__).resolve().parent.parent
ged_file = base_dir / "docs" / "imports" / "Batie.GED"

print(f"Loading {ged_file}")

gedcom = Parser()
gedcom.parse_file(str(ged_file))

root = gedcom.get_root_child_elements()

people = 0
families = 0

for element in root:
    if element.get_tag() == "INDI":
        people += 1
    elif element.get_tag() == "FAM":
        families += 1

print(f"People: {people}")
print(f"Families: {families}")
