---
name: fft-vibration-harmonic-analysis
parent_domain: conveyor-diagnostics
parent_discipline: motor-drive-diagnostics
display_name: "FFT Harmonic Peak & Bearing Degradation Analysis"
hierarchy_level: 3
level_name: "OPERATIONAL_MICRO_SKILL"
description: "Calculates Fast Fourier Transform frequency spectra to detect Ball Pass Frequency Outer (BPFO) and Inner (BPFI) raceway faults."
tags: ["fft", "vibration", "bearing", "harmonic", "bpfo", "iso 10816"]
---

# FFT Harmonic Peak & Bearing Degradation Analysis (Level 3 Operational Micro-Skill)

**Hierarchy Path**: `conveyor-diagnostics` ➔ `motor-drive-diagnostics` ➔ `fft-vibration-harmonic-analysis`

## Description
Calculates Fast Fourier Transform frequency spectra to detect Ball Pass Frequency Outer (BPFO) and Inner (BPFI) raceway faults.

### Standard Operating Procedure: FFT Vibration Analysis
1. **Sampling Protocol**: Collect 4096-point accelerometer sample at 10 kHz from drive-end bearing housing.
2. **Frequency Peak Matching**:
   - 1X RPM: Shaft unbalance
   - 2X RPM: Mechanical misalignment
   - High Frequency (3.2x - 5.8x RPM): Bearing raceway pitting (BPFO / BPFI).
3. **ISO 10816-3 Thresholds**:
   - < 2.8 mm/s RMS: Class A (Good)
   - 2.8 - 4.5 mm/s RMS: Class B (Acceptable)
   - 4.5 - 7.1 mm/s RMS: Class C (Warning - schedule greasing/bearing swap within 48h)
   - > 7.1 mm/s RMS: Class D (Danger - trip safety interlock immediately).

## Executable Helper Script
Executable implementation available at `scripts/tool.py`.
