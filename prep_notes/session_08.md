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
dirName = 'C:\\Users\\jaywang\\Assignment07\CollegeScorecard_Raw_Data';
# Get the list of all files in directory tree at given path
listOfFiles = getListOfFiles(dirName)
```

## Use forward slash ("/") which is cross-platform (works in Windows, Linux, Mac)

```python
os.remove('C:\\Users\\jaywang\\Assignment07\\CollegeScorecard_Raw_Data\\data.yaml')
os.remove('C:\\Users\\jaywang\\Assignment07\\CollegeScorecard_Raw_Data\\Crosswalks.zip')
os.remove('C:\\Users\\jaywang\\Assignment07\\CollegeScorecard_Raw_Data\\a.DS_Store')
os.remove('C:\\Users\\jaywang\\Assignment07\\CollegeScorecard_Raw_Data\\FieldOfStudyData1415_1516_PP.csv')
os.remove('C:\\Users\\jaywang\\Assignment07\\CollegeScorecard_Raw_Data\\FieldOfStudyData1516_1617_PP.csv')
```
## Don't Write Repetitive Code, Use Loops Instead

```python
df1 = pd.read_csv('C:\\Users\jaywang\\Assignment07\\CollegeScorecard_Raw_Data\\MERGED1996_97_PP.csv', usecols = ["UNITID", "INSTNM", "STABBR", "REGION", "ADM_RATE", "TUITIONFEE_IN"])
......
df26 = pd.read_csv('C:\\Users\\jaywang\\Assignment07\\CollegeScorecard_Raw_Data\\MERGED2018_19_PP.csv', usecols = ["UNITID", "INSTNM", "STABBR", "REGION", "ADM_RATE", "TUITIONFEE_IN"])
```
## Make the charts larger with figsize option.
```python
fig, ax = plt.subplots(figsize=(10,8))
```
## Insert Year at appropriate time
```python
from os import listdir

filepaths = [f for f in listdir(path) if f.endswith('.csv')]
df = pd.concat(map(pd.read_csv, filepaths))
......
small_df = df[["UNITID", "INSTNM", "STABBR", "REGION", "ADM_RATE", "TUITIONFEE_IN"]]
......
select_UMBC = small_df.loc[df['INSTNM'] == 'University of Maryland-Baltimore County']

UMBC_df = select_UMBC

UMBC_df.insert(0, "Year", [1996,1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018], True) 

print(UMBC_df)
```
