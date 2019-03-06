""" Reads CSV data file """

import csv
import sys

from pathlib import Path


def add_sys_path(requested_path):
    """Add the requested_path to the sys.path"""
    sys.path.insert(0, requested_path)


def read_student_file(filepath):
    """ Read the responses from the CSV, returning them in a list of lists """

    # handle nonexistant files
    if Path(filepath).is_file() is False:
        print("filenotfound")
        return ""
    # read the raw CSV data
    with open(filepath, "r") as csvfile:
        csvdata = list(csv.reader(csvfile, delimiter=","))

        # transform into desired output
    responses = list()
    for record in csvdata[1:]:
        temp = list()
        temp.append(record[0].replace('"', ""))
        for value in record[1:]:
            if value == "True":
                temp.append(True)
            elif value == "False":
                temp.append(False)
    responses.append(temp)
    return responses