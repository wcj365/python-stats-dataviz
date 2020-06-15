# Comprehension
Comprehension is a Python feature for concise and elegant code.
It applies to all collection types.
The most commonly used comprehension is list comprehension.

## Example
The `result` variable is a list of dictionaries:
```Python
result=[{"type":"feature",
        "properties":{"class":"x","contour":0},
        "geometry":{
            "type":"MultiPolygon",
            "coordinates":[[1,2,3],[4,5,6]]
            }
        },
        {"type":"feature",
        "properties":{"class":"x","contour":1},
        "geometry":{
            "type":"MultiPolygon",
            "coordinates":[[1,2,3],[4,5,6]]
            }
        },
        {"type":"feature",
        "properties":{"class":"x","contour":0},
        "geometry":{
            "type":"MultiPolygon",
            "coordinates":[[1,2,3],[4,5,6]]
            }
        }]
```

The task is to filter the list to a subset that only contains dictionaries that has the property `contour` value "1".
Here is the simple one-liner solution using *list comprehension*:

```Python
r = [x for x in result if x["properties"]["contour"] == 1]
```

