# Research Sources

Sources for our disease simulation project, organized by disease.

## Mathematical Foundation: SIR and SEIR Models

**Kermack, W. O., & McKendrick, A. G. (1927).** *A Contribution to the Mathematical Theory of Epidemics.* *Proceedings of the Royal Society A*, **115**, 700–721. [Original paper](https://doi.org/10.1098/rspa.1927.0118) | [PDF](https://pdodds.w3.uvm.edu/files/papers/others/1927/kermack1927a.pdf)

The researchers developed mathematical equations to understand how epidemics spread and decline. On **page 714**, they compared their model with **weekly plague deaths in Bombay, India, during 1905–1906**. Their work helped establish the SIR model. SEIR was developed later.

**SEIR historical source:** Burke, D. S. (2024). *Origins of the problematic E in SEIR epidemic models.* [Read the paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC11024649/). This discusses why an exposed stage was introduced to represent the delay between infection and becoming infectious.

**Note:** The paper does not provide default beta, gamma, or sigma values for our simulation. Record where any values you use come from.

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
