#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:56:43 2021

@author: victorbarrera
"""

import sys
import itertools




barcodes_file=sys.argv[1]
unknown_barcodes_file=sys.argv[2]

barcodes_file_fh=open(barcodes_file,'r')
unknown_barcodes_file_fh=open(unknown_barcodes_file,'r')


barcodes_dict = {}

next(barcodes_file_fh)
for barcode_group in barcodes_file_fh:
    barcode_group_id=str(barcode_group.rstrip().split(",")[0])
    index_i7=str(barcode_group.rstrip().split(",")[1])
    index_ai5=str(barcode_group.rstrip().split(",")[2])
    index_bi5=str(barcode_group.rstrip().split(",")[3])
    comb_list=list(itertools.permutations([index_i7,index_ai5,index_bi5], 2))
    for comb in comb_list:
        barcodes_dict[str("+".join(comb))]=barcode_group_id

for key_val in barcodes_dict.keys():
    print('%s\t' %
          (key_val,
           ))
    

barcodes_file_fh.close()
unknown_barcodes_file_fh.close()