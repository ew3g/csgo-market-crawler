import time 

class Timer():
    @staticmethod
    def pause(seconds):
        init_time = time.time()
        while time.time() < init_time + seconds: pass