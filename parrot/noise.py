"""
Map noises (like pop) to actions so they can have contextually differing behavior
"""
# Copied ideas from community/core/noise :)
# I recorded pop/hiss sounds but only so the model could differentiate between sounds better (I think this makes sense). 
#  (and also why they are banished to the end of the patterns.json file)
#  The default talon pop/hiss is already perfect. 
#     Because: aegis 1:00PM may be hard to beat the default hiss, talon's noise recognizers are based on classic signal processing and not neural nets

# Had to comment out the line in parrot_integration.py:
#   pattern['throttle'][name] = 0
# For good shush/hiss detection.

from talon import Context, Module, actions, cron, noise

mod = Module()

@mod.action_class
class Actions:
    def noise_trigger_tut():
      """Tut noise - sometimes trigger when moving my head"""
      #actions.mouse_click(0)
      print ("real tut 1")
      print ("real tut 2")
      pass

    def noise_trigger_cluck():
      """Cluck noise -- also sometimes triggers when moving my head"""
      print ("real cluck")
      pass

    def noise_parrot_trigger_shush(start: bool):
      """Shush noise"""
      noise_trigger_shush_debounce(start)
      #print ("trigger: shush: ")
      pass

    def noise_parrot_trigger_hiss(start: bool):
      """Shush noise"""
      noise_trigger_hiss_debounce(start)
      #print ("trigger: shush: ")
      pass

    
    def noise_trigger_shush(active: bool):
      """Shush noise active"""
      print (f"* noise: shush: {active}")
      actions.skip()
      pass

    def noise_trigger_hiss(active: bool):
      """Shush noise active"""
      print (f"* noise: hiss: {active}")
      actions.skip()
      pass

    def noise_trigger_hiss_debug(active: bool):
      """Shush noise active"""
      print (f"* noise: hiss: {active}")
      actions.skip()
      pass


shush_cron, hiss_cron = None, None
hiss_end_cron = None # my personal hiss end seems a little less reliable then the default.
def noise_trigger_shush_debounce(active: bool):
    """Since the shush noise triggers while you're talking we need to debounce it"""
    global shush_cron
    if active:
        shush_cron = cron.after("100ms", lambda: actions.user.noise_trigger_shush(active))
    else:
        cron.cancel(shush_cron)
        actions.user.noise_trigger_shush(active)

def noise_trigger_hiss_debounce(active: bool):
    """Since the hiss noise triggers while you're talking we need to debounce it"""
    global hiss_cron, hiss_end_cron
    if active:
        cron.cancel(hiss_end_cron)
        hiss_cron = cron.after("100ms", lambda: actions.user.noise_trigger_hiss(active))
    else:
        cron.cancel(hiss_cron)
        hiss_end_cron = cron.after("50ms", lambda: actions.user.noise_trigger_hiss(active))
        #actions.user.noise_trigger_hiss(active)

# For public repo. I comment this out.      
noise.register("hiss", noise_trigger_hiss_debounce)

#An experiment
shush_end_cron = None
isShushing = False

def noise_trigger_shush_debounce_sami(active: bool):
    """Since the shush noise triggers while you're talking we need to debounce it"""
    global shush_cron, shush_end_cron, isShushing
    if active:
        cron.cancel(shush_end_cron)
        if (not isShushing):
          shush_cron = cron.after("100ms", lambda: actions.user.noise_trigger_shush(active))
          isShushing = True
        shush_end_cron = cron.after("250ms", lambda: noise_trigger_shush_end())
    else:
        pass
        #shush_end_cron = cron.after("200ms", lambda: actions.user.noise_trigger_shush(active))


def noise_trigger_shush_end():
  global shush_cron, isShushing
  cron.cancel(shush_cron)
  actions.user.noise_trigger_shush(False)
  isShushing = False


#noise.register("tut", lambda _: actions.user.noise_trigger_tut())
#noise.register("shush", noise_trigger_buzz_debounce)

"""
Shouldn't have been clucks?
	2024-02-18 14:29:09.602    IO predict cluck 96.20% pow=26.37 f0=1659.690 f1=741.222 f2=1508.300
	2024-02-18 14:30:13.661    IO predict cluck 99.22% pow=41.21 f0=1193.477 f1=890.696 f2=1385.504
	2024-02-18 14:30:27.732    IO predict cluck 98.90% pow=26.21 f0=927.510 f1=869.287 f2=1455.716
  2024-02-18 14:32:04.451    IO predict cluck 99.50% pow=45.36 f0=1361.266 f1=752.767 f2=1440.118

Good clucks
	2024-02-18 14:30:42.071    IO predict cluck 99.73% pow=62.38 f0=1062.053 f1=901.932 f2=1319.845
	2024-02-18 14:30:43.031    IO predict cluck 99.71% pow=41.54 f0=1360.277 f1=830.905 f2=1353.628
	2024-02-18 14:30:41.081    IO predict cluck 99.55% pow=35.68 f0=1094.130 f1=901.318 f2=1346.315
  2024-02-18 14:34:07.901    IO predict cluck 97.24% pow=31.62 f0=1028.533 f1=876.271 f2=1355.937
  2024-02-18 14:35:23.001    IO predict cluck 99.11% pow=84.38 f0=1029.494 f1=861.912 f2=2216.777
  """
