import threading
import time
import os

class DeadMansSwitch:
    def __init__(self, timeout=10):
         self.timeout = timeout
         self.timer = None
         self.is_running = False

    def _trigger_action(self):
        print("\n\n[!!!] STATUS: INACTIVE. Executing payload...")
        # Add your "failsafe" logic here (e.g., delete files, send email)
        os._exit(1) 

    def start_timer(self):
        if self.timer:
            self.timer.cancel()
        
        self.timer = threading.Timer(self.timeout, self._trigger_action)
        self.timer.start()
        self.is_running = True

    def reset(self):
        print(f"\n[+] Signal received. Resetting {self.timeout}s clock.")
        self.start_timer()

def main():
    switch = DeadMansSwitch(timeout=10)
    print("--- DEAD MAN'S SWITCH ACTIVE (10s) ---")
    print("Press 'Enter' to check in. Fail to check in, and the system triggers.")
    
    switch.start_timer()

    try:
        while True:
            input("") # Wait for user to hit Enter
            switch.reset()
    except KeyboardInterrupt:
        print("\nManual override detected. Shutting down.")

if __name__ == "__main__":
    main()
