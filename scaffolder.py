import re
from part import Part


def build_tree(parts: str) -> list[Part]:
    roots: list[Part] = []
    current_root: Part | None = None
    current_section: Part | None = None

    for raw in parts.splitlines():
        line = raw.strip()
        if not line:
            continue
        # 1.
        m = re.match(r"^(\d+)\.\s*(.*)$", line)
        if m:
            number, text = m.groups()
            current_root = Part(
                partID=number,
                text=text
            )
            roots.append(current_root)
            current_section = None
            continue

        # a.
        m = re.match(r"^([a-z])\.\s*(.*)$", line)
        if m:
            letter, text = m.groups()
            if current_root is None:
                # bỏ qua nếu parser lỗi
                continue
            current_section = Part(
                partID=f"{current_root.partID}_{letter}",
                text=text
            )
            current_root.child.append(current_section)
            continue

        # a1.
        m = re.match(r"^([a-z])(\d+)\.\s*(.*)$", line)
        if m:
            letter, number, text = m.groups()
            if current_root is None:
                # bỏ qua nếu file lỗi
                continue
            current_section.child.append(
                Part(
                    partID=f"{current_section.partID}_{letter}{number}",
                    text=text
                )
            )
            continue
    return roots