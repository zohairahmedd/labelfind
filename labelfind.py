import os
import json
import argparse
import csv

header = 0

KEYWORDS = {
    "LUpEyelid": 0,
    "LLowEyelid": 0,
    "RUpEyelid": 0,
    "RLowEyelid": 0,
    "RCornea": 0,
    "LCornea": 0,
}

def main():
    """
    take command line arguments input for the paths of both the location of the file(s) and name of csv file

    arguments:
        none
    """
    parser = argparse.ArgumentParser(description='processing some video.') # necessary for implementing command-line
    parser.add_argument('--input_directory', '-id', type=str, help='path to json files') # adds argument input_directory to the parser
    parser.add_argument('--csv_file', '-cf', type=str, help='name of csv file') # adds argument csv_file

    args = parser.parse_args() # allows us to use the arguments in the parser (args.argument_name)

    count_keywords(args.input_directory, args.csv_file) 

def count_keywords(input_directory, csv_file):
    """
    counts the occurrence of keywords within json file(s) located in the specified directory

    parameters:
    - input_directory (str): path to the directory containing the json file(s)
    - csv_file (str): name of csv file
    """

    global header

    keyword_counts = KEYWORDS.copy()

    LUpEyelid = 0
    LLowEyelid = 0
    LCornea = 0
    RUpEyelid = 0
    RLowEyelid = 0
    RCornea = 0
    
    # iterate over all files in the directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".json"):
            filepath = os.path.join(input_directory, filename) # if the file ends with ".json", construct the full path to the file
            
            # open and read the json file
            with open(filepath, 'r') as file: # open in reading mode

                data = json.load(file) # read the content
                
                text_data = str(data) # convert content into string data

                print(f"{filename}")
                
                # count occurrences of keywords in the file
                for keyword, count in keyword_counts.items():
                    keyword_count = text_data.count(keyword)
                    keyword_counts[keyword] += keyword_count
                    if keyword == 'LUpEyelid':
                        LUpEyelid += keyword_count
                    if keyword == 'LLowEyelid':
                        LLowEyelid += keyword_count
                    if keyword == 'RUpEyelid':
                        RUpEyelid += keyword_count
                    if keyword == 'RLowEyelid':
                        RLowEyelid += keyword_count
                    if keyword == 'RCornea':
                        RCornea += keyword_count
                    if keyword == 'LCornea':
                        LCornea += keyword_count

                # data for CSV file
                data = {
                    "Filename: ": filename,
                    " RCornea: ": RCornea,
                    " LCornea: ": LCornea,
                    " RUpEyelid: ": RUpEyelid,
                    " LUpEyelid: ": LUpEyelid,
                    " RLowEyelid: ": RLowEyelid,
                    " LLowEyelid: ": LLowEyelid
                }

                csv_name = csv_file

                # write data to CSV file
                if header == 0:
                    with open(csv_name, mode="a", newline='') as file:
                        file.write("Filename, RCornea, LCornea, RUpEyelid, LUpEyelid, RLowEyelid, LLowEyelid\n")
                        header += 1
                        file.close()
                
                with open(csv_name, mode='a', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=list(data.keys()))
                    writer.writerow(data)
                    file.close()

            print(f"LUpEyelid: {LUpEyelid}, LLowEyelid: {LLowEyelid}, RUpEyelid: {RUpEyelid}, RLowEyelid: {RLowEyelid}, RCornea: {RCornea}, LCornea: {LCornea}\n")
            
            LUpEyelid = 0
            LLowEyelid = 0
            RUpEyelid = 0
            RLowEyelid = 0
            RCornea = 0
            LCornea = 0

    print("Number of Keywords Found:")
    for keyword, count in keyword_counts.items():
        print(f"{keyword}: {count}")
    
if __name__ == "__main__":
    main()
