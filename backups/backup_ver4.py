import os
import time

source = ['/media/alex/Data/books/AByteofPythonRussian-2.01.pdf', '/media/alex/Data/books/django.pdf']

target_dir = '/media/alex/Data/Backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('input comment --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('dir make successful', today)

zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('backup create successful in ', target)
else:
    print('create backup error')
