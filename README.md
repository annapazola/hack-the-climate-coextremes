# hack-the-climate-coextremes


# Work Description

Our work is split into two parts:
1) Analysing co-occurence of extreme events over the next 3 decades of wind conditional to extreme low temperature
2) Analysing co-occurence of extreme events over the next 3 decades high temperature conditional to extreme at a given base point. Here we have down three things:
  - Produce plots for chi for a varying basepoint
  - Heatwave buddy finder
  - Measuring size (statistically) of heatwaves via connected sets.

The presentation of results in 1) can be found in the file: ```windfarm_coextremes.ipynb``` and for 2) in the file ```heatwave_buddies.ipynb```.

Preview: 

**Screenshot of the tool for 1) in `windfarm_coextremes.ipynb`**:

![Screenshot from 2021-06-04 12-45-24](https://user-images.githubusercontent.com/13718882/120797082-790f9380-c533-11eb-8734-3b4109a3d09b.png)

**Screenshot of the tool for 2) in `heatwave_buddies.ipynb`**:

![Screenshot from 2021-06-04 12-52-03](https://user-images.githubusercontent.com/13718882/120797272-b5db8a80-c533-11eb-8a66-c3c69f5a441c.png)


# Environment

On UCL JupyterHub:

- required environment `conda config --add envs_dirs /shared/groups/jrole001/geog0121/envs`
- required data `ln -s /shared/groups/jrole001/geog0121/UKCP18 $HOME/UKCP18`

For our packages there is a `hack.yml` from which a conda-environment can be created. Additionally for the  `windfarm_coextremes.ipynb` and for the  `heatwave_buddies.ipynb` you will need to install `gradio` from pip: `pip3 install gradio`.
