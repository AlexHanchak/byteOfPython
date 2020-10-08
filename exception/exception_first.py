try:
    text = input('some text -->')
except EOFError:
    print('why did you do EOF')
except KeyboardInterrupt:
    print('you interrupt operation')
else:
    print('you input {0}'.format(text))
