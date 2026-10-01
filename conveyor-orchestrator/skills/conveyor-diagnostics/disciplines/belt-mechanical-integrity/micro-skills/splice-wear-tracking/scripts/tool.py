# Splice Integrity Analyzer
def inspect_splice_gap(gap_width_mm: float):
    return {
        "gap_width_mm": gap_width_mm,
        "max_allowable_mm": 3.0,
        "integrity": "CRITICAL" if gap_width_mm > 3.0 else ("MONITOR" if gap_width_mm > 2.0 else "SECURE")
    }
