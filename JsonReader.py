#! -*- coding: utf-8 -*-

import sys
import json

def read_json(ff):
    for l in open(ff):
        l = l.strip()
        j = json.loads(l)
        yield j