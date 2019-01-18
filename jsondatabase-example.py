import json
from collections import namedtuple

data ="""
{
  "item": {
    "icon": "http:\/\/services.runescape.com\/m=itemdb_rs\/1545055868407_obj_sprite.gif?id=444",
    "icon_large": "http:\/\/services.runescape.com\/m=itemdb_rs\/1545055868407_obj_big.gif?id=444",
    "id": 444,
    "type": "Mining and Smithing",
    "typeIcon": "http:\/\/www.runescape.com\/img\/categories\/Mining and Smithing",
    "name": "Gold ore",
    "description": "This needs refining.",
    "current": {
      "trend": "neutral",
      "price": 164
    },
    "today": {
      "trend": "positive",
      "price": "+1"
    },
    "members": "false",
    "day30": {
      "trend": "positive",
      "change": "+7.0%"
    },
    "day90": {
      "trend": "positive",
      "change": "+2.0%"
    },
    "day180": {
      "trend": "negative",
      "change": "-4.0%"
    }
  }
}
"""

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
print (x.item[2], x.item.name)