#!/usr/bin/env python3
import json

inventory = {
    "all": {
        "hosts": ["localhost"],
        "vars": {
            "ansible_connection": "local"
        }
    }
}

print(json.dumps(inventory))

