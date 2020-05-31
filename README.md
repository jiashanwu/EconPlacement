# EconPlacement

This project is an exercise to practice web-scrapping and the use of Regex. In this project, I web srape the placement data from econ department websites. My current focus is on US universities. The selected set of universities can be found [here](https://github.com/jiashanwu/EconPlacement/blob/master/placement_univ_acronym.xlsx). The data is gathered from us news.

## Web scrapping scripts and placement by universities

I have included several example web scrapping scripts in [here](https://github.com/jiashanwu/EconPlacement/tree/master/Webscrapping). By executing the [runAll](https://github.com/jiashanwu/EconPlacement/blob/master/RunAll.ipynb) program, I combine all placement data into one table.

## Cleaning the data

The challenge is on how to clean the placement data. Different universities follow different rules in describing the same placement (e.g. "Fudan" versus "Fudan University" versus "Assistant Prof, Fudan University" versus "School of Economics, Fudan University"). I adapt the named entity labeling under Python NLP module. More details can be found [here](https://github.com/jiashanwu/EconPlacement/blob/master/CleanData_v1.ipynb).

## Preliminary Analysis

Several analysis results are included [here](https://github.com/jiashanwu/EconPlacement/blob/master/InitAnalysis_v1.ipynb): 1. total PhD counts by year; 2. Academics and non-Academics placement; 3. Most favorable universities by cerntain employers, etc.
