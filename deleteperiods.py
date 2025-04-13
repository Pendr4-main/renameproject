import os
import sys

def delete_per(folder_path):
    try:
        files = os.listdir(folder_path)
        
        # Iterate through the files
        for filename in files:
            # Create the full paths
            old_path = os.path.join(folder_path, filename)
            
            # Skip if it's a directory
            if os.path.isdir(old_path):
                continue
            
            # Split the filename into name and extension
            name_parts = filename.rsplit(".", 1)  # Split at the last period
            
            if len(name_parts) > 1:
                # Has extension
                name = name_parts[0]
                extension = name_parts[1]
                
                # Replace dots with spaces in the filename part only
                new_name = name.replace(".", " ")
                
                # Reconstruct the filename with its extension
                new_filename = f"{new_name}.{extension}"
            else:
                # No extension
                new_filename = filename.replace(".", " ")
            
            # Skip if no changes were made
            if new_filename == filename:
                continue
            
            # Create the new full path
            new_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: '{filename}' -> '{new_filename}'")
            except OSError as e:
                print(f"Error renaming '{filename}': {e}")
        
        print("File renaming complete.")
        
    except FileNotFoundError:
        print(f"Error: Directory '{folder_path}' not found")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to access '{folder_path}'")
        sys.exit(1)