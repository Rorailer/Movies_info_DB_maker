#!/usr/bin/venv python3
import os
import json
import sqlite3 as sql

import pandas
import requests

# Base URL of YTS API
url = "https://yts.mx/api/v2/list_movies.json"


# Directory to Scan folders from
folder = "/media/EXTRA/Movies/"


# Reads the folder names such as [ The Godfather (1972) ] and ignore hidden files on linux which start with '.'
names = [i[:-1] for i in os.listdir(folder) if i[0] != "."]

# If you want to store the list in a file uncomment the following two lines

# with open("test_data.json", "w") as f:
#     json.dump(names, f)


# Creating a DataFrame With Attributes: Name, Year, Rating, Genres, IMDB ID
df = pandas.DataFrame(columns=["Name", "Year", "Rating", "Genres", "IMDB ID"])

# Read the 'names' list from a file if a file was already created

# with open("test_data.json", "r") as f:
#     names = json.load(f)

# Main for loop that will loop through the files names and gather data.
for name in names:
    
    try:
        # Splitting folder name into a list containing Name and Year
        x = name.split(" (")
        
        #Searching for the movie using name.
        info = requests.get(url + "?query_term=" + x[0])
        info = info.json()

        # Checking if atleast one movie was found.
        if info["data"]["movie_count"] != int(0):
            
            # Looping through response ( if more than one movie was found)
            for i, movie in enumerate(info["data"]["movies"]):
                #debug
                # print(f"Year: {x[1]}, search: {movie['year']}")

                #Checking if the year of release is same.
                if str(movie["year"]) == x[1]:
                    
                    # Storing required movie data into a list
                    data = [
                        # "Name"
                        x[0],
                        # "Year"
                        x[1],
                        # "Rating"
                        movie["rating"],
                        # "Genres"
                        str(movie["genres"]),
                        # "IMDB ID"
                        movie["imdb_code"],
                    ]

                    # Writing aquired data into the DataFrame
                    df.loc[len(df)] = data
                    
                    print(f"Done {len(df)}")

                else:
                    pass
    
    # Server/API side error
    except requests.exceptions.RequestException as e:
        print(f"Request error for {name}: {e}")
    
    # Program/Data Error
    except (ValueError, KeyError) as e:
        print(f"Error processing {name}: {e}")

print(df)

# Creating a connection (table)
connection = sql.connect("Movies.db")

# Writing the connection (table) to a file.
df.to_sql("movies", connection, if_exists="replace")


# Commit changes
connection.commit()

# Close Connection (table)
connection.close()
