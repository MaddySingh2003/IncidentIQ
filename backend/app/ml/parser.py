import re

LOG_PATTERN = re.compile(
    r'^(?P<timestamp>\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+'
    r'(?P<level>INFO|ERROR|WARN|DEBUG|TRACE|FATAL)\s+'
    r'(?P<service>\S+)\s+'
    r'(?P<message>.+)$'
)

def parse_log(line: str):
    line =line.strip()
    match = LOG_PATTERN.match(line)
    if not match:
        return None
    
    return match.groupdict()