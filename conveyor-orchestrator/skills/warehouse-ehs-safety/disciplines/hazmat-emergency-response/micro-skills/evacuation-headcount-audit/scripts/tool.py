# Muster Point Headcount Reconciler
def audit_muster_headcount(total_on_site: int, mustered_count: int):
    missing = total_on_site - mustered_count
    return {
        "total_on_site": total_on_site,
        "accounted_for": mustered_count,
        "missing_count": missing,
        "status": "ALL_CLEAR" if missing == 0 else "URGENT_SEARCH_ACTIVE"
    }
