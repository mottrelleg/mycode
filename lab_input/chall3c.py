#!/usr/bin/env python3
hard= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

print(f"My {hard[0]['user']['name']['first']}! The {hard[0]['kumquat']} do {hard[0]['d']}")

print("My " + hard[0]["user"]["name"]["first"] +"! " + "The " + hard[0]["kumquat"] + " do " + hard[0]["d"] +"!")
