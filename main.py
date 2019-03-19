"""
GNU LESSER GENERAL PUBLIC LICENSE
                       Version 2.1, February 1999

 Copyright (C) 1991, 1999 Free Software Foundation, Inc.
 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

[This is the first released version of the Lesser GPL.  It also counts
 as the successor of the GNU Library Public License, version 2, hence
 the version number 2.1.]
 
 https://github.com/systemd/python-systemd/blob/master/LICENSE.txt
"""
from systemd import journal
from elecXjournal import manager

def main():
    j = manager.service(journal=journal)
    # j.testWatch()
    j.watch()

if __name__ == '__main__':
    main()
