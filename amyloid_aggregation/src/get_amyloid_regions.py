#!/usr/bin/env python3

import argparse
from os import listdir
from os.path import join
import more_itertools as mit


def apr_distribution(data, score):
    """
    Parse TANGO predictions into a list
    containing the centroid position of
    each aggregation-prone region (APR).
    """

    with open(data, 'r') as fh:
        next(fh)
        residues = [float(row.split()[5]) for row in fh]
    score = score

    regions = [index for index, res in enumerate(residues, 1)
               if res >= score]
    apr = []
    for group in mit.consecutive_groups(regions):
        group = list(group)
        position = (group[-1] + group[0]) // 2
        length = group[-1] - group[0] + 1
        apr.append([position, length])
    return apr


def get_species_taxon(species_name, taxons_table):
    """
    Retrieve the taxon (Mammalia, Tetrapods,
    Actinopterygii or Sapcopterygii) based on
    the species name.
    """
    with open(taxons_table, 'r') as fh:
        taxons_dic = {line.split(',')[1]: line.strip().split(',')[2] for line in fh}
    return taxons_dic[species_name]


def aggregate_results(results_dir, score, taxons):
    """
    Collects TANGO scores from all files present
    in a directory and assign them a taxonomy field.
    """
    print("Species,Taxon,Position,Lenght")
    files = [file for file in listdir(results_dir) if file.endswith(".txt")]
    for file in files:
        file_path = join(results_dir, file)
        results = apr_distribution(file_path, score)
        species_name = file.split('.txt')[0]
        taxon = get_species_taxon(species_name, taxons)
        for record in results:
            print(f'{species_name},{taxon},{record[0]},{record[1]}')


def main():
    '''Command line argument parser. '''

    parser = argparse.ArgumentParser()
    parser.add_argument('data',
                        help='TANGO outputs directory')
    parser.add_argument('score',
                        type=int,
                        help='Aggregation score threshold')
    parser.add_argument('taxons',
                        help='Taxons identifiers')
    args = parser.parse_args()
    data, score, taxons = args.data, args.score, args.taxons
    aggregate_results(data, score, taxons)


if __name__ == '__main__':
    main()
