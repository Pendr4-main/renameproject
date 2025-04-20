import os
import sys
import re

def find_year(folder_path):
    try:
        files = os.listdir(folder_path)
        
        # Iterate through the files
        for filename in files:
            # Pattern that finds years not already in parentheses
            pattern = r'(?<!\()\b(\d{4})\b(?!\))'  # Note the capturing group parentheses
            
            # Function to process each match
            def replace_year(match):
                year = int(match.group(1))
                if year >= 1920:
                    return f"({match.group(1)})"
                else:
                    return match.group(1)  # Return original if before 1920
            
            # Use the replace_year function with re.sub
            new_filename = re.sub(pattern, replace_year, filename)
            
            if new_filename != filename:
                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, new_filename)
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} → {new_filename}")
        
        return True
        
    except FileNotFoundError:
        print(f"Error: Directory '{folder_path}' not found")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to access '{folder_path}'")
        sys.exit(1)
