# Assignment #1

```

for year in years:
path = '/Users/masoud/Downloads/names/yob%d.txt' % year
frame = pd.read_csv(path, names=columns)

```

You would need to indent within the for loop:

```
for year in years:
    path = '/Users/masoud/Downloads/names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
```

```
import json
path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt' 
records = [json.loads(line) for line in open(path)]
```

This is a common issue related to absolute path vs relative path. also need to know what is your current path. Remind me to cover this.
