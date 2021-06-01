import subprocess

class GenericBackend():
    cmd = []

    def get_process_list(self):
        if self.cmd:
            return subprocess.check_output(self.cmd)
        else:
            raise NOtImplemented

class WindowsBackend(GenericBackend):
    cmd = ['tasklist', '/nh', '/fo', 'CSV']
class MacBsdBackend(GenericBackend):
    cmd = ['ps', '-e', '-o', "comm = ''", '-c']
class LinuxBackend(GenericBackend):
    cmd = ['ps', '-e', '--format', 'comm', '--no-heading']

def get_backend(os_name):
    backends = {'Windows': WindowsBackend, 'Darwin': MacBsdBackend, 'freebsd7': MacBsdBackend, 'Linux': LinuxBackend}

    try:
        return backends[os_name]
    except KeyError:
        raise NOtImplemented('No backend for OS')

get_backend()
