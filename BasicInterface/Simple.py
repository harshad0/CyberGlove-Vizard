import viz
import vizact
import vizshape

viz.setMultiSample(4)
viz.fov(60)
viz.go()

# Import necessary dle file for the sensor *refer polhemus on world viz
# Adding fastrack device 
'''
polhemus = viz.add('polhemus.dle') 
fastrak =  polhemus.addFastrak()
'''


#Adding Cyberglove
CyberGlove = viz.add('CyberGlove.dle')
sensor =  CyberGlove.addCyberGlove()

import hand
h = hand.add(sensor)
h.setEuler(0,-90,0)

#Uncomment if you are using it for left hand
#h.leftHand()

tips = []
for x in range(5):
     tips.append( vizshape.addSphere(radius=0.001,color=viz.BLUE) )

def UpdateFingerTips():
  '''
  Uncomment line 1 of this function if you add Fastrak
  '''
  #h.setPosition(fastrak.getPosition())
	for x,tip in enumerate(tips):
		 mat = h.getFingerTip(x)
		 tip.setPosition(mat.getPosition())
		 tip.setQuat(mat.getQuat()) 

vizact.ontimer(0,UpdateFingerTips)

import vizcam
cam = vizcam.PivotNavigate()
cam.setCenter(0,0,0)
cam.setDistance(0.3)

viz.clearcolor(viz.GRAY)
