---
layout: page
title: Designing a Silicon Nitride Waveguide
description: Designing and simulating a waveguide for quantum optics applications
img: assets/img/project/Waveguide/Components/MMI.png
importance: 1
category: REU
pdf: assets/pdf/CQN_Waveguide.pdf
presentation: assets/pdf/CQN_Waveguide.pdf
related_publications: true
---

# Integrated Photonic Circuits
Project motivation, entanglement swap
## Project Motivation
A qubit is the basic unit of quantum information, analogous to a classical bit, but can exist in a superposition of states:

\begin{equation}
\ket{\psi} =\alpha \ket{0} +\beta \ket{1} \qquad \qquad \left|  \alpha^{2} \right|+\left|  \beta^{2} \right|=1 
\end{equation}

Entanglement is when two qubits are linked such that one’s state can be inferred from the other, for example this Bell state:

\begin{equation}
\ket{\Phi^+} = \frac{1}{\sqrt{ 2 }}(\ket{00} +\ket{11} )
\end{equation}

If we have two pairs of photons entangled A with B, and C with D, we can remotely entangle A&D together by performing a bell state measurement on B&C. This is ‘Entanglement Swapping. To perform this measurement, the photon qubit pairs must be indistinguishable, therefore the information of which path they came from must be erased. This is done through Hong-Ou-Mandel interference – when the pairs are incident on a 50:50 beam splitter, they interfere with one another resulting in both photons exiting the same side of the beam splitter, regardless of their starting path.

## Entanglement Swapping

Through entanglement swapping, two distant qubits can be remotely entangled. This would allow for increased scalability of quantum computers through distributed computing, as well as increased scalability of quantum networks through quantum repeaters. 

Entanglement can be achieved with photons through several degrees of freedom, such as spatially, temporally (or time-bin), or most commonly through polarization. This design focuses on photon pairs encoded through their polarizations, with states:

\begin{equation}
\ket{H} \qquad \ket{V} 
\end{equation}

<div class="row justify-content-center">
    <div class="col-md-8 col-lg-6">
        {% include figure.liquid loading="eager" path="assets/img/project/Waveguide/Motivation/EnSw.png" title="Entanglement Swapping Scheme" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Entanglement swapping protocol showing the measurement setup with 50:50 beamsplitter and polarizing beam splitters.
</div>

The qubit pairs are incident on a 50:50 beamsplitter, which leads them to polarizing beam splitters for measurement. The detectors give ”click patterns” corresponding to the measurements – of 8 possible patterns, 4 of them correspond to a successful entanglement. 

{% cite Dhara2023 %}

# Design Considerations
Because this design is for polarization entangled qubit sources, the design requires polarization insensitivity.

## Material
Silicon Nitride $$Si_3N_4$$ is chosen as the core material with a Silicon Dioxide $$SiO_2$$ cladding.

## Geometry
To minimize polarization sensitivity, we want to avoid confining the wave in the vertical orientation. A pure rectangular or square waveguide is difficult to fabricate at these dimensions, so a double stripe geometry is used.

## Components
Multimode interference couplers are used to build Mach-Zehnder interferometers to replace the beam splitters in the theoretical design. These are chosen over directional couplers to accomodate the dual polarizations.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/project/Waveguide/Components/MMI.png" title="Multimode Interference Coupler Design" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/project/Waveguide/Components/MMI2.png" title="MMI Coupler Configuration" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Multimode interference (MMI) coupler
</div>

# Simulations
## COMSOL
COMSOL was used to simulate the waveguide design.


## Methods
3D simulations of the multimode interference coupler would be ideal but are not feasible with the hardware available.

### Effective Index Method

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/project/Waveguide/cross sections/mode1.png" title="TE" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/project/Waveguide/cross sections/mode2.png" title="TM" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
   TM (left) and TE (right) fundamental modes
</div>

The effective index method was used to approximate the behavior of the multimode interference coupler. 2D simulations are done in COMSOL of the tranverse cross sections of the multimode interference coupler at key locations and an effective index is extracted. These values are linearly interpolated between and this function informs a simulation of the 2D longitudinal cross section of the multimode interference coupler.

## Results

<div class="row justify-content-center">
    <div class="col-md-8 col-lg-6">
        {% include figure.liquid loading="eager" path="assets/img/project/Waveguide/cross sections/freq_domain.png" title="Entanglement Swapping Scheme" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    frequency domain simulation of the multimode interference coupler using the effective index method
</div>

Currently the maximum transmittance found is 46.75%.

## Embedded Document Preview

<div class="alert alert-info">
    <i class="fa-solid fa-info-circle alert-icon"></i>
    <strong>Note:</strong> You can preview the technical report below or <a href="{{ '/assets/pdf/CQN_Waveguide.pdf' | relative_url }}" target="_blank">download it directly</a>.
</div>

<div class="row">
    <div class="col-12">
        <div class="embed-responsive embed-responsive-4by3" style="height: 600px;">
            <iframe class="embed-responsive-item" src="{{ '/assets/pdf/CQN_Waveguide.pdf' | relative_url }}" type="application/pdf" style="width: 100%; height: 100%;">
                <p>Your browser does not support PDFs. <a href="{{ '/assets/pdf/CQN_Waveguide.pdf' | relative_url }}">Download the PDF</a>.</p>
            </iframe>
        </div>
    </div>
</div>

## Project Documentation

<div class="row mt-3">
    <div class="col-md-6">
        <div class="alert alert-info">
            <i class="fa-solid fa-file-pdf alert-icon"></i>
            <strong>Technical Report:</strong><br>
            <a href="{{ '/assets/pdf/CQN_Waveguide.pdf' | relative_url }}" target="_blank" class="btn btn-outline-primary btn-sm mt-2">
                <i class="fa-solid fa-download"></i> Download Report
            </a>
        </div>
    </div>
    <div class="col-md-6">
        <div class="alert alert-warning">
            <i class="fa-solid fa-presentation-screen alert-icon"></i>
            <strong>Presentation:</strong><br>
            <a href="{{ '/assets/pdf/CQN_Waveguide.pdf' | relative_url }}" target="_blank" class="btn btn-outline-warning btn-sm mt-2">
                <i class="fa-solid fa-eye"></i> View Document
            </a>
        </div>
    </div>
</div>

{% include research_notes.liquid %}
