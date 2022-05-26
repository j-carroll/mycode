#!/usr/bin/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

# Make all 3 lists/dicts print the following: My eyes! The goggles do nothing!

# Challenge List

x = challenge[2][1] # eyes
y = challenge[2][0] # goggles
z = challenge[3] # nothing

print(f"My {x}! The {y} do {z}!")


# Trial list

x = trial[2]["goggles"] # eyes
y = trial[2]["eyes"] # goggles
z = trial[3]

print(f"My {x}! The {y} do {z}!")


# nightmare list

x = nightmare[0]["user"]["name"]["first"]
y = nightmare[0]["kumquat"]
z = nightmare[0]["d"]


print(f"My {x}! The {y} do {z}!")

