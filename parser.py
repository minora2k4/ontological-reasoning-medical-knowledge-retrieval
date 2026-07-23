import re

def parser(text: str) -> str:
    result = []
    section_letter = 0
    bullet_count = 0
    for line in text.splitlines():
        line = line.rstrip()
        if not line.strip():
            continue
        # Heading cấp 1: 1. 2. 3. ...
        if re.match(r"^\d+\.", line):
            result.append(line)
            section_letter = 0
            bullet_count = 0
        # Bullet: -
        elif re.match(r"^\s*-\s+", line):
            bullet_count += 1
            content = re.sub(r"^\s*-\s+", "", line)
            letter = chr(ord("a") + section_letter - 1)
            result.append(f"{letter}{bullet_count}. {content}")
        # Dòng thường
        else:
            section_letter += 1
            bullet_count = 0
            letter = chr(ord("a") + section_letter - 1)
            result.append(f"{letter}. {line.strip()}")
    return "\n".join(result)