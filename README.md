[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21729144.svg)](https://doi.org/10.5281/zenodo.21729144)

# ACS PFT Projection

This repository contains Jupyter notebooks for estimating chlorophyll-*a*
concentrations of phytoplankton functional types (PFTs) from particulate
absorption spectra measured with a WET Labs ac-s. The retrieval uses empirical
orthogonal functions (EOFs) and regression coefficients derived from matched ACS
and HPLC observations.

The projected groups are total chlorophyll-*a*, diatoms, dinoflagellates,
haptophytes, green algae, and prokaryotic phytoplankton.

## Contents

- `ACS_projection.ipynb` performs the standard PFT projection.
- `ACS_projection_with_uncertainty.ipynb` processes high-frequency observations,
  bins the results, and estimates within-bin uncertainty.
- `ACS_validation_HPLC_matchup.ipynb` compares ACS-derived concentrations with
  discrete HPLC measurements.
- `Coefficients/` contains the EOF and regression coefficients used by the
  projection notebooks.
- `config_PS113.ini` and `config_PS113-unc.ini` contain the input paths and
  processing options for the two projection workflows.
- `constants.py` defines the PFT names and concentration limits.

Cruise absorption, wavelength, navigation, and HPLC validation data are not
included in this repository.

## Setup

Create the Conda environment and register its Jupyter kernel:

```bash
conda env create -f environment.yml
conda activate acs-projection
python -m ipykernel install --user --name acs-projection --display-name "acs-projection"
```

Jupyter Lab is not included in the environment file. Use an existing Jupyter
installation or install it with:

```bash
conda install -n acs-projection -c conda-forge jupyterlab
```

## Usage

1. Add the required ACS and navigation data or update their paths in the relevant
   configuration file.
2. Make sure the configured output and figure directories exist.
3. Open the desired projection notebook from the repository root.
4. Select the `acs-projection` kernel and run all cells.

The notebooks produce PFT concentration datasets in NetCDF format and optional
figures. The standard workflow also exports CSV files, while the uncertainty
workflow writes within-bin standard-deviation products.

The validation notebook contains dataset-specific file paths that must be updated
before use.

## License

This project is licensed under the GNU General Public License v3.0. See
[`LICENSE`](LICENSE).
