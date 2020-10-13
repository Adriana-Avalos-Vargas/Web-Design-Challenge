## Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "WebVisualizations/cities_weather.csv"

# Read Purchasing File and store into Pandas data frame 
cities_data = pd.read_csv(file_to_load)
# to save as html file 
# named as "Table" 
cities_data.to_html("Table.htm") 
  
# assign it to a  
# variable (string) 
html_file = cities_data.to_html() 
