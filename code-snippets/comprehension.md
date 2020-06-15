# Comprehension
Comprehension is a Python feature for concise and elegant code.
It applies to all collection types.
The most commonly used comprehension is list comprehension.

## Example
This is a real-world example from a machine learning project. The The `result` variable is a list of dictionaries:

![](https://github.com/wcj365/python-stats-dataviz/blob/master/images/comprehension_example.jpg)
```python
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

```python
r = [x for x in result if x["properties"]["contour"] == 1]
```

Here, we also see the example of accessing the `value` of a dictionary using the `key` in a nested dictionary (dict within a dict). A dictionary contains *key-value pairs*.
