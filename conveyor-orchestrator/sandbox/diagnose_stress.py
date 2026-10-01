
import os
import pandas as pd
import numpy as np
import json

def diagnose_stress():
    file_candidates = [
        'fleet_telemetry_dump.json',
        os.path.join(os.path.dirname(__file__), 'fleet_telemetry_dump.json'),
        os.path.join(os.path.dirname(__file__), '..', 'sandbox', 'fleet_telemetry_dump.json'),
        os.path.join(os.path.dirname(__file__), '..', 'mock_data', 'fleet_telemetry_dump.json'),
    ]
    telemetry_path = None
    for cand in file_candidates:
        if os.path.exists(cand) and os.path.getsize(cand) > 0:
            telemetry_path = cand
            break

    if not telemetry_path:
        print("Error: 'fleet_telemetry_dump.json' not found in the sandbox.")
        return

    try:
        with open(telemetry_path, 'r', encoding='utf-8') as f:
            telemetry_data = json.load(f)
    except json.JSONDecodeError:
        print("Error: Could not decode 'fleet_telemetry_dump.json'. Invalid JSON format.")
        return

    df = pd.DataFrame(telemetry_data)

    required_columns = ['aisle', 'temperature_c', 'current_draw_a', 'speed_mps']
    for col in required_columns:
        if col not in df.columns:
            print(f"Error: Missing required column '{col}' in telemetry data. Available columns: {df.columns.tolist()}")
            return

    # Filter for Aisle 4 using flexible case-insensitive matching
    aisle_4_df = df[df['aisle'].astype(str).str.contains(r'aisle\s*4', case=False, na=False)].copy()
    if aisle_4_df.empty:
        aisle_4_df = df[df['aisle'] == 'Aisle 4'].copy()

    if aisle_4_df.empty:
        print("No telemetry data found for Aisle 4.")
        with open('aisle_4_stress_report.md', 'w') as f:
            f.write("# Aisle 4 Stress Profile Report\n\n")
            f.write("No telemetry data available for Aisle 4 to generate a stress profile.\n")
        return

    # Calculate Thermal Heat Stress Index (TSI) using correct column names
    speed_safe = aisle_4_df['speed_mps'].replace(0, np.nan).fillna(0.01).clip(lower=0.01)
    aisle_4_df['tsi'] = (aisle_4_df['temperature_c'] * aisle_4_df['current_draw_a']) / speed_safe

    # Identify hot-spots (e.g., top 10% highest TSI values)
    hot_spot_threshold = aisle_4_df['tsi'].quantile(0.90)
    hot_spots = aisle_4_df[aisle_4_df['tsi'] >= hot_spot_threshold].sort_values(by='tsi', ascending=False)

    # Generate summary statistics
    summary_stats = aisle_4_df['tsi'].describe().to_string()

    # Prepare report content
    report_content = f"""# Aisle 4 Stress Profile Report

## Summary Statistics for Thermal Stress Index (TSI) in Aisle 4
```
{summary_stats}
```

## Hot-Spot Analysis (Top 10% TSI Values)

Identified {len(hot_spots)} potential hot-spot entries with TSI values at or above the 90th percentile ({hot_spot_threshold:.2f}). These indicate areas of elevated thermal stress for devices operating in Aisle 4.

### Detailed Hot-Spot Telemetry

```json
{hot_spots.to_json(orient='records', indent=2)}
```

## Recommendations

Further investigation is recommended for devices and locations identified in the hot-spot analysis. Consider:
*   **Load Balancing**: Redistribute tasks to reduce sustained high current draw in specific devices.
*   **Cooling System Review**: Ensure adequate ventilation and cooling in identified hot-spot areas within Aisle 4.
*   **Device Maintenance**: Inspect devices operating under high stress for potential wear and tear.
*   **Speed Optimization**: Analyze if operational speeds are contributing to excessive thermal loads during high current activities.
"""

    # Save report to a file
    report_filename = 'aisle_4_stress_report.md'
    with open(report_filename, 'w') as f:
        f.write(report_content)

    print(f"Stress profile report for Aisle 4 generated and saved to '{report_filename}'.")
    print("\n--- Summary ---")
    print("Mean TSI:", aisle_4_df['tsi'].mean())
    print("Max TSI:", aisle_4_df['tsi'].max())
    print(f"Number of hot-spot entries (TSI >= {hot_spot_threshold:.2f}): {len(hot_spots)}")

if __name__ == "__main__":
    diagnose_stress()
