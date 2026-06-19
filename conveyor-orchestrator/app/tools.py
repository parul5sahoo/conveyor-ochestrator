# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.tools import FunctionTool


def check_wms_stock(sku: str) -> dict:
    """Verify stock status and block condition for a specific SKU in the Warehouse Management System (WMS).

    Args:
        sku: The unique Stock Keeping Unit identifier to check in the WMS.

    Returns:
        A dictionary containing the SKU, its current blocking status, quantity, and physical warehouse location.
    """
    sku_cleaned = sku.strip().upper()
    if sku_cleaned == "SKU-991":
        return {
            "sku": sku_cleaned,
            "status": "BLOCKED",
            "quantity": 15,
            "location": "Aisle 4",
        }
    elif sku_cleaned == "SKU-502":
        return {
            "sku": sku_cleaned,
            "status": "AVAILABLE",
            "quantity": 42,
            "location": "Aisle 2",
        }
    return {
        "sku": sku_cleaned,
        "status": "UNKNOWN",
        "quantity": 0,
        "location": "Unknown",
    }


def query_runbooks(error_code: str) -> dict:
    """Query the maintenance Vector Search database for repair instructions matching the error code.

    Args:
        error_code: The machine error or warning code reported by the conveyor telemetry.

    Returns:
        A dictionary containing matched repair instructions, error code, and urgency level.
    """
    err_cleaned = error_code.strip()
    if err_cleaned == "Error 4042":
        return {
            "error_code": err_cleaned,
            "instructions": "Calibrate the main belt speed sensor and reset controller C-3.",
            "urgency": "HIGH",
        }
    elif err_cleaned == "Error 5011":
        return {
            "error_code": err_cleaned,
            "instructions": "Clear debris from diverter flap and manual cycle standard restart.",
            "urgency": "MEDIUM",
        }
    return {
        "error_code": err_cleaned,
        "instructions": "Perform standard conveyor belt safety inspection and reboot system.",
        "urgency": "LOW",
    }


def dispatch_agv(aisle: str, task: str, bot_id: str = "PickerBot-Alpha") -> dict:
    """Command an Autonomous Guided Vehicle (AGV) or picker bot to perform a bypass task in a specific aisle.

    Args:
        aisle: The warehouse aisle where the AGV must perform the bypass.
        task: The specific bypass instruction or route for the AGV.
        bot_id: The unique identifier of the AGV to dispatch (e.g. 'PickerBot-Beta').

    Returns:
        A dictionary confirming the AGV's dispatched status, assigned bot ID, and routing details.
    """
    return {
        "aisle": aisle,
        "task": task,
        "status": "DISPATCHED",
        "bot_id": bot_id,
    }


check_wms_stock_tool = FunctionTool(func=check_wms_stock)
query_runbooks_tool = FunctionTool(func=query_runbooks)
dispatch_agv_tool = FunctionTool(func=dispatch_agv)
