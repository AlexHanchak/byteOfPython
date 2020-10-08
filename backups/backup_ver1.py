import os
import time

source = ['/media/alex/Data/Blog-task.txt', '"/media/alex/Data/python Django"']

target_dir = '/media/alex/Data/Backup/'

target = target_dir + os.sep + time.strftime('%Y%m%d%%H%M%S') + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('success', target)
else:
    print('sorry')
