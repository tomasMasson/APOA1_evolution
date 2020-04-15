#!/usr/bin/env python3

import argparse
from Bio.PDB import PDBParser

def filter_contiguous_residues(array):
    '''Takes a .csv file containing coevolution pairs and return only pairs with a separation of 6 or more residues.'''
    with open(array, 'r') as fh:
        next(fh)
        coev_residues = []
        for row in fh:
            i = int(row.split(',')[0])+44
            j = int(row.split(',')[1])+44
            if j-i > 5 and (j-i) % 11 != 0:
                coev_residues.append((i, j, row.split(',')[2]))
                        
    return coev_residues

def residues_distance(i, j, structure, threshold):
    '''Returns True if two residues are separated by a distance minor to the threshold.'''
    return structure[j]['CA'] - structure[i]['CA'] < threshold

def interresidues_distance(i, j, structure1, structure2, threshold):
    '''Returns True if two residues are separated by a distance minor to the threshold.'''
    return structure2[j]['CA'] - structure1[i]['CA'] < threshold

def map_residues_structure(coev_residues, monomer, hdl):
    '''Take the first 50 residue pairs that at separated by least than 8 Angstroms in the protein structure.'''
    parser = PDBParser()
    monomer_pdb = parser.get_structure('apoa1_monomer', monomer)
    chain_monomer = monomer_pdb[0]['A']
    hdl_pdb = parser.get_structure('apoa1-hdl', hdl)
    chain_A_hdl = hdl_pdb[0]['A']
    chain_B_hdl = hdl_pdb[0]['B']

    coev_res_mapped = []
    count = 0
    for pair in coev_residues:
        if count < 40: 
            if residues_distance(pair[0], pair[1], chain_monomer, 8):
                coev_res_mapped.append([pair, 'monomer'])
                count += 1
            elif interresidues_distance(pair[0], pair[1], chain_A_hdl, chain_B_hdl, 8):
                coev_res_mapped.append([pair, 'hdl'])
                count += 1
            elif interresidues_distance(pair[0], pair[1], chain_B_hdl, chain_A_hdl, 8):
                coev_res_mapped.append([pair, 'hdl'])
                count += 1
    for item in coev_res_mapped:
        print(f'{item[0][0]} int {item[0][1]} {item[0][2]}{item[1]}')    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('residues', help='File with coevolving residues')
    parser.add_argument('monomer', help='File with monomer structure')
    parser.add_argument('hdl', help='File with hdl apoa1 structure')
    
    args = parser.parse_args()
    residues = args.residues
    monomer = args.monomer
    hdl = args.hdl
    
    residues_filtered = filter_contiguous_residues(residues)
    map_residues_structure(residues_filtered, monomer, hdl)
    

if __name__ == '__main__':    
    main()
