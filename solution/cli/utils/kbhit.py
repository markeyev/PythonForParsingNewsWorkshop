"""
A Python class implementing KBHIT, the standard keyboard-interrupt poller.
Works transparently on Windows and Posix (Linux, Mac OS X).  Doesn't work
with IDLE.
"""

import os

# Windows
if os.name == 'nt':
    import msvcrt

# Posix (Linux, OS X)
else:
    import sys
    import termios
    import atexit
    from select import select


class KBHit:

    def __init__(self):
        """Creates a KBHit object that you can call to do various keyboard
        things.
        """

        if os.name == 'nt':
            pass

        else:

            # Save the terminal settings
            self.fd = sys.stdin.fileno()
            self.new_term = termios.tcgetattr(self.fd)
            self.old_term = termios.tcgetattr(self.fd)

            # New terminal setting unbuffered
            self.new_term[3] = (self.new_term[3] & ~termios.ICANON &
                                ~termios.ECHO)
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.new_term)

            # Support normal-terminal reset at exit
            atexit.register(self.set_normal_term)

    def set_normal_term(self):
        """ Resets to normal terminal.  On Windows this is a no-op.
        """

        if os.name == 'nt':
            pass

        else:
            termios.tcsetattr(self.fd, termios.TCSAFLUSH, self.old_term)

    @staticmethod
    def get_char():
        """ Returns a keyboard character after kb_hit() has been called.
            Should not be called in the same program as get_arrow().
        """

        if os.name == 'nt':
            return msvcrt.get_char().decode('utf-8')

        else:
            return sys.stdin.read(1)

    @staticmethod
    def hit():
        """ Returns True if keyboard character was hit, False otherwise.
        """
        if os.name == 'nt':
            return msvcrt.hit()

        else:
            dr, dw, de = select([sys.stdin], [], [], 0)
            return dr != []


# Test    
if __name__ == "__main__":

    kb = KBHit()

    print('Hit any key, or ESC to exit')

    while True:

        if kb.hit():
            c = kb.get_char()
            if ord(c) == 27:  # ESC
                break
            print(c)

    kb.set_normal_term()
