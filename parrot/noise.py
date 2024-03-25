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
    def noise_trigger_pop():
        """
        Called when the user makes a 'pop' noise. Listen to
        https://noise.talonvoice.com/static/previews/pop.mp3 for an
        example.
        """


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


    # --- Not real functions you're expected to override, handle more accurate recognition.
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

    # Sometimes background noises mess with my own pop recognition.
    def noise_trigger_talon_pop():
      """The base talon pop"""

    # Because hiss is used by the community/mouse to scroll, and I wanted to test my own hiss recording, this function exists.
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
noise.register("pop", lambda _: actions.user.noise_trigger_talon_pop())

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


""" shoulda popped

2024-03-04 17:58:44.383    IO predict tut 33.41% pow=45.24 f0=31.660 f1=40.522 f2=1263.973
2024-03-04 17:58:44.394    IO predict pop 98.37% pow=42.93 f0=20.427 f1=317.748 f2=1031.431
2024-03-04 17:58:44.413    IO predict pop 99.37% pow=46.61 f0=28.186 f1=195.045 f2=991.231
2024-03-04 17:58:44.424    IO predict pop 96.89% pow=33.42 f0=32.983 f1=49.911 f2=1086.135
2024-03-04 17:58:44.443    IO predict pop 38.47% pow=41.85 f0=24.284 f1=31.597 f2=1110.201
2024-03-04 17:58:44.453    IO predict tut 42.96% pow=62.99 f0=21.108 f1=32.044 f2=1099.249
2024-03-04 17:58:44.474    IO predict tut 43.24% pow=65.15 f0=14.682 f1=38.000 f2=1171.303
2024-03-04 17:58:44.483    IO predict silence 28.65% pow=60.76 f0=64.780 f1=50.472 f2=1184.140
2024-03-04 17:58:44.504    IO predict silence 56.54% pow=59.31 f0=28.689 f1=40.182 f2=1116.603
2024-03-04 17:58:44.513    IO predict tut 48.08% pow=70.67 f0=57.931 f1=49.095 f2=1160.429
2024-03-04 17:58:44.533    IO predict silence 31.53% pow=89.91 f0=32.298 f1=44.688 f2=1130.598
2024-03-04 17:58:44.543    IO predict silence 46.58% pow=79.36 f0=35.078 f1=57.950 f2=1199.555
2024-03-04 17:58:44.562    IO predict silence 36.59% pow=59.15 f0=29.667 f1=37.449 f2=1234.852
2024-03-04 17:58:44.573    IO predict tut 35.26% pow=68.70 f0=27.455 f1=31.419 f2=1326.024
2024-03-04 17:58:44.592    IO predict silence 38.93% pow=63.37 f0=34.882 f1=49.244 f2=1137.494
2024-03-04 17:58:44.603    IO predict silence 66.36% pow=32.77 f0=30.532 f1=47.797 f2=1189.264
2024-03-04 17:58:44.623    IO predict silence 47.20% pow=23.10 f0=27.524 f1=35.844 f2=1208.419
2024-03-04 17:58:44.637    IO predict tut 69.05% pow=38.82 f0=38.626 f1=44.364 f2=1206.331
2024-03-04 17:58:44.656    IO predict tut 68.62% pow=36.89 f0=24.451 f1=27.275 f2=1216.978
2024-03-04 17:58:44.665    IO predict tut 48.13% pow=25.90 f0=18.760 f1=26.633 f2=1232.787
2024-03-04 17:58:44.689    IO predict tut 47.02% pow=38.89 f0=35.607 f1=49.499 f2=1214.730
2024-03-04 17:58:44.696    IO predict tut 59.75% pow=36.30 f0=35.291 f1=44.176 f2=1138.052
2024-03-04 17:58:44.713    IO predict silence 28.22% pow=14.87 f0=23.101 f1=36.798 f2=1058.550
2024-03-04 17:58:44.722    IO predict tut 56.48% pow=39.00 f0=26.353 f1=29.454 f2=1151.603
2024-03-04 17:58:44.744    IO predict tut 75.64% pow=40.70 f0=19.703 f1=23.149 f2=1212.576
2024-03-04 17:58:44.754    IO predict tut 58.97% pow=21.98 f0=19.970 f1=22.272 f2=1145.088
2024-03-04 17:58:44.774    IO predict tut 82.68% pow=17.77 f0=13.496 f1=18.140 f2=1237.051
2024-03-04 17:58:44.783    IO predict cluck 50.25% pow=8.93 f0=57.412 f1=35.614 f2=1127.031
2024-03-04 17:58:44.803    IO predict cluck 36.39% pow=6.54 f0=36.053 f1=65.392 f2=1096.925
2024-03-04 17:58:44.813    IO predict tut 53.44% pow=8.31 f0=24.453 f1=48.286 f2=1143.586
2024-03-04 17:58:44.832    IO predict tut 57.04% pow=8.24 f0=25.532 f1=40.900 f2=1120.923
2024-03-04 17:58:44.843    IO predict cluck 34.87% pow=6.62 f0=23.217 f1=33.922 f2=1149.907
2024-03-04 17:58:44.862    IO predict tut 37.45% pow=14.06 f0=39.177 f1=54.434 f2=1162.322
2024-03-04 17:58:44.874    IO predict tut 59.33% pow=17.24 f0=35.776 f1=43.867 f2=1184.357
2024-03-04 17:58:44.892    IO predict tut 71.56% pow=17.96 f0=46.974 f1=54.051 f2=1193.020
2024-03-04 17:58:44.904    IO predict tut 79.43% pow=18.94 f0=30.872 f1=36.728 f2=1155.812
2024-03-04 17:58:44.925    IO predict tut 50.61% pow=16.99 f0=26.138 f1=31.992 f2=1097.688
2024-03-04 17:58:44.934    IO predict silence 43.26% pow=14.94 f0=26.839 f1=58.890 f2=1147.464
2024-03-04 17:58:44.954    IO predict tut 73.14% pow=22.84 f0=39.613 f1=47.891 f2=1132.288
2024-03-04 17:58:44.964    IO predict tut 43.43% pow=36.39 f0=21.224 f1=28.193 f2=1185.009
2024-03-04 17:58:44.984    IO predict tut 47.41% pow=50.74 f0=23.661 f1=25.663 f2=1060.472
2024-03-04 17:58:44.994    IO predict tut 76.80% pow=45.85 f0=32.802 f1=37.385 f2=1126.788
2024-03-04 17:58:45.013    IO predict tut 79.63% pow=21.50 f0=43.530 f1=55.862 f2=1096.539
2024-03-04 17:58:45.024    IO predict hiss 42.02% pow=13.86 f0=30.556 f1=44.707 f2=1147.213
2024-03-04 17:58:45.043    IO predict tut 76.18% pow=20.43 f0=32.472 f1=35.893 f2=1207.606
2024-03-04 17:58:45.054    IO predict tut 76.32% pow=20.01 f0=41.758 f1=48.019 f2=1194.279
2024-03-04 17:58:45.073    IO predict tut 89.73% pow=22.12 f0=43.485 f1=51.588 f2=1113.371
2024-03-04 17:58:45.083    IO predict tut 66.13% pow=18.98 f0=25.975 f1=32.848 f2=1238.966
2024-03-04 17:58:45.113    IO predict silence 41.86% pow=12.94 f0=27.152 f1=38.244 f2=1128.585
2024-03-04 17:58:45.133    IO predict cluck 33.65% pow=14.93 f0=17.648 f1=30.011 f2=1086.864
2024-03-04 17:58:45.144    IO predict silence 32.61% pow=8.35 f0=38.804 f1=105.169 f2=1054.321
2024-03-04 17:58:45.252    IO predict tut 37.63% pow=7.00 f0=42.092 f1=65.548 f2=1119.501
2024-03-04 17:58:45.262    IO predict tut 61.29% pow=22.63 f0=25.387 f1=30.708 f2=1073.042
2024-03-04 17:58:45.282    IO predict tut 75.86% pow=26.16 f0=33.944 f1=41.123 f2=1180.680
2024-03-04 17:58:45.294    IO predict tut 43.06% pow=28.05 f0=23.305 f1=31.047 f2=1175.680
2024-03-04 17:58:45.313    IO predict tut 94.20% pow=37.72 f0=39.293 f1=45.263 f2=1131.075
2024-03-04 17:58:45.324    IO predict tut 84.98% pow=31.10 f0=26.916 f1=32.208 f2=1076.210
2024-03-04 17:58:45.343    IO predict tut 91.62% pow=16.61 f0=31.654 f1=36.637 f2=1190.222
2024-03-04 17:58:45.354    IO predict tut 74.85% pow=16.02 f0=24.462 f1=35.843 f2=1104.275
2024-03-04 17:58:45.373    IO predict tut 60.14% pow=18.08 f0=46.474 f1=64.588 f2=1158.906
2024-03-04 17:58:45.386    IO predict tut 82.21% pow=34.10 f0=39.245 f1=48.285 f2=1104.929
2024-03-04 17:58:45.404    IO predict tut 54.36% pow=48.82 f0=23.784 f1=35.821 f2=1103.043
2024-03-04 17:58:45.413    IO predict tut 36.85% pow=59.19 f0=24.163 f1=32.935 f2=1170.109
2024-03-04 17:58:45.434    IO predict tut 38.11% pow=63.94 f0=25.313 f1=30.971 f2=1157.015
2024-03-04 17:58:45.443    IO predict tut 73.87% pow=57.66 f0=30.687 f1=36.272 f2=1216.046
2024-03-04 17:58:45.464    IO predict tut 94.13% pow=37.97 f0=29.072 f1=33.382 f2=1205.136
"""