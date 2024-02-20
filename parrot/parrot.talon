# Needs Talon Beta.
# Only decent additional sounds (I think): tut, shush, cluck. Maybe buzz (zzz).

parrot(cluck): 
	user.noise_trigger_cluck()

parrot(shush):
	user.noise_parrot_trigger_shush(true)
	#print("+++ shush start")
#parrot(shush:repeat):
	#user.noise_trigger_shush_active()
	#print("= shush repeat")
parrot(shush:stop):	
	user.noise_parrot_trigger_shush(false)
	#print("--- shush end")

parrot(tut): user.noise_trigger_tut()

parrot(hiss):
	user.noise_parrot_trigger_hiss(true)
	#print("+++ hiss start")
#parrot(hiss:repeat): 
	#print("hiss repeat")
parrot(hiss:stop):	
	user.noise_parrot_trigger_hiss(false)
	#print("--- hiss end")
	#print("hiss end")

parrot(pop): user.noise_trigger_pop()
#parrot(whistle): print("whistle")
