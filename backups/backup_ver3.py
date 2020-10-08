import os
import time

src = ['/media/alex/Data/Blog-task.txt']

target_dir = '/media/alex/Data/Backup/'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('input comment --> ')
if len(comment) == 0:
    target = today + os.sep + now + './zip'
else:
    target = today + os.sep + now + '_' +\
             comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('dir create success ' + today)

zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(src))

if os.system(zip_command) == 0:
    print('successful ', target)
else:
    print('error')
