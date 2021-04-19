import contextlib
import io


class stdio:
    def __init__(self, stdout_cls=io.StringIO, stderr_cls=io.StringIO):
        self.stdout = stdout_cls()
        self.stderr = stderr_cls()


@contextlib.contextmanager
def redirect_stdio(stdout_cls=io.StringIO, stderr_cls=io.StringIO):
    stdio_ins = stdio(stdout_cls, stderr_cls)
    try:
        with contextlib.redirect_stdout(stdio_ins.stdout):
            with contextlib.redirect_stderr(stdio_ins.stderr):
                yield stdio_ins
    finally:
        ...
