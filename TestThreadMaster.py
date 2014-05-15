#!/usr/bin/python

from TestThreadSlave import CommandThread
import sys

class MainApplication:
    """ a class for the main application """
    def __init__(self):
        """ constructor defines a thread variable, but doesnt construct the thread, 
        because threads can only be started once. """
        print "Creating CommandThread"
        self.commandThread = None

    def doit(self):
        """ set the command and start the thread. """
        self.commandThread = CommandThread()
        #self.commandThread.setCommand("echo 1; sleep 1; echo 2; sleep 2; echo 3")
        #self.commandThread.setCommand("play /usr/share/sounds/gnome/default/alerts/bark.ogg")
        self.commandThread.setCommand("ssh cubieboard2.local ls /tmp; echo \"ZACKBUMM\"; ssh -v cubieboard2.local ls /tmp")        
        print "Starting CommandThread"
        self.commandThread.start()
    
    def output(self):
        """ read the output and print it on sync. """
        while self.commandThread and self.commandThread.isRunning():
            lines = self.commandThread.dumpOutputLines()
            for line in lines:
                sys.stdout.write("%d>%s" % (len(lines), line))
        
if __name__ == '__main__':
    app = MainApplication()
    # no thread => do nothing
    app.output()
    print "First Run"
    app.doit()
    app.output()
    print "Second Run"
    app.doit()
    app.output()
    print "Main Application Ends"
