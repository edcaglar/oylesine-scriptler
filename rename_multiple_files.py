"""
Multiple file name changer

Usage:
python rename_multiple_files.py --path /your/path/to/folder --name filePrefix
"""
import os

def renameFiles(path, name):
    count = 1
    for filename in os.listdir(path):
        # Construct old file name
        extension  = os.path.splitext(filename)[1] # get the extension of file
        source = path + "/" + filename

        destination = path + "/" + name + "_" + str(count) + extension

        # Renaming the file
        os.rename(source, destination)
        count += 1



if __name__ == '__main__':
    import argparse
    # Parse command line arguments

    parser = argparse.ArgumentParser(
        description='Multiple Filename Changer'
    )

    parser.add_argument('--path', required=True)
    parser.add_argument('--name', required=True)
    #parser.add_argument('--extension', required=True)

    args = parser.parse_args()
    res = renameFiles(args.path, args.name)
    print(res)
