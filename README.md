# sqlalchemy-challenge
### In this section, we use Python and SQLAlchemy to do a basic climate analysis and data exploration of our climate database.
---
# Precipitation Analysis
![precipitation](https://github.com/bgrullon/sqlalchemy-challenge/assets/45550119/fb29d1b1-941a-42a3-b50e-006608ae85fe)
---
# Station Analysis
![Temperature vs Frequency](https://github.com/bgrullon/sqlalchemy-challenge/assets/45550119/24680aba-b7ed-4e38-ba87-7b93886c0c7e)
---
# Climate App

- /
  - Start at the homepage.
  - List all the available routes.

- /api/v1.0/precipitation
  - Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
  - Return the JSON representation of your dictionary.

- /api/v1.0/stations
  - Return a JSON list of stations from the dataset.

- /api/v1.0/tobs
  - Query the dates and temperature observations of the most-active station for the previous year of data.
  - Return a JSON list of temperature observations for the previous year.

- /api/v1.0/start
- /api/v1.0/start/end
  - Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
  - For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
  - For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
