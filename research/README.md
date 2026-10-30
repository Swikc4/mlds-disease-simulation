# Research Sources

This folder contains the scientific sources we use to study measles, influenza, and COVID-19. We use these references to understand disease transmission and select parameters for our simulation.

## Mathematical Models

**SIR Model**

Kermack, W. O., & McKendrick, A. G. (1927). *A Contribution to the Mathematical Theory of Epidemics.* Proceedings of the Royal Society A, 115, pp. 700–721.

Relevant page: **714** (historical epidemic comparison).

[Original Paper](https://doi.org/10.1098/rspa.1927.0118) | [PDF](https://pdodds.w3.uvm.edu/files/papers/others/1927/kermack1927a.pdf)

**SEIR Model**

Burke, D. S. (2024). *Origins of the problematic E in SEIR epidemic models.* Infectious Disease Modelling, 9(3), pp. 673–679.

Relevant sections: **Abstract, Introduction, and Section 4** (exposed and latent states).

[Read Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC11024649/)

## Disease Research

### Measles

[CDC: Clinical Overview of Measles](https://www.cdc.gov/measles/hcp/clinical-overview/index.html)

Relevant sections: Clinical features, How it spreads, Prevention.

Delamater et al. (2019). *Complexity of the Basic Reproduction Number (R₀).* Emerging Infectious Diseases, 25(1), **pp. 1–4**.

[Read Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC6302597/)

This paper explains R₀ generally, rather than providing measles-specific parameters.

### Influenza

[CDC: Influenza](https://www.cdc.gov/yellow-book/hcp/travel-associated-infections-diseases/influenza.html)

Relevant section: **Transmission** (incubation and infectious periods).

Biggerstaff et al. (2014). *Estimates of the reproduction number for seasonal, pandemic, and zoonotic influenza: a systematic review of the literature.* BMC Infectious Diseases, 14, Article 480.

Relevant sections: **Methods, Results, and Conclusions**.

[Read Paper](https://stacks.cdc.gov/view/cdc/25291)

### COVID-19

[CDC: Clinical Presentation](https://www.cdc.gov/covid/hcp/clinical-care/covid19-presentation.html)

Relevant sections: **Incubation period, Presentation, and Transmission**.

[COVID-19 Reproduction Number Research](https://pmc.ncbi.nlm.nih.gov/articles/PMC8827628/)

Relevant sections: Abstract, Methods, and Results. Check the article for exact page references.

[SARS-CoV-2 Transmission Timing Research](https://pmc.ncbi.nlm.nih.gov/articles/PMC10541713/)

Relevant sections: Abstract, Results, and Discussion. Check the article for exact page references.

## Historical Data

[Johns Hopkins COVID-19 Data Repository](https://github.com/CSSEGISandData/COVID-19)

We may use historical data for additional comparisons after completing our core simulation.

## Using Research in Our Simulation

We classify every numerical parameter as:

| Type | Meaning |
|---|---|
| **Sourced** | Reported directly in a scientific source |
| **Derived** | Calculated from sourced information |
| **Assumed** | Selected for our educational simulation |

We record the source, value, units, and assumptions for each parameter. We do not treat published reproduction numbers or incubation periods as direct infection probabilities.

Our simulation is for educational purposes and does not predict real-world outbreaks.