import subprocess


def yuv_histogram():
    subprocess.call(['ffplay', 'output.mp4', '-vf', 'split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay'])

