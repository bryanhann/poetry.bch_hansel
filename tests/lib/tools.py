import os
import subprocess

def shell_exec(args,**b):
    x = subprocess.run(args,capture_output=True)
    return Result( stdout=x.stdout.decode(), stderr=x.stderr.decode(), retval=x.returncode )

class Result:
    def __init__(self, stdout='', stderr='', retval=0):
        self.stdout=stdout
        self.stderr=stderr
        self.retval=retval

class RunCase:
    def __init__(self, cmd="", args=[], cd='.', exp=Result(), out='', err=''):
        self.cmd = cmd
        self.args = args
        self.cd = cd
        self.exp = exp

    def run(self):
        try:
            self.got
        except AttributeError:
            here=os.getcwd()
            os.chdir( self.cd )
            self.got = shell_exec([self.cmd] + self.args)
            os.chdir(here)
        return self

    def assert_pass(self):
        assert self.exp.stdout == self.got.stdout
        assert self.exp.stderr == self.got.stderr
        assert self.exp.retval == self.got.retval
