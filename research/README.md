# Research Sources

Sources for our disease simulation project, organized by disease.

## Mathematical Foundation: SIR and SEIR Models

- **Kermack, W. O., & McKendrick, A. G. (1927).** *A Contribution to the Mathematical Theory of Epidemics.* *Proceedings of the Royal Society of London. Series A*, **115**(772), 700–721. [Original paper DOI](https://doi.org/10.1098/rspa.1927.0118) | [Read the original paper (PDF)](https://pdodds.w3.uvm.edu/files/papers/others/1927/kermack1927a.pdf)

  **What the authors investigated:** They developed a mathematical explanation for how epidemics spread and eventually decline. Their work became a foundation for SIR-style models. SEIR is a later extension, not a model introduced in this paper.

  **Historical example in the paper (page 714):** The authors compared their mathematical epidemic curve with **weekly deaths from plague on the island of Bombay (now Mumbai), India, from December 17, 1905, to July 21, 1906**. Their figure shows the observed death counts and a calculated curve. This is the source for the Bombay plague facts in the Week 1 assignment.

  **Important distinction:** These figures are *plague deaths*, not daily counts of susceptible, exposed, or infectious individuals. Their general mathematical theory was not specific to plague. The simple SIR model also does not reproduce every detail of plague transmission involving rats and fleas.

  **Parameters:** The paper supports the modeling framework, but it does not supply default beta, gamma, or sigma values for our classroom simulation. Any numerical values used in our work must be identified as sourced, derived, or assumed.

## Measles

- [Review of measles reproduction numbers](https://pmc.ncbi.nlm.nih.gov/articles/PMC6302597/)
- [CDC measles clinical overview](https://www.cdc.gov/measles/hcp/clinical-overview/index.html)

## Influenza

- [Influenza reproduction number review](https://stacks.cdc.gov/view/cdc/25291)
- [CDC Yellow Book: Influenza](https://www.cdc.gov/yellow-book/hcp/travel-associated-infections-diseases/influenza.html)

## COVID-19

- [Review of COVID-19 R0 estimates](https://pmc.ncbi.nlm.nih.gov/articles/PMC8827628/)
- [CDC clinical presentation](https://www.cdc.gov/covid/hcp/clinical-care/covid19-presentation.html)
- [COVID-19 transmission timing research](https://pmc.ncbi.nlm.nih.gov/articles/PMC10541713/)

## Optional Historical Data

- [Johns Hopkins CSSE COVID-19 repository](https://github.com/CSSEGISandData/COVID-19)

## Using Research Data

When we use disease parameters, we should record the parameter, value, units, source, and whether it is:

- **Sourced:** Reported directly in a source.
- **Derived:** Calculated from sourced data, with the calculation explained.
- **Assumed:** Chosen for our educational model, not measured disease data.

Check each source and its relevance before using values in the simulation.
