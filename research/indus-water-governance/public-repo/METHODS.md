# Methods (planned)

## Design

- **Unit:** main canal command (n ≈ 45).
- **Outcomes:** (1) mean groundwater storage trend within each command, from the downscaled
  surface; (2) the spread of that trend within each command.
- **Institutional variables:** canal position (head / middle / tail), electricity tariff regime,
  tubewell density, historical tenure class where it can be coded.
- **Controls:** rainfall, evapotranspiration, cropping intensity, canal deliveries where
  available.
- **Model:** spatial regression (spatial error or spatial lag) with a small covariate set,
  six to seven at most, because of the sample size.

## Known risks, stated in advance

- **Small n.** About 45 units supports a descriptive spatial join and a parsimonious model, not
  a rich one. The sample size will be stated everywhere.
- **Spatial autocorrelation** inflates significance if ignored. It is modelled explicitly.
- **Ecological inference.** A command-level association between tariffs and depletion does not
  show that individual farmers responded to tariffs. This limit will be stated.
- **The measure itself.** Downscaled satellite estimates carry model uncertainty. The analysis
  carries that uncertainty through rather than treating the surface as observed.
- **Uncodeable institutions.** Historical tenure may not exist in usable form. The headline
  claim will not rest on it.
- **Null results** will be reported.

## Pre-registration

The model specification will be written down and time-stamped (Zenodo or OSF) before the
institutional variables are joined to the outcome.
