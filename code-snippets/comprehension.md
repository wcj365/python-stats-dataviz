# Comprehension
Comprehension is a Python feature for concise and elegant code.
It applies to all collection types.
The most commonly used comprehension is list comprehension.

## Example
The `result` variable is a list of dictionaries:
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
