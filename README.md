# hack-the-climate-coextremes


# Work Description

Our work is split into two parts:
1) Analysing co-occurence of extreme events over the next 3 decades of wind conditional to extreme low temperature
2) Analysing co-occurence of extreme events over the next 3 decades high temperature conditional to extreme at a given base point. Here we have down three things:
  - Produce plots for chi for a varying basepoint
  - Heatwave buddy finder
  - Measuring size (statistically) of heatwaves via connected sets.

The presentation of results in 1) can be found in the file: ```windfarm_coextremes.ipynb``` and for 2) in the file ```heatwave_buddies.ipynb```.


# Environment

on UCL JupyterHub:

required environment
```conda config --add envs_dirs /shared/groups/jrole001/geog0121/envs```

required data
```ln -s /shared/groups/jrole001/geog0121/UKCP18 $HOME/UKCP18```

For our packages there is a `hack.yml` from which a conda-environment can be created. Additionally for the  `windfarm_coextremes.ipynb` and for the  `heatwave_buddies.ipynb` you will need to install `gradio` from pip: `pip3 install gradio`.
