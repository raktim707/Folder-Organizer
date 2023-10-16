#!/usr/bin/env python3

import os, shutil, sys
import argparse

parser = argparse.ArgumentParser(prog='ProgramName',
                    description='What the program does')

current_dir = os.getcwd()

parser.add_argument("-s", "--source", help="source path", default=current_dir)

parser.add_argument("-d", "--dest", help="destination path")

parser.add_argument("-f", "--file", help= "file type", choices=['image', 'video', 'music', 'sheet', 'pdf', 'doc'])

args = parser.parse_args()

dest_path = args.dest
source_path = args.source

file_type = args.file

extensions = {
	'music': ['mp3', 'wav', 'flac'], 
	'image': ['jpg', 'jpeg', 'png'],
	'video': ['mp4', 'webm', 'mkv', 'flv', 'avi'],
	'sheet': ['xlsx', 'csv', 'xls', 'xlsb'],
	'pdf': ['pdf'],
	'doc': ['docx', 'doc']
	}

#check if folders path exists
def path_verifier(folder_path):
	if folder_path:
		if os.path.exists(folder_path):
			return True
		else:
			return False
	else:
		return False


#main function
def fileOrganize(file_type: str, dest_dir: str, source_dir: str):
	if dest_dir:
		dest_exist = path_verifier(dest_dir)
		if not dest_exist:
			os.mkdir(dest_dir)
			print("Destination folder created at: ", dest_dir)
	
	if file_type and path_verifier(source_dir):
		count = 0
		all_files = os.listdir(source_dir)
		extension = extensions[file_type]
		for item in all_files:
			name, ext = os.path.splitext(item)
			ext = ext[1:]
			if ext in extension:
				count = count + 1

				if path_verifier(dest_dir):
					shutil.move(item, dest_dir)
		
		print(count, '%ss found in %s'%(file_type, source_dir))
		
		if not path_verifier(dest_dir):
			print("dest_dir %s not found."%(dest_dir))
		else:
			print('Files moved successfully')
	else:
		if not file_type:
			print("No file type provided.")
		if not path_verifier(source_dir):
			print("Source_dir %s not found."%(source_dir))
		
		print("See fileOrganizer.py -h for help")	

fileOrganize(file_type=file_type, dest_dir=dest_path, source_dir=source_path)