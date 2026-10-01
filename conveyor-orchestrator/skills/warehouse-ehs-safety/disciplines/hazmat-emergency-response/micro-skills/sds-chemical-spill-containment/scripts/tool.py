# Hazmat SDS Containment Matcher
def get_spill_containment_action(chemical_class: str, spill_volume_liters: float):
    if "FLAMMABLE" in chemical_class.upper():
        neutralizer = "Activated Charcoal Clay & Non-Sparking Beryllium Shovels"
        ppe = "LEVEL_B_RESPIRATORY"
    elif "CORROSIVE" in chemical_class.upper():
        neutralizer = "Sodium Bicarbonate Neutralizing Sorbent"
        ppe = "LEVEL_C_SPLASH_RESISTANT"
    else:
        neutralizer = "General Universal Polypropylene Absorbent Pads"
        ppe = "LEVEL_D_STANDARD"
    return {"chemical_class": chemical_class, "neutralizer": neutralizer, "ppe_required": ppe, "containment_perimeter_m": 15 if spill_volume_liters > 20 else 5}
