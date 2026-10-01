---
name: motor-drive-diagnostics
parent_skill: conveyor-diagnostics
display_name: "Motor Drive & Bearing Diagnostics"
hierarchy_level: 2
level_name: "SPECIALIST_DISCIPLINE"
description: "Analyzes motor vibration spectra, bearing fault harmonics, and variable frequency drive (VFD) thermal loads."
micro_skills: ['fft-vibration-harmonic-analysis', 'thermal-overload-monitoring']
---

# Motor Drive & Bearing Diagnostics (Level 2 Specialist Discipline)

**Parent Domain**: `conveyor-diagnostics`

Analyzes motor vibration spectra, bearing fault harmonics, and variable frequency drive (VFD) thermal loads.

## Operational Micro-Skills (Level 3)
- **[`fft-vibration-harmonic-analysis`](./micro-skills/fft-vibration-harmonic-analysis/SKILL.md)**: Calculates Fast Fourier Transform frequency spectra to detect Ball Pass Frequency Outer (BPFO) and Inner (BPFI) raceway faults.
- **[`thermal-overload-monitoring`](./micro-skills/thermal-overload-monitoring/SKILL.md)**: Monitors IGBT junction temperatures and calculates current derating to prevent motor winding insulation breakdown.
