#!/usr/bin/env python
# eggd_archive_system 1.0.0

import os
import subprocess

import dxpy
from dxpy.exceptions import DXJobFailureError
import dxpy.app_builder import upload_applet

@dxpy.entry_point('main')
def main(file_to_archive=None, file_to_unarchive=None):

    # The following line(s) initialize your data object inputs on the platform
    # into dxpy.DXDataObject instances that you can start using immediately.

    if file_to_archive is not None:
        file_to_archive = [dxpy.DXFile(item) for item in file_to_archive]
    if file_to_unarchive is not None:
        file_to_unarchive = [dxpy.DXFile(item) for item in file_to_unarchive]

    # The following line(s) download your file inputs to the local file system
    # using variable names for the filenames.

    if file_to_archive is not None:
        for i, f in enumerate(file_to_archive):
            dxpy.download_dxfile(f.get_id(), "file_to_archive-" + str(i))

    if file_to_unarchive is not None:
        for i, f in enumerate(file_to_unarchive):
            dxpy.download_dxfile(f.get_id(), "file_to_unarchive-" + str(i))

    # Check if project and files have the appropriate archive tag if not add it

    # Add archiving tag to projects/files with no archive_ready tag
    dxpy.api.project_add_tags(object_id, input_params={"tags:archive_ready"}, always_retry=True)

    # Add unarchiving tag to projects files with not unarchive specific tag
    dxpy.api.project_add_tags(object_id, input_params={"tags:unarchive"}, always_retry=True)

    # Get project and file IDs for inputs to archive
    file_to_archive = self.get_proj_id()
    get_proj_id()
    get_id()
    # Get project and file IDs for inputs to unarchive

    # Call archiving
    dxpy.api.project_archive(archived_ready_files, input_params={"allCopies:true"}, always_retry=True)
    # Call unarchiving
    dxpy.api.project_unarchive(unarchive_ready_files, input_params={}, always_retry=True)

    # Outputs will be a .txt/.log file containing the summary of the archiving/unarchiving command (includes count of files that have been archived and the project/file-ID)
    # Store output form archiving-unarchiving command in .txt and upload as output
    output = {}
    output["archived_log"] = [dxpy.dxlink(item) for item in archived_log]
    output["unarchived_log"] = [dxpy.dxlink(item) for item in unarchived_log]

    return output

dxpy.run()
