import os
import json

KEYWORDS = {
    "LUpEyelid": 0,
    "LLowEyelid": 0,
    "RUpEyelid": 0,
    "RLowEyelid": 0,
    "RCornea": 0,
    "LCornea": 0,
}

def count_keywords(directory_path):
    keyword_counts = KEYWORDS.copy()

    LUpEyelid = 0
    LLowEyelid = 0
    LCornea = 0
    RUpEyelid = 0
    RLowEyelid = 0
    RCornea = 0
    
    # iterate over all files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".json"):
            filepath = os.path.join(directory_path, filename) # if the file ends with ".json", construct the full path to the file
            
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

            print(f"LUpEyelid: {LUpEyelid}, LLowEyelid: {LLowEyelid}, RUpEyelid: {RUpEyelid}, RLowEyelid: {RLowEyelid}, RCornea: {RCornea}, LCornea: {LCornea}\n")
            
            LUpEyelid = 0
            LLowEyelid = 0
            RUpEyelid = 0
            RLowEyelid = 0
            RCornea = 0
            LCornea = 0

    return keyword_counts

if __name__ == "__main__":
    directory_path = 'D:\\work\\Segmentation_code_Scripts4Zohair\\datasets\\Training_images_horse_eyes' # absolute path
    keyword_counts = count_keywords(directory_path)
    
    print("Number of Keywords Found:")
    for keyword, count in keyword_counts.items():
        print(f"{keyword}: {count}")
