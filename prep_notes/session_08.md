# Preparation Notes for Session 08
## Avoid Over Engineering
```python
#https://thispointer.com/python-how-to-get-list-of-files-in-directory-and-sub-directories/
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles
dirName = 'C:\\Users\\shrut\\Assignment07\CollegeScorecard_Raw_Data';
# Get the list of all files in directory tree at given path
listOfFiles = getListOfFiles(dirName)
```
