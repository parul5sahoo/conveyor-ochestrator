# SoC Opportunity Charging Scheduler
def evaluate_charging_need(agv_id: str, battery_soc_pct: float, current_task_priority: str = "NORMAL"):
    if battery_soc_pct < 20.0:
        action = "IMMEDIATE_CHARGING_REROUTE"
        target_pad = "FAST-CHARGE-PAD-01"
    elif battery_soc_pct <= 35.0:
        action = "OPPORTUNITY_CHARGE_POST_TASK"
        target_pad = "INDUCTIVE-STATION-03"
    else:
        action = "CONTINUE_ACTIVE_DISPATCH"
        target_pad = None
    return {"agv_id": agv_id, "battery_soc": battery_soc_pct, "recommended_action": action, "assigned_pad": target_pad}
