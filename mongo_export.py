#!/usr/bin/env python

import sys, subprocess, os, time, math
from datetime import date, timedelta
from config import logdir, MAX_PROCESSES

def wait_processes(children):
    for p in children:
        if p.wait() != 0:
            print time.strftime("%Y-%m-%d %H:%M:%S, "),
            print "Process have error", children[p]
        else:
            print time.strftime("%Y-%m-%d %H:%M:%S, "),
            print "Process done", children[p]
    sys.stdout.flush()

def run(children):
    rc = []
    while True:
        while len(children) > 0 and len(rc) < MAX_PROCESSES:
            prog, fout, info = children.pop()
            p = subprocess.Popen(prog.split(), stdout=fout)
            rc.append((p, info, time.time()))

        if len(rc) == 0:
            print time.strftime("%Y-%m-%d %H:%M:%S, "),
            print "all done"
            break

        for i in range(len(rc)):
            p, info, t = rc[i]
            if p.poll() == None: continue
            break
        if p.poll() == None:
            time.sleep(5)
            continue

        if p.poll() != 0:
            print time.strftime("%Y-%m-%d %H:%M:%S, "),
            print "Process have error", p.poll(), info
        else:
            print time.strftime("%Y-%m-%d %H:%M:%S, "),
            print "Process done", info, "cost", int(time.time()-t)

        rc.pop(i)
#print "Current Process Count", len(rc)


if __name__ == "__main__":

    d1 = date(2013,11,29)
    d2 = date(2014,2,5)
    # this will give you a list containing all of the dates
    dates = [d1 + timedelta(days=x) for x in range((d2-d1).days + 1)]
    children = []
    for day in dates:
#        prog = "logsave /work2/logs/day%s.log python export_day.py %s"%(str(day),str(day))
        prog = "python export_day.py %s"%str(day)
        print prog
        fout = open(os.path.join(logdir,"day"+str(day)), 'w')
        children.append((prog, fout, "export day"+str(day) ))
    run(children)