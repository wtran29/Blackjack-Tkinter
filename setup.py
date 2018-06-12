from distutils.core import setup
import py2exe, sys, os


sys.argv.append('py2exe')

# image_files = []
# for files in os.listdir('C:/users/wtran/desktop/projects/python3/blackjack/cards/'):
#     f1 = 'C:/users/wtran/desktop/projects/python3/blackjack/cards/' + files
#     if os.path.isfile(f1):
#         f2 = 'cards', [f1]
#         image_files.append(f2)

setup(
    options={'py2exe': {
        'bundle_files': 1,
        'compressed': True
    }},
    windows=[{'script': "blackjack.py"}],
    zipfile=None,
)
