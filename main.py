import os
import sys
from deleteperiods import delete_per
from dateformat import find_year

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_folder>")
	sys.exit(1)

folder_path = sys.argv[1]

find_year(folder_path)
delete_per(folder_path)