#!c:\users\alice\documents\2019-3-level-labs\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Flask==1.1.2.dev0','console_scripts','flask'
__requires__ = 'Flask==1.1.2.dev0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Flask==1.1.2.dev0', 'console_scripts', 'flask')()
    )
