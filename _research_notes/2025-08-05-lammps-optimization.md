---
layout: research_note
title: "LAMMPS Simulation Parameters Optimization"
date: 2025-08-05
description: "Investigation of timestep and ensemble parameters for accurate gold stress-strain simulations"
tags: [molecular-dynamics, lammps, optimization]
categories: [simulation]
related_project: "Modelling Gold Stress Strain Curves in LAMMPS"
---

## Timestep Analysis

After running multiple simulations with different timestep values, I found that:

- 1 fs timestep: Stable but computationally expensive
- 2 fs timestep: Good balance of stability and performance
- 5 fs timestep: Unstable for high strain rates

## Ensemble Considerations

The NPT ensemble with Nosé-Hoover thermostat provides the most realistic results for our gold nanowire simulations.

### Key Findings

1. **Temperature Control**: 300K maintains room temperature conditions
2. **Pressure Control**: 1 atm pressure coupling essential for realistic deformation
3. **Damping Parameters**: τ_T = 100 fs, τ_P = 1000 fs work well

## Next Steps

- Test with different gold crystal orientations
- Investigate size effects on mechanical properties
- Compare with experimental data from literature

## References

- Thompson et al. (2022) - LAMMPS Documentation
- Plimpton (1995) - Fast Parallel Algorithms for Short-Range Molecular Dynamics
