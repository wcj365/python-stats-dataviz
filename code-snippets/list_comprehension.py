#!/usr/bin/bash python3

# to filter the list by selecting only the entries with contour = 1

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
        
r = [x for x in result if x["properties"]["contour"] == 1]

print(r)
