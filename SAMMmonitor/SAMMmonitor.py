'''
SAMMmonitor.py
Original created: 270619
Python Version: 3.9.0
Purpose: Script for screening APEX3D-generated ion mobility data
and report intensities of a list of targets within a preset threshold. 
Input: Data folder containing .csv APEX3D data (ex: from 3D-TWIMS-extract.py)
Summary output .csv is exported to data directory.
'''

import os
import csv
from pathlib import Path
from datetime import datetime, date, time, timezone

# time functions
print('program start at: ' + str(datetime.now()) + '\n---===---\n')
hmmss = str(datetime.now()).split(' ')[1][0:8].replace(':', '')
day = str(datetime.now()).split(' ')[0][2:10].replace(':', '')

# Directories:
monitorDir = str(os.getcwd())

# refer to : for data location:
data_directory = Path(
    r'D:\\2-SAMM\Data\EJ3-60-SAMM3-MoMonitoring\Raw Data\APEX Output')
    # D:\2-SAMM\Data\EJ3-60-SAMM3-MoMonitoring\Raw Data\APEX Output

# path of CSV file with target analytes
targets_csv = Path(
    r'D:\\2-SAMM\Programs\SAMM\SAMMmonitor\experimental-target-list.csv')

# mz_tolerance = error tolerance for target m/z value (default: 1 m/z)
# mob_tolerance = error tolerance for mobility, in percentage  (default: 0.05 m/z)
mz_tolerance, mob_tolerance = 1.0, 0.05


csv_files = [os.path.join(data_directory, csv_f)
             for csv_f in os.listdir(data_directory)]


# Functions:
def read_data_csv(csv_file, delimitchar=',', headers=True):
    '''
    [Reads input csv file excluding headers and returns contents as list of lists]
    Arguments: csv_file {str} -- [full str path to .csv file]
    **kwargs: delimitchar {str} -- [delimiter for csv] (default: {','})
    Returns: data_list {list} -- [list of csv data by row]
    '''
    data_list = []  # create new list
    with open(csv_file) as f:
        # open comma-delimited csv
        csvreader = csv.reader(f, delimiter=delimitchar)
        for row, columns in enumerate(csvreader):
            if (headers and row > 0) or not headers:
                data_list.append([columns[i] for i in range(0, len(columns))])
            else:
                pass
    return data_list

def fetch_target_data(target_file):
    '''
    [Returns dictionary of analyte targets from .csv file]
    Arguments:
    target_file {str} -- [full string path to targets CSV]
    Returns:
    target_dict {dict} -- [dictionary of name, m/z, mobility from target list]
    '''
    print(f'Retrieving analyte formula, base peak m/z, observed drift time (ms) from target_file: \n {target_file}\n')
    target_dict = {}
    
    target_data_file = read_data_csv(target_file)

    for data in target_data_file:
        target, target_mz, target_mob = data[0], float(data[2]), float(data[3])
        target_dict[target] = {'mz': target_mz, 'mobility': target_mob}
        
    return target_dict



# put the experimental reference data into dictionary
input1 = fetch_target_data(targets_csv)

# apex 3d Data file - single test:
testData = read_data_csv(csv_files[0])

print(testData)


practice_mz = ### continue

# check for ms hit
# for analyte in input1.keys():
#     formula = str(analyte)
#     analyte_mz = input1.get(analyte).get('mz')
#     analyte_dt = input1.get(analyte).get('mobility')
#     # check if the above information matches the current line of data in the current apex3d data file
#     if target_mz_from_file >= target_mz_from_file - mz_tolerance and target_mz_from_file <= target_mz_from_file + mz_tolerance:
#         # and if the mobility is within specified range (default 5% chosen)
#         mob_delta = target_mob * 0.05
#         if data_mob >= target_mob - mob_delta and data_mob <= target_mob + mob_delta:
#             # sum signals and combine with analyte name vs. time
#             return True
#     else:
#         print('-')
#         return False






###
# ending script and testing notes:
# test csv: input1
# target_dict, data_directory, mz_tolerance, mob_tolerance

import sys
sys.exit('Stopping Program....')
###


def get_output_csv_path(input_csv):
    ''' [Find output directory if it exists (otherwise create it). Naming scheme based on input data name.]

    Arguments:
        data_csv = [CSV in which original APEX3D output data is stored]
        target_dict = [From fetch_target_data, list of target m/s vs. mob pairs provided by user in CSV form]
        mz_tolerance = [Selected threshold entered for m/z tolerance required for a 'hit' to be recorded]
        mob_tolerance = [Selected threshold entered for mobility tolerance in BINS required for a 'hit' to be recorded]
        mz_units='abs' = [Changed if absolute m/z threshold is not used (i.e. a percentage instead)]

    Returns:
        targ_dict = [A dictionary of targets returning True from check_hit]

    NOTE: Incompatible with DriftScope v 2.2 (ex: APEX exports use col 4 of .csv file)
    '''
    input_csv_name = os.path.basename(input_csv).replace('.csv', '')

    output_folder = os.path.join(monitorDir + 'SAMMmonitor Output - ' + str(hmmss))
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    return os.path.join(output_folder, f'{input_csv_name}-monitor.csv')


def write_output_csv(output_csv, headers=['target_molecule', 'id', 'obs_mz', 'RT', 'obs_mobility', 'intensity'],
                     delimitchar=','):

    with open(output_csv, 'w') as write_file:

        write = csv.writer(write_file, delimiter=delimitchar)
        write.writerow(headers)


def append_output_csv(output_csv, write_list, delimitchar=','):

    # print(f'for {output_csv}, write list = {write_list}')
    with open(output_csv, 'a') as opened_file:
        writer = csv.writer(opened_file, delimiter=delimitchar)
        writer.writerow(write_list)


def write_hits_for_single_csv(data_csv, target_dict, mz_tolerance, mob_tolerance,
                              out_folder=None, headers=['Target Formula', 'Index',
                                                        'Observed m/z', 'm/z No Cal', 'RT', 'Intensity', 'Area', 'Counts', 'Mobility']):
    targ_dict = screen_hits_for_single_csv(
        data_csv, target_dict, mz_tolerance, mob_tolerance
        )
    output_csv = get_output_csv_path(data_csv)
    write_output_csv(output_csv, headers)

    for target_molecule, hits_lists in targ_dict.items():

        for hit in hits_lists:
            if len(hit) > 0:
                write_list = [target_molecule]
                write_list.extend(hit)
                append_output_csv(output_csv, write_list)


def write_hits_multiple_csvs(target_dict, csv_folder,
                             mz_tolerance, mob_tolerance,
                             out_folder=None):
    for entry in csv_files:
        write_hits_for_single_csv(entry, target_dict,
                                  mz_tolerance, mob_tolerance,
                                  out_folder)


# Module initiation and main
def main():
    target_dict = fetch_target_data(targets_csv)
    
    # write_hits_multiple_csvs(target_dict, data_directory,
    #                          mz_tolerance, mob_tolerance)


if __name__ == '__main__':
    main()
    # main(data_directory, targets_csv, mz_tolerance, mob_tolerance)
    print('\n---===--- \nprogram end at: ' + str(datetime.now()))

### To do:
# sum output of counts for each target mz





## unused / testing

# def list_csv_data_files(data_directory):
#     '''
#     [Returns list of full file paths for data files in directory]
#     Arguments: data_directory {str} -- [full string path to data folder]
#     Returns:
#     files {list} -- [list of full string paths to data files]
#     '''
#     files = [os.path.join(data_directory, csv_f)
#              for csv_f in os.listdir(data_directory)]
#     return files
