#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:56:43 2021

@author: victorbarrera
"""

from sys import argv
from itertools import permutations, dropwhile


barcodes_file=argv[1]
unknown_barcodes_file=argv[2]


barcodes_dict = {}

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

def barcode_section(line): return line != '### Columns: Index_Sequence Hit_Count\n'
barcodes_found=[]
    
with open(unknown_barcodes_file,'r') as unknown_barcodes_file_fh:
    for line in dropwhile(barcode_section, unknown_barcodes_file_fh):
        if line.startswith("#"):
            next
        else:
            barcode_unknown_found=str(line.rstrip().split()[0])
            if barcode_unknown_found in barcodes_dict.keys():
                barcodes_found.append(barcodes_dict[barcode_unknown_found])
                
print("Barcodes found:")
print(barcodes_found)