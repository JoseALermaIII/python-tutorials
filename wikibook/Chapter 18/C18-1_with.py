#!/usr/bin/env python3
# ~*~ coding: utf-8 ~*~

with open("in_test.txt", "rt") as in_file:
    with open("out_test.txt", "wt") as out_file:
        text = in_file.read()
        data = parse(text)
        results = encode(data)
        out_file.write(results)
    print( "All done.")
