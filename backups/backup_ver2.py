import os
import time

src = ['/media/alex/Data/Blog-task.txt']

target_dir = '/media/alex/Data/Backup/'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print('dir create success ' + today)

target = today + os.sep + now + '.zip'

zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(src))

if os.system(zip_command) == 0:
    print('successful ', target)
else:
    print('error')
