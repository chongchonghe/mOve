#!/usr/bin/env python3

from __future__ import print_function
import os
import sys
import json
import logging

# JSON_PATH = "~/.config/workon/projects.json"

logging.basicConfig(format='')

def find_match(elements, obj):
    """Find the matching string in a list of elements.
    Args
        elements (list):
        obj (str): object fuzzy string

    e.g.
    >>> find_match(['abc', 'abcd'], 'ab']

    """

    exact_match = []
    fuzzy_match = []
    for ele in elements:
        try:
            if ele[:len(obj)].lower() == obj.lower():
                if len(ele) == len(obj):
                    exact_match.append(ele)
                else:
                    fuzzy_match.append(ele)
        except IndexError:
            continue
    if len(exact_match) > 0:
        if len(exact_match) == 1:
            return exact_match[0]
        else:
            for ele in exact_match:
                if ele[:len(obj)] == obj:
                    return ele
    else:
        if len(fuzzy_match) > 0:
            # return the shortest match
            lens = [len(i) for i in fuzzy_match]
            pick = lens.index(min(lens))
            return fuzzy_match[pick]
        else:
            return None

def test_find_match():
    pairs = [((['abcd', 'abce', 'abc'], 'abc'), 'abc'),
             ((['abcd', 'abce', 'ab'], 'abc'), 'abcd'),
             ((['abcd', 'abce', 'abc'], 'ab'), 'abc'),
             ]
    for pair in pairs:
        inp, outp = pair
        if not find_match(inp[0], inp[1]) == outp:
            print("Test failed")
            return 1
    print("Test succeeded")
    return 0

def main(flag):
    json_fn = os.path.expanduser(os.environ['MOVE_JSON'])
    # json_fn = os.path.expanduser(JSON_PATH)
    if not os.path.isfile(json_fn):
        print(("Couldn't find projects.json file. Please execute 'wo add' first.\n"
               "Check 'wo -h'"),
               file=sys.stderr)
        return '.'
    with open(json_fn, 'r') as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            print("JSONDecodeError. Fix the json file:\n" + json_fn, file=sys.stderr)
            return "."
        flag_match = find_match(list(data.keys()), flag)
        if flag_match is None:
            print("Could not find a good match with {}.".format(flag),
                  file=sys.stderr)
            return "."
        else:
            logging.warning("Working on {} ...".format(flag_match))
            return data[flag_match]["dir"]

if __name__ == "__main__":
    try:
        print(main(sys.argv[1]))
    except BaseException as err:
        print(err, file=sys.stderr)
        print(".")
