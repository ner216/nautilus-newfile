#!/bin/bash

# Get the absolute path of the directory where the script is located
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)

# Make script terminate if a command fails
set -e

# Create the rpm folder structure at the root of the current user's home directory
printf "\nCreating RPM tree...\n"
rpmdev-setuptree

printf "\nCopying spec file...\n"
cp $SCRIPT_DIR/nautilus-extension-newfile.spec ~/rpmbuild/SPECS/

printf "\nCopying source files...\n"
cp $SCRIPT_DIR/../new-file-dialog.ui ~/rpmbuild/SOURCES/
cp $SCRIPT_DIR/../nautilus-newfile.py ~/rpmbuild/SOURCES/

printf "\nBuilding binary RPM...\n"
rpmbuild -bb ~/rpmbuild/SPECS/nautilus-extension-newfile.spec

printf "\nDone. RPM file is located at ~/rpmbuild/RPMS/noarch/\n"



