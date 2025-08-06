---
layout: research_note
title: "Waveguide Mode Analysis Results"
date: 2025-08-04
description: "Comparison of TE and TM modes in silicon nitride waveguides for quantum applications"
tags: [photonics, waveguide, mode-analysis]
categories: [optics]
related_project: "Designing a Silicon Nitride Waveguide"
featured: true
---

## Mode Profile Calculations

Using COMSOL Multiphysics, I calculated the fundamental TE and TM modes for our silicon nitride waveguide design.

### Waveguide Parameters
- **Core**: Si₃N₄ (n = 2.0)
- **Cladding**: SiO₂ (n = 1.46)
- **Dimensions**: 500 nm × 250 nm

## Results Summary

| Mode | Effective Index | Mode Area (μm²) | Confinement Factor |
|------|----------------|-----------------|-------------------|
| TE₀₀ | 1.8234 | 0.156 | 0.94 |
| TM₀₀ | 1.7891 | 0.189 | 0.91 |

## Key Observations

1. **TE Mode Preference**: Higher confinement factor makes TE₀₀ more suitable for quantum applications
2. **Single Mode Operation**: At 1550 nm, the waveguide supports only fundamental modes
3. **Low Loss**: Theoretical propagation loss < 0.1 dB/cm

## Fabrication Considerations

- **Sidewall Roughness**: Must be < 2 nm RMS to maintain low scattering loss
- **Thickness Variation**: ±5 nm tolerance acceptable for single-mode operation
- **Etch Profile**: Near-vertical sidewalls (>85°) required

## Next Experiments

- [ ] Fabricate test structures using e-beam lithography
- [ ] Measure insertion loss and propagation loss
- [ ] Test coupling efficiency with fiber arrays
- [ ] Characterize temperature dependence

## Simulation Files

All COMSOL simulation files are stored in `/simulations/waveguide_modes/v2.1/`
