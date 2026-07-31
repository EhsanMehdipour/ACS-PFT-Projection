# acs-projection

## Conda environment
### Create
Firstly, a conda environmentl should be install with all the used modules and their dependencies. It is possible to directly create this environment from an *environment.yml* file using the following code:

```bash
conda env create -f environment.yml

```
### Activate

If you have jupyter lab install already in your computer, you can add the environment kernal to access the environment in jupyter lab.

```bash
source activate acs-projection
python -m ipykernel install --user --name acs-projection --display-name "acs-projection"
conda deactivate
```

you can now start the jupyter lab and change the kernel in top right to "acs-projection".

### Configuration file (config.ini)

All the parameters needed for running the codes are entered in the config.ini file. There is a brief explanation for most of the parameters.

### pft_retrieval_constants.py

Please check the PFT names in the python code pft_retrieval_constants.py. Change the name of the PFT, PFT_limits, PFT_longname accordingly.

