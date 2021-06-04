# hack-the-climate-coextremes


# Work Description

Our work is split into two parts:

1) Analysing co-occurence of extreme event of high wind conditional to extreme low temperature, looking at two different time slices [2020,2030], [2050,2060]. The analysis looked at the Chi function (defined in Coles et al., 2000), considering 4 locations for the wind variables. The results consists of:
  - Heat map of the Chi function P(W>x|T->-x) 
  - The variability of the probability of joint extremes wrt to base period [2010,2020]
  
2) Analysing co-occurence of extreme events over the next 3 decades high temperature conditional to extreme at a given base point. Here we have down three things:
  - Produce plots for chi for a varying basepoint
  - Heatwave buddy finder
  - Measuring size (statistically) of heatwaves via connected sets.


Results:
- The presentation of results in 1) can be found in the folder: ```coextreme_wind_temp/windfarm_coextremes.ipynb``` 

- The presentation of the results in 2) in the file ```coextreme_heatwaves/heatwave_buddies.ipynb```.

Preview: 

**Screenshot of the tool for 1) in `coextreme_wind_temp/windfarm_coextremes.ipynb`**:

![Screenshot from 2021-06-04 12-45-24](https://user-images.githubusercontent.com/13718882/120797082-790f9380-c533-11eb-8734-3b4109a3d09b.png)

**Screenshot of the tool for 2) in `coextreme_heatwaves/heatwave_buddies.ipynb`**:

![Screenshot from 2021-06-04 12-52-03](https://user-images.githubusercontent.com/13718882/120797272-b5db8a80-c533-11eb-8a66-c3c69f5a441c.png)


# Environment

On UCL JupyterHub:

- required environment `conda config --add envs_dirs /shared/groups/jrole001/geog0121/envs`
- required data `ln -s /shared/groups/jrole001/geog0121/UKCP18 $HOME/UKCP18`

For our packages there is a `hack.yml` from which a conda-environment can be created. Additionally for the  `windfarm_coextremes.ipynb` and for the  `heatwave_buddies.ipynb` you will need to install `gradio` from pip: `pip3 install gradio`.

## additional files - calculations
- `visualise.py`: returns 3 plots (1 for every decade) showing the Chi values on the co-occurence of heatwaves conditional to extreme for a given base point. Usage demonstrated in `visualise_test.ipynb`
- `VISUALISAION.ipynb`: interactive generation of plots (as above) based on the chosen decade and UK postcode

## additional files - data
- ```chi_vals[...].txt``` : Chi values on the co-occurence of heatwaves conditional to extreme for all UK base points, for a given decade
- ```derotated_coordinates.csv```: aggregated data on grid point coordinates + postcodes
