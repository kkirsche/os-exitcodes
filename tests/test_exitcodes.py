from os_exitcodes import (
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
    ExitCode,
    __version__,
)


def test_version() -> None:
    assert __version__ == "1.0.0"


def test_EX_NOTFOUND() -> None:
    try:
        from os import EX_NOTFOUND as OS_EXIT_CODE

        assert EX_NOTFOUND == OS_EXIT_CODE
    except ImportError:
        assert EX_NOTFOUND == 79
    assert int(ExitCode.EX_NOTFOUND) == EX_NOTFOUND


def test_EX_CANTCREAT() -> None:
    try:
        from os import EX_CANTCREAT as OS_EXIT_CODE

        assert EX_CANTCREAT == OS_EXIT_CODE
    except ImportError:
        assert EX_CANTCREAT == 73
    assert int(ExitCode.EX_CANTCREAT) == EX_CANTCREAT


def test_EX_CONFIG() -> None:
    try:
        from os import EX_CONFIG as OS_EXIT_CODE

        assert EX_CONFIG == OS_EXIT_CODE
    except ImportError:
        assert EX_CONFIG == 78
    assert int(ExitCode.EX_CONFIG) == EX_CONFIG


def test_EX_DATAERR() -> None:
    try:
        from os import EX_DATAERR as OS_EXIT_CODE

        assert EX_DATAERR == OS_EXIT_CODE
    except ImportError:
        assert EX_DATAERR == 65
    assert int(ExitCode.EX_DATAERR) == EX_DATAERR


def test_EX_IOERR() -> None:
    try:
        from os import EX_IOERR as OS_EXIT_CODE

        assert EX_IOERR == OS_EXIT_CODE
    except ImportError:
        assert EX_IOERR == 74
    assert int(ExitCode.EX_IOERR) == EX_IOERR


def test_EX_NOHOST() -> None:
    try:
        from os import EX_NOHOST as OS_EXIT_CODE

        assert EX_NOHOST == OS_EXIT_CODE
    except ImportError:
        assert EX_NOHOST == 68
    assert int(ExitCode.EX_NOHOST) == EX_NOHOST


def test_EX_NOINPUT() -> None:
    try:
        from os import EX_NOINPUT as OS_EXIT_CODE

        assert EX_NOINPUT == OS_EXIT_CODE
    except ImportError:
        assert EX_NOINPUT == 66
    assert int(ExitCode.EX_NOINPUT) == EX_NOINPUT


def test_EX_NOPERM() -> None:
    try:
        from os import EX_NOPERM as OS_EXIT_CODE

        assert EX_NOPERM == OS_EXIT_CODE
    except ImportError:
        assert EX_NOPERM == 77
    assert int(ExitCode.EX_NOPERM) == EX_NOPERM


def test_EX_NOUSER() -> None:
    try:
        from os import EX_NOUSER as OS_EXIT_CODE

        assert EX_NOUSER == OS_EXIT_CODE
    except ImportError:
        assert EX_NOUSER == 67
    assert int(ExitCode.EX_NOUSER) == EX_NOUSER


def test_EX_OK() -> None:
    try:
        from os import EX_OK as OS_EXIT_CODE

        assert EX_OK == OS_EXIT_CODE
    except ImportError:
        assert EX_OK == 0
    assert int(ExitCode.EX_OK) == EX_OK


def test_EX_OSERR() -> None:
    try:
        from os import EX_OSERR as OS_EXIT_CODE

        assert EX_OSERR == OS_EXIT_CODE
    except ImportError:
        assert EX_OSERR == 71
    assert int(ExitCode.EX_OSERR) == EX_OSERR


def test_EX_OSFILE() -> None:
    try:
        from os import EX_OSFILE as OS_EXIT_CODE

        assert EX_OSFILE == OS_EXIT_CODE
    except ImportError:
        assert EX_OSFILE == 72
    assert int(ExitCode.EX_OSFILE) == EX_OSFILE


def test_EX_PROTOCOL() -> None:
    try:
        from os import EX_PROTOCOL as OS_EXIT_CODE

        assert EX_PROTOCOL == OS_EXIT_CODE
    except ImportError:
        assert EX_PROTOCOL == 76
    assert int(ExitCode.EX_PROTOCOL) == EX_PROTOCOL


def test_EX_SOFTWARE() -> None:
    try:
        from os import EX_SOFTWARE as OS_EXIT_CODE

        assert EX_SOFTWARE == OS_EXIT_CODE
    except ImportError:
        assert EX_SOFTWARE == 70
    assert int(ExitCode.EX_SOFTWARE) == EX_SOFTWARE


def test_EX_TEMPFAIL() -> None:
    try:
        from os import EX_TEMPFAIL as OS_EXIT_CODE

        assert EX_TEMPFAIL == OS_EXIT_CODE
    except ImportError:
        assert EX_TEMPFAIL == 75
    assert int(ExitCode.EX_TEMPFAIL) == EX_TEMPFAIL


def test_EX_UNAVAILABLE() -> None:
    try:
        from os import EX_UNAVAILABLE as OS_EXIT_CODE

        assert EX_UNAVAILABLE == OS_EXIT_CODE
    except ImportError:
        assert EX_UNAVAILABLE == 69
    assert int(ExitCode.EX_UNAVAILABLE) == EX_UNAVAILABLE


def test_EX_USAGE() -> None:
    try:
        from os import EX_USAGE as OS_EXIT_CODE

        assert EX_USAGE == OS_EXIT_CODE
    except ImportError:
        assert EX_USAGE == 64
    assert int(ExitCode.EX_USAGE) == EX_USAGE
