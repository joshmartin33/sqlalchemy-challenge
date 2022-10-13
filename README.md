
<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/joshmartin33/sqlalchemy-challenge">
    <img src="images/logo1.png" alt="Logo1" width="110" height="70">
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
      <ul style="list-style-type:square;">
        <li><a href="#getting-started-part-1">Getting Started</a></li>
      </ul>
    <li><a href="#part-2">Part 2: Design Your Climate App</a></li>
      <ul style="list-style-type:square;">
        <li><a href="#getting-started-part-2">Getting Started</a></li>
      </ul>
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
  <ol style="list-style-type:upper-roman">
<li>Use the SQLAlchemy create_engine() function to connect to your SQLite database.</li>
<li>Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.</li>
<li>Link Python to the database by creating a SQLAlchemy session.</li>
<li>Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.</li>
 </ol>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
### Getting Started Part 1

To get a local copy up and running follow these simple example steps.

#### <u>Jupyter Notebook</u>

  <ol style="list-style-type: lower-alpha;">
<li>Clone the repo</li>
   git clone https://github.com/joshmartin33/sqlalchemy-challenge
<li>Open file called climate_starter.ipynb in Jupyter Notebook</li>
<li>Refresh and clear the kernal.</li>
<li>Click on "Run all"</li>
<li>Results will be printed to the screen</li>
 </ol>


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Part 2 -->
## Part 2

Now that I’ve completed my initial analysis, I’ll design a Flask API based on the queries that I just developed. To do so, I will use Flask to create my routes as follows:

<ol style="list-style-type:upper-roman">
  <li>/</li>
    <ul>
      <li>Start at the homepage.</li>
      <li>List all the available routes.</li>
    </ul>
  <br>
  <li>/api/v1.0/precipitation</li>
    <ul>
      <li>Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.</li>
      <li>Return the JSON representation of the dictionary.</li>
    </ul>
  <br>
  <li>/api/v1.0/stations</li>
    <ul>
      <li>Return a JSON list of stations from the dataset.</li>
    </ul>
  <br>
  <li>/api/v1.0/tobs</li>
    <ul>
      <li>Query the dates and temperature observations of the most-active station for the previous year of data.</li>
      <li>Return a JSON list of temperature observations for the previous year.</li>
    </ul>
  <br>
  <li>/api/v1.0/'start' and /api/v1.0/'start'/'end'</li>
    <ul>
      <li>Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.</li>
      <li>For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.</li>
      <li>For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.</li>
    </ul>
</ol>


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
### Getting Started Part 2

To get a local copy up and running follow these simple example steps.

#### <u>VS Code</u>

  <ol style="list-style-type: lower-alpha;">
    <li>Locate file called app.py found in folder "SurfsUp"</li>
    <li>Open file this file in VS Code</li>
    <li>Click on "Run Python File"</li>
    <li>Resulting http link will be displayed in the "Terminal" (example: http://127.0.0.1:5000/)</li>
    <li>Copy the http link and paste it into a browser</li>
    <li>This will bring you to the "Home" page which displays the avaible routes</li>
    <li>To view the required data copy the highlighted links and paste them to the end of your original http link</li>
    <li>Results will be displayed</li>
 </ol>


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Creators -->
## Creators

Josh Martin - <a href="https://github.com/joshmartin33">GitHub</a>


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Citing and Referencing -->
## Citing and Referencing

* Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, <a href="https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml">Link</a>


<p align="right">(<a href="#readme-top">back to top</a>)</p>