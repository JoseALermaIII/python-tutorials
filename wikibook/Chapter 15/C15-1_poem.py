#!/usr/bin/env python3
# ~*~ coding: utf-8 ~*~

poem = ["<B>", "Jack", "and", "Jill", "</B>", "went", "up", "the",\
"hill", "to", "<B>", "fetch", "a", "pail", "of", "</B>",\
"water.", "Jack", "fell", "<B>", "down", "and", "broke",\
"</B>", "his", "crown", "and", "<B>", "Jill", "came",\
"</B>", "tumbling", "after"]

def get_bolds(text):
    true = 1
    false = 0
    ## is_bold tells whether or not we are currently looking at
    ## a bold section of text.
    is_bold = false
    ## start_block is the index of the start of either an unbolded
    ## segment of text or a bolded segment.
    start_block = 0
    for index in range(len(text)):
        ## Handle a starting of bold text
        if text[index] == "<B>":
            if is_bold:
                print("Error: Extra Bold")
            ## print "Not Bold:", text[start_block:index]
            is_bold = true
            start_block = index + 1
        ## Handle end of bold text
        ## Remember that the last number in a slice is the index
        ## after the last index used.
        if text[index] == "</B>":
            if not is_bold:
                print("Error: Extra Close Bold")
            print("Bold [", start_block, ":", index, "]", text[start_block:index])
            is_bold = false
            start_block = index + 1

get_bolds(poem)
