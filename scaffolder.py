import re
from part import Part


def build_tree(parts: str, doc_id: str) -> Part:
    document = Part(
        partID=doc_id,
        text=parts.strip(),
    )

    current_root: Part | None = None
    current_section: Part | None = None

    for line in map(str.strip, parts.splitlines()):
        if not line:
            continue

        # 1.
        if match := re.match(r"^(\d+)\.\s*(.*)$", line):
            number, text = match.groups()
            current_root = Part(
                partID=f"{document.partID}_{number}",
                text=text,
            )
            document.child.append(current_root)
            current_section = None
            continue

        # a.
        if match := re.match(r"^([a-z])\.\s*(.*)$", line):
            if current_root is None:
                continue
            letter, text = match.groups()
            current_section = Part(
                partID=f"{current_root.partID}_{letter}",
                text=text,
            )
            current_root.child.append(current_section)
            continue

        # a1.
        if match := re.match(r"^([a-z])(\d+)\.\s*(.*)$", line):
            if current_section is None:
                continue
            bullet, number, text = match.groups()
            current_section.child.append(
                Part(
                    partID=f"{current_section.partID}_{bullet}{number}",
                    text=text,
                )
            )
    return document