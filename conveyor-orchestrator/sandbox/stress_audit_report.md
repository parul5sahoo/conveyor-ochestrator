# Fleet Diagnostic Stress-Profiling Audit

**Cymbal Warehouse Automation — Sandbox Diagnostic Report**

- Total telemetry records analyzed: **500**
- Mean TSI: **378.43**
- Median TSI: **165.27**
- Max TSI: **4145.92**
- Critical readings (TSI ≥ 300): **85**
- High readings (150 ≤ TSI < 300): **194**

## Stress Classification Distribution

```
stress_class
ELEVATED    213
HIGH        194
CRITICAL     85
NOMINAL       8
```

## Aisle-Level Hotspots

```
         records  mean_TSI  max_TSI  mean_temp  mean_current  mean_speed  mean_batt
aisle                                                                              
Aisle 4      114   1081.35  4145.92      66.26          8.24        1.12      48.56
Aisle 2       65    188.13   455.70      50.69          5.31        1.49      67.60
Aisle 5       77    185.86   422.45      49.86          5.29        1.47      68.48
Aisle 1       82    168.82   393.27      49.73          4.85        1.46      64.71
Aisle 6       82    158.50   423.07      49.76          4.83        1.55      67.41
Aisle 3       80    157.02   426.60      48.08          4.69        1.51      65.53
```

## Top 10 Highest-Stress Readings

```
      device_id   aisle  temperature  current_draw  speed  battery     TSI stress_class
 PickerBot-Beta Aisle 4        104.3          15.9    0.4       25 4145.92     CRITICAL
 PickerBot-Beta Aisle 4        103.7          15.8    0.4       25 4096.15     CRITICAL
  Conveyor-CV11 Aisle 4        100.0          15.6    0.4       15 3900.00     CRITICAL
 PickerBot-Beta Aisle 4         99.2          11.6    0.3       11 3835.73     CRITICAL
  Conveyor-CV11 Aisle 4         90.9          12.2    0.3       18 3696.60     CRITICAL
  Conveyor-CV11 Aisle 4         94.9          11.4    0.3       23 3606.20     CRITICAL
PickerBot-Delta Aisle 4        103.2          13.9    0.4       25 3586.20     CRITICAL
 PickerBot-Beta Aisle 4         97.9          14.4    0.4       23 3524.40     CRITICAL
 PickerBot-Beta Aisle 4         87.0          14.3    0.4       11 3110.25     CRITICAL
PickerBot-Delta Aisle 4         92.2          13.2    0.4       23 3042.60     CRITICAL
```

## Top 10 Devices by Mean TSI

```
                 mean_TSI  max_TSI  readings
device_id                                   
Conveyor-CV11      801.85  3900.00        66
PickerBot-Beta     773.79  4145.92        70
PickerBot-Delta    529.49  3586.20        58
PickerBot-Gamma    180.65   450.12        61
PickerBot-Alpha    171.25   455.70        46
SorterBot-02       166.40   423.07        50
SorterBot-01       164.77   426.60        44
Conveyor-CV15      163.62   397.27        57
Conveyor-CV12      158.84   388.60        48
```

## Battery Risk (SOC < 20%): 22 readings

```
      device_id   aisle  temperature  current_draw  speed  battery     TSI stress_class
 PickerBot-Beta Aisle 4         87.0          14.3    0.4       11 3110.25     CRITICAL
  Conveyor-CV11 Aisle 4         87.9          13.1    0.6       17 1919.15     CRITICAL
 PickerBot-Beta Aisle 4        102.0          14.2    0.6       15 2414.00     CRITICAL
PickerBot-Delta Aisle 4        102.2          11.7    0.4       18 2989.35     CRITICAL
  Conveyor-CV11 Aisle 4         93.6          11.6    0.6       17 1809.60     CRITICAL
PickerBot-Delta Aisle 4         92.5          15.1    0.5       13 2793.50     CRITICAL
  Conveyor-CV11 Aisle 4         90.9          12.2    0.3       18 3696.60     CRITICAL
  Conveyor-CV11 Aisle 4        100.0          15.6    0.4       15 3900.00     CRITICAL
  Conveyor-CV11 Aisle 4        102.4          14.1    0.6       18 2406.40     CRITICAL
 PickerBot-Beta Aisle 4         96.8          11.0    0.7       11 1521.14     CRITICAL
```

## Recommended Actions

- Immediate inspection of devices flagged CRITICAL.
- Thermal cooldown cycles for aisles with mean TSI > 150.
- Recharge queue for units with battery SOC < 20%.
- Review current-draw calibration for stalled (speed=0) units.
