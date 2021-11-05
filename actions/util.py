import pathlib
import subprocess
import tempfile


QUOTAS = {
    # production dirs
    '/mnt/homework/homework': '/sbin/zfs set userquota@"{}"=15G homework/homework',
    '/mnt/homework/public_html': '/sbin/zfs set userquota@"{}"=3G homework/public_html',
    '/mnt/homework/private_cvmfs': '/sbin/zfs set userquota@"{}"=10G homework/private_cvmfs',
    '/mnt/lfs7/users': '/usr/bin/lfs setquota -g {} --block-softlimit 2000000 --block-hardlimit 2250000 /mnt/lfs7',
    # testing dirs
    '/mnt/homework/homework_test': '/sbin/zfs set userquota@"{}"=15G homework/homework_test',
    '/mnt/lfs7/users_test': '/usr/bin/lfs setquota -g {} --block-softlimit 2000000 --block-hardlimit 2250000 /mnt/lfs7',
}

ssh_opts = ['-o', 'UserKnownHostsFile=/dev/null', '-o', 'StrictHostKeyChecking=no']

def ssh(host, *args):
    """Run command on remote machine via ssh."""
    cmd = ['ssh'] + ssh_opts + [f'{host}'] + list(args)
    subprocess.check_call(cmd, stderr=subprocess.DEVNULL)

def scp_and_run(host, script_data, script_name='create.py'):
    """Transfer a script to a remote machine, run it, then delete it."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        filename = pathlib.Path(tmpdirname) / script_name
        with open(filename, 'w') as f:
            f.write(script_data)
        cmd = ['scp'] + ssh_opts + [filename, f'{host}:/tmp/{script_name}']
        subprocess.check_call(cmd, stderr=subprocess.DEVNULL)

    try:
        ssh(host, 'python', f'/tmp/{script_name}')
    finally:
        ssh(host, 'rm', f'/tmp/{script_name}')

def scp_and_run_sudo(host, script_data, script_name='create.py'):
    """Transfer a script to a remote machine, run it as root, then delete it."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        filename = pathlib.Path(tmpdirname) / script_name
        with open(filename, 'w') as f:
            f.write(script_data)
        cmd = ['scp'] + ssh_opts + [filename, f'{host}:/tmp/{script_name}']
        subprocess.check_call(cmd, stderr=subprocess.DEVNULL)

    try:
        ssh(host, 'sudo', 'python', f'/tmp/{script_name}')
    finally:
        ssh(host, 'rm', f'/tmp/{script_name}')
