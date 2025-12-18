from datetime import datetime


def now_iso() -> str:
    return datetime.now().isoformat()


def now_str() -> str:
    return now_iso()


def parse_iso(value: str) -> datetime:
    return datetime.fromisoformat(value)


def format_br(value: str) -> str:
    dt = parse_iso(value)
    return dt.strftime("%d/%m/%Y %H:%M")


def diff_hours(start: str, end: str) -> float:
    delta = parse_iso(end) - parse_iso(start)
    return round(delta.total_seconds() / 3600, 2)
