import os

# get the directory that contains this script
gmhi2_script_install_folder = os.path.dirname(os.path.abspath(__file__))
# get the default database folder
DEFAULT_DB_FOLDER = os.path.join(gmhi2_script_install_folder, "gmhi2_databases")