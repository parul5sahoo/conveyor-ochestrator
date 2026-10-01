# Barcode Recoder Utility
def recode_barcode_symbology(sku_id: str, batch_number: str):
    return {
        "sku": sku_id,
        "symbology": "GS1-128",
        "barcode_payload": f"(01)00850029{sku_id}(10){batch_number}",
        "print_station": "LABEL-APPLY-03",
        "status": "SENT_TO_PRINTER"
    }
