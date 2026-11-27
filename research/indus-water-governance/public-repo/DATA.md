# Data

## The go/no-go: canal-command boundaries

The unit of analysis is the main canal command. The Indus system has about 45 major commands.
Command-level results appear in published studies (IFPRI 2016; IWMI canal-crops dataset), so
the geography exists somewhere. **An open boundary file has not been found.** Open questions:

- Are the boundary layers behind the IFPRI and IWMI work obtainable, and from whom?
- Do watercourse-outlet locations exist? They would allow a much finer unit and a larger sample.

If boundaries cannot be obtained, the project shifts to quantifying the uncertainty in
published abstraction estimates.

## Sources

| Variable | Source | Access |
|---|---|---|
| Groundwater storage change | Downscaled GRACE/GRACE-FO (Arshad et al., 2024); GRACE-FO mascons, NASA JPL | Published product: to request. Mascons: open |
| Soil moisture, snow, surface water | GLDAS / NOAH, NASA GES DISC | Open |
| Rainfall | CHIRPS | Open |
| Evapotranspiration | MODIS MOD16 | Open |
| Cropping intensity and crop type | Sentinel-2, Landsat | Open |
| Subsidence (secondary check) | Sentinel-1 InSAR | Open |
| Canal position, command boundaries | Punjab Irrigation Department; IFPRI; IWMI | **To establish** |
| Electricity tariff regime | NEPRA tariff determinations | To establish |
| Tubewell density | Pakistan Agricultural Census | To establish |
| Observation wells (validation) | PCRWR, provincial monitoring | On request |
| Historical tenure class | Settlement reports, canal-colony boundaries | Doubtful in machine-readable form |

## Principles

- No restricted or confidential data goes into this repository.
- Every dataset is cited with version and access date.
- The assembled, joinable dataset will be released with a DOI (Zenodo) before any analysis is
  published, so that others can use it whatever the analysis finds.
