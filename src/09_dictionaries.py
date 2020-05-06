"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
waypoints.append({
        "lat": 123,
        "lon": -1234,
        "name": "a fourth place"
    })

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

# YOUR CODE HERE
a_place_idx = [i for (i, v) in enumerate(waypoints) if v["name"] == "a place"][0]

waypoints[a_place_idx]["lon"] = -130
waypoints[a_place_idx]["name"] = "not a real place"
print(a_place_idx)

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
def print_waypoints(w):
    for i, waypoint in enumerate(w):
        print(f"waypoint {i+1}")
        for k, v in waypoint.items():
            print(f"{k}: {v}")

print_waypoints(waypoints)