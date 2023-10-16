import os

def get_folder_names_in_current_dir(cur_dir):
  return [dir.name for dir in os.scandir(current_dir) if dir.is_dir() and not dir.name.startswith(".")]


def rename_folders(folders):
  for i, name in enumerate(folders, 1):
    
    prefix = name.split("-")[0]

    if int(prefix) != i:
      old_name = current_dir + "/" + name
      new_name = f"{current_dir}/0{i}{name[2:]}"
      
      os.replace(old_name, new_name)


# Get current dir name
current_dir = os.getcwd()

# Get folder names
folders = get_folder_names_in_current_dir(current_dir)

# Rename folder names
rename_folders(folders)

  