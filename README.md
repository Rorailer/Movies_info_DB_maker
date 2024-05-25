# Movies_info_DB_maker
A Simple python program that reads folder names of format [ Movie Name (Year of Release) ] , retrieves data of the movies and creates a DB.

# Usage
### Change the 'folder' variable to the path of your desired directory, where you have your movie folders. 
If you don't want to do that comment out the following lines
```python
# Directory to Scan folders from
folder = "/media/EXTRA/Movies/"


# Reads the folder names such as [ The Godfather (1972) ] and ignore hidden files on linux which start with '.'
names = [i[:-1] for i in os.listdir(folder) if i[0] != "."]
```

### You may uncomment the following lines to store the file names as a .json file
```python
# with open("test_data.json", "w") as f:
#     json.dump(names, f)
```
### Also uncomment the following lines to read data from a files.
```python
# with open("test_data.json", "w") as f:
#     json.dump(names, f)
```


# Working
The working is pretty straight forward.

1. The program will read all file names in the required folder. NOTE: Format is [Movie Name (Year of relase)] eg. The Godfather (1972).

2. The file name is split into two parts: Movie Name and Year of Release.

3. The program sends request to the API to retrieve search results from the name and filters out the required movie by cross matching the year of release.

4. If a match is found, data is appended into a dataframe which is converted into a DB at the end of execution of the program.


