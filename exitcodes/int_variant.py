# See enum variant for a description of each constant
# glibc source:
# https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=misc/sysexits.h;hb=refs/heads/master

# musl libc source:
# https://git.musl-libc.org/cgit/musl/tree/include/sysexits.h

try:
    from os import EX_CANTCREAT as EX_CANTCREAT
    from os import EX_CONFIG as EX_CONFIG
    from os import EX_DATAERR as EX_DATAERR
    from os import EX_IOERR as EX_IOERR
    from os import EX_NOHOST as EX_NOHOST
    from os import EX_NOINPUT as EX_NOINPUT
    from os import EX_NOPERM as EX_NOPERM
    from os import EX_NOTFOUND as EX_NOTFOUND
    from os import EX_NOUSER as EX_NOUSER
    from os import EX_OK as EX_OK
    from os import EX_OSERR as EX_OSERR
    from os import EX_OSFILE as EX_OSFILE
    from os import EX_PROTOCOL as EX_PROTOCOL
    from os import EX_SOFTWARE as EX_SOFTWARE
    from os import EX_TEMPFAIL as EX_TEMPFAIL
    from os import EX_UNAVAILABLE as EX_UNAVAILABLE
    from os import EX_USAGE as EX_USAGE
except ImportError:
    EX_OK = 0
    EX_USAGE = 64
    EX_DATAERR = 65
    EX_NOINPUT = 66
    EX_NOUSER = 67
    EX_NOHOST = 68
    EX_UNAVAILABLE = 69
    EX_SOFTWARE = 70
    EX_OSERR = 71
    EX_OSFILE = 72
    EX_CANTCREAT = 73
    EX_IOERR = 74
    EX_TEMPFAIL = 75
    EX_PROTOCOL = 76
    EX_NOPERM = 77
    EX_CONFIG = 78
    EX_NOTFOUND = 79
