# Quarantined Stock Resolver
def triage_quarantined_item(sku_id: str, reason: str, is_packaging_intact: bool):
    if is_packaging_intact and "barcode" in reason.lower():
        action = "REPRINT_LABEL_AND_RELEASE"
    elif "leak" in reason.lower() or "chemical" in reason.lower():
        action = "HAZMAT_DISPOSAL"
    else:
        action = "RETURN_TO_VENDOR"
    return {"sku_id": sku_id, "resolution": action, "destination_bin": "RELEASE-BAY" if action == "REPRINT_LABEL_AND_RELEASE" else "SCRAP-BAY"}
