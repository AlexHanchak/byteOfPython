import zipfile

with zipfile.ZipFile('spam.zip', 'w') as myzip:
    myzip.write('/media/alex/Data/60277051_310783819812128_4807593465808736050_n.jpg')

# https://docs.python.org/2/library/zipfile.html#zipfile-objects
# http://www.devshed.com/c/a/Python/Python-UnZipped/
# https://docs.python.org/3/library/zipfile.html