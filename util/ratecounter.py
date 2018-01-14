import time

class RateCounter:
  def __init__(self):
    self.reset()

  def reset(self):
    self.start = time.time()
    self.count = 0
    self.nbytes = 0

  def update(self,nbytes):
    self.count += 1
    self.nbytes += nbytes

  def report(self):
    return("{:.1f} msg/s, {:.1f} Mbits/s".format(
                                float(self.count)/(time.time()-self.start),
                                float(self.nbytes)*8e-6/(time.time()-self.start)
                              ))