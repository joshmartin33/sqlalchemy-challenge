
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/joshmartin33/sqlalchemy-challenge">
    <img src="images/logo1.png" alt="Logo" width="110" height="70">
  </a>

<h3 align="center">sqlalchemy-challenge</h3>

  <p align="center">
    Honolulu, Hawaii Climate Analysis
    <br />
    <a href="https://github.com/joshmartin33/sqlalchemy-challenge"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/joshmartin33/sqlalchemy-challenge/blob/main/SurfsUp/climate_starter.ipynb">View Analysis</a>
    ·
    <a href="https://github.com/joshmartin33/sqlalchemy-challenge/issues">Report Bug</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#part-1">Part 1: Analyse and Explore the Climate Data</a></li>
      <ul>
        <li><a href="#getting-started">Getting Started</a></li>
      </ul>
    <li><a href="#part-2">Part 2: Design Your Climate App</a></li>
    <li><a href="#creators">Creators</a></li>
    <li><a href="#citing-and-referencing">Citing and Referencing</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

I am off on a LONG vacation to Honolulu in Hawaii. To help with my trip planning I will complete a climate anaylsis on the area.

For this project, I will complete a climate analysis about Honolulu, Hawaii using Python and SQLAlchemy. 
Then I will design a Flask API based on the queries outlined in the analysis. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Part 1 -->
## Part 1

In this section, I’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, I’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, I completed the following steps:
  <ol>
<li>Use the SQLAlchemy create_engine() function to connect to your SQLite database.</li>
<li>Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.</li>
<li>Link Python to the database by creating a SQLAlchemy session.</li>
<li>Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.</li>
 </ol>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### GitHub

  <ol>
<li>Clone the repo</li>
   git clone https://github.com/joshmartin33/sqlalchemy-challenge
<li>Open file called climate_starter.ipynb in Jupyter Notebook</li>
<li>Click on "Run all"</li>
<li>Results will be printed to the screen</li>
 </ol>


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Part 2 -->
## Part 2

1. Create a python file called get_pass.py and save it in the folder "SQL-challenge".

2. Within the get_pass.py copy and paste the code below. 

```
# PG ADMIN password
password = "ENTER YOUR PASSWORD HERE"
```

3. Enter in your password for PG Admin.

4. Locate file called bonus_visualisation.ipynb found in folder "SQL-challenge"

5. Open bonus_visualisation.ipynb in any application that can run a Jupyter notebook.

6. Refresh and clear the kernal. Click on "Run all"

Results will be displayed


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Creators -->
## Creators

Josh Martin - <a href="https://github.com/joshmartin33">GitHub</a>


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Citing and Referencing -->
## Citing and Referencing

* Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, <a href="https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml">Link</a>


<p align="right">(<a href="#readme-top">back to top</a>)</p>