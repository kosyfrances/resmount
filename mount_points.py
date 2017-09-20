import json
from pathlib import Path


def get_mount_points():
    mount_file = '/proc/self/mountinfo'
    mount_points_dict = {
        'mount_points': []
    }

    if Path(mount_file).is_file():
        with open(mount_file, 'r') as f:
            for line in f:
                line = line.split()
                if len(line) > 4:
                    mount_points_dict['mount_points'].append(line[4])
    else:
        print(
            '{} does not exist.\
            Please ensure the file exists and try again'.format(mount_file)
        )
    return json.dumps(mount_points_dict)
