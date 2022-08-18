from enum import IntEnum

from exitcodes.int_variant import (
    EX_CANTCREAT,
    EX_CONFIG,
    EX_DATAERR,
    EX_IOERR,
    EX_NOHOST,
    EX_NOINPUT,
    EX_NOPERM,
    EX_NOTFOUND,
    EX_NOUSER,
    EX_OK,
    EX_OSERR,
    EX_OSFILE,
    EX_PROTOCOL,
    EX_SOFTWARE,
    EX_TEMPFAIL,
    EX_UNAVAILABLE,
    EX_USAGE,
)


class ExitCode(IntEnum):
    """The following exit codes are defined and can be used with SystemExit, although
    they are not required. These are typically used for system programs written in
    Python, such as a mail server's external command delivery program.

    glibc source:
    https://sourceware.org/git/?p=glibc.git;a=blob_plain;f=misc/sysexits.h;hb=refs/heads/master

    musl libc source:
    https://git.musl-libc.org/cgit/musl/tree/include/sysexits.h

    * EX_OK: Exit code that means no error occurred.
    * EX_USAGE: Exit code that means the command was used incorrectly, such as when the
        wrong number of arguments are given.
    * EX_DATAERR: Exit code that means the input data was incorrect.
    * EX_NOINPUT: Exit code that means an input file did not exist or was not readable.
    * EX_NOUSER: Exit code that means a specified user did not exist.
    * EX_NOHOST: Exit code that means a specified host did not exist.
    * EX_UNAVAILABLE: Exit code that means that a required service is unavailable.
    * EX_SOFTWARE: Exit code that means an internal software error was detected.
    * EX_OSERR: Exit code that means an operating system error was detected, such as
        the inability to fork or create a pipe.
    * EX_OSFILE: Exit code that means some system file did not exist, could not be
        opened, or had some other kind of error.
    * EX_CANTCREAT: Exit code that means a user specified output file could not be
        created.
    * EX_IOERR: Exit code that means that an error occurred while doing I/O on some
        file.
    * EX_TEMPFAIL: Exit code that means a temporary failure occurred. This indicates
        something that may not really be an error, such as a network connection that
        couldn't be made during a retryable operation.
    * EX_PROTOCOL: Exit code that means that a protocol exchange was illegal, invalid,
        or not understood.
    * EX_NOPERM: Exit code that means that there were insufficient permissions to
        perform the operation (but not intended for file system problems).
    * EX_CONFIG: Exit code that means that some kind of configuration error occurred.
    * EX_NOTFOUND: Exit code that means something like "an entry was not found".
    """

    EX_OK = EX_OK
    EX_USAGE = EX_USAGE
    EX_DATAERR = EX_DATAERR
    EX_NOINPUT = EX_NOINPUT
    EX_NOUSER = EX_NOUSER
    EX_NOHOST = EX_NOHOST
    EX_UNAVAILABLE = EX_UNAVAILABLE
    EX_SOFTWARE = EX_SOFTWARE
    EX_OSERR = EX_OSERR
    EX_OSFILE = EX_OSFILE
    EX_CANTCREAT = EX_CANTCREAT
    EX_IOERR = EX_IOERR
    EX_TEMPFAIL = EX_TEMPFAIL
    EX_PROTOCOL = EX_PROTOCOL
    EX_NOPERM = EX_NOPERM
    EX_CONFIG = EX_CONFIG
    EX_NOTFOUND = EX_NOTFOUND
