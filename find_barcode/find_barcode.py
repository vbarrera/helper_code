#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:56:43 2021

@author: Victor Barrera
"""

from sys import argv
from itertools import permutations, dropwhile


barcodes_file=argv[1]
unknown_barcodes_file=argv[2]

barcodes_dict = {}

# Load file with all the cellranger indexes
# Create a dictionary for the possible permutations
# Suposedly, only i7 should be first but being less 
# strict on that to capture any possibility

with open(barcodes_file,'r') as barcodes_file_fh:
    next(barcodes_file_fh)
    for barcode_group in barcodes_file_fh:
        barcode_group_id=str(barcode_group.rstrip().split(",")[0])
        index_i7=str(barcode_group.rstrip().split(",")[1])
        index_ai5=str(barcode_group.rstrip().split(",")[2])
        index_bi5=str(barcode_group.rstrip().split(",")[3])
        comb_list=list(permutations([index_i7,index_ai5,index_bi5], 2))
        for comb in comb_list:
            barcodes_dict[str("+".join(comb))]=barcode_group_id

# Load the cellranger stats file that contains the Unknown barcodes found
# (those not assign to any sample). 

def barcode_section(line): return line != '### Columns: Index_Sequence Hit_Count\n'
barcodes_found=[]
    
with open(unknown_barcodes_file,'r') as unknown_barcodes_file_fh:
# Discard all lines until the unknown section
# Discard first line as it contains a text string and
# not barcode information
    for line in dropwhile(barcode_section, unknown_barcodes_file_fh):
        if line.startswith("#"):
            next
        else:
            # extract the barcode information. If the barcode 
            # is among the possible combinations, stored as 
            # keys in the barcodes_dict dictionary, add the 
            # barcode id to the output
            barcode_unknown_found=str(line.rstrip().split()[0])
            if barcode_unknown_found in barcodes_dict.keys():
                barcodes_found.append(barcodes_dict[barcode_unknown_found])
                
print("Barcodes found:")
print(barcodes_found)