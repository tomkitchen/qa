from django.shortcuts import render
from django.http import HttpResponse
from .models import Card
import random


# Create your views here.

def osce_random(request):
	all_cards = Card.objects.all()
	stations = Card._meta.get_field('station').choices
	count = len(stations)
	index = random.random() * (count)
        int_index = int(round(index, 0))
        return osce(request, int_index)

def get_random_station():
	stations = Card._meta.get_field('station').choices
        count = len(stations)
        index = random.random() * (count)
        int_index = int(round(index, 0))
	int_index = 1
	if int_index == 1:
		return station1()
	else:
		return station1()

def stationDetails(station):
	if station == '1':
		weight = random.randint(3, 50) * float(1)
      		period = random.randint(1, 23)
       		maintenanceRate = random.randint(45, 60)
#      		dripFactor = random.randint(10, 50)
		dripFactor = random.choice([15, 20, 60])
		totalMaintenance = maintenanceRate * weight
		hourlyMaintenance = totalMaintenance / period
		minuteMaintenance = hourlyMaintenance / float(60)
		frequency = minuteMaintenance * dripFactor
      		qText =  """The vetinary surgeon decides that a %d kg patient requires administration of intravenous crystalloid fluids, over a period of %d hours.<br><div align="left">Maintenance rate = %d ml/kg/day<br>Drip factor = %d drops/ml</div><br><br>Calculate:<br><div align="left">a; The total daily maintenance<br>b; ml per hour<br>c; The fluid administration rate (Drops per minute)</div>""" % (weight, period, maintenanceRate, dripFactor)
    		aText = """<div align="left">a; total daily maintenance = maintenance rate x mass<br></div>
				%d x %.0f = %d ml <br><br>
			shhhhhhhoooow, given over %d hours.....<br><br>
			<div align="left">b; ml per hr = total daily maintenance &divide; time period<br></div>
				%d &divide; %d = %.2f ml/hr<br><br>
			<div align="left">c; drops per min:<br>    
				&nbsp;&nbsp;&nbsp;&nbsp;i; ml per min = ml per hr &divide; 60<br></div>
					%.2f &divide; 60 = %.2f<br><br>    
				<div align="left">&nbsp;&nbsp;&nbsp;&nbsp;ii; drops per min = ml per min x drip factor<br></div>
					%.2f x %d = %.2f drops/min</div>""" % (
				maintenanceRate, weight, totalMaintenance,
				period, 
				totalMaintenance, period, hourlyMaintenance, 
				hourlyMaintenance, minuteMaintenance,
				minuteMaintenance, dripFactor, frequency)	
		context = {'qText': qText, 'aText': aText}
        	return context
	elif station == '2':
		doseRate = random.randint(10,100)
		mass = random.randint(2,50)
		qText = "A young %dkg Labrador has had a fracture repair to his left fore leg. He is to be administered [generic name] as [trade name].<br><br>Using the dose rate %dml/kg:<br><br>Calculate the correct dose of [generic name] to be given to this patient" % (mass, doseRate)
		aText = "dose = mass x dose rate<br>%d x %d = %dml" % (mass, doseRate, mass * doseRate)
		context = {'qText': qText, 'aText': aText}
		return context
	elif station == '3':
		doseRate = random.randint(10,100)
		mass = random.randint(2,50)
		concentration = 50 * float(1)
		dose = doseRate * mass
		qText = "Bobby is a young %dkg Labrador who has had a traumatic wound to his face debrided and sutured. He is to have antibiotic cover of (generic name) as (trade name).<br><br>Using the dose rate %dmg/kg, calculate the correct dose of (generic name) to be given to this patient.<br><br>The bottle states that the concentration is %dmg/ml." % (mass, doseRate, concentration)
		aText = "dose = mass x dose rate<br>%d x %d = %dml<br><br>volume = dose &divide; concentration<br>%d &divide %d = %.2fml" % (mass, doseRate, dose, dose, concentration, dose / concentration)
		context = {'qText': qText, 'aText': aText}
		return context
	elif station == '4':
		doseRate = random.randint(10,100)
		mass = random.randint(2,50)
		dose = mass * doseRate * float(1)
		qText = "A %dkg thoroughbred foal has a stake injury to his ventral chest. He is to have antibiotic cover of Excenel injection 50mg/ml.<br><br>a: Using the dose rate %dmg/kg, calculate the correct dose of Excenel to be given to this patient" % (mass, doseRate)
		aText = "a: dose = mass x dose rate<br>%d x %d = %dmg.<br><br>volume = dose &divide; concentration<br>%.0f &divide; 50 = %.2fml" % (mass, doseRate, mass * doseRate, dose, dose/float(50))
		context = {'qText': qText, 'aText': aText}
                return context
	elif station == '5':
                doseRate = random.randint(10,100)
                mass = random.randint(2,50)
                dose = mass * doseRate * float(1)
                qText = """
		Poppy, a %dkg Shetland pony foal, has a wire wound injury to her left hind limb. She is to have antibiotic cover of Depocillin injection 300mg/ml.<br><br>
		a: Using the dose rate %dmg/kg, calculate the correct dose of Depocillin to be given to this patient
		""" % (mass, doseRate)
                aText = "a: dose = mass x dose rate<br>%d x %d = %dmg.<br><br>volume = dose &divide; concentration<br>%.0f &divide; 300 = %.2fml" % (mass, doseRate, mass * doseRate, dose, dose/float(300))
                context = {'qText': qText, 'aText': aText}
                return context
	elif station == '6':
		mealPerDay = random.randint(3,10)
		dailyDose = random.randint(500,1000)* float(1)
		dosePerFeed = dailyDose / mealPerDay
		qText = """
		This cat has been hospitalised following surgery to repair a fractured jaw. The veterinary surgeon requests that you provide its nutritional requirements via a naso-oesophageal (6fg) tube. <br>The patient is being fed %d meals a day.<br><br> Determine the volume of food required for each meal given they require %.0f ml per day.
                """ % (mealPerDay, dailyDose)
                aText = """
		ml per feed = ml per day &divide; MEALS per day<br>
		%.2f &divide; %d = %.2fml per feed
		""" % (dailyDose, mealPerDay, dosePerFeed)
                context = {'qText': qText, 'aText': aText}
                return context
	elif station == '9':
		weight = random.randint(3, 50) * float(1)
		if weight > 10:
			tidalVolume = 10
		else:
			tidalVolume = 15
		circuitFactor = float(2.5)
		respirationRate = random.randint(10,40)
		qText = """The vetinary surgeon wants to anaesthetise a %dkg cat for ovariohysterectomy<br>
			Using the equipment available, select, assemble and attach the most appropriate anaesthetic breathing system
			for this patient.<br><br>
			As this is the first induction of the day, you will also need to check that the anaesthetic machine is ready
			for use. Explain to the examiner the checks you are making.<br><br>
			For this patient you are required to calculate:
			<div align="left">a: Tidal volume (%dml/kg)<br>
			b; Minute volume<br>
			c; Fresh gas flow per minute</div>
			The patient has a pre-anaesthetic respiration rate %d breaths per minute
		""" %(
		weight,
		tidalVolume,
		respirationRate
		)
		aText = """a; Tidal volume = Bodyweight x %dml/kg <br>
			%d x %d = %dml <br><br>
		b; Minute Volume = Tidal Volume x Respiratory Rate<br>
			%d x %d = %dml/min<br><br>
		c; FGF = Minute Volume x Circuit Factor <br>
			%d x %.1f = %.2fml/min

		""" %(
		tidalVolume,
		weight, tidalVolume, weight * tidalVolume,
		weight * tidalVolume, respirationRate, weight * tidalVolume * respirationRate,
		weight * tidalVolume * respirationRate, circuitFactor, circuitFactor * weight * tidalVolume * respirationRate
		)
		context = {'qText': qText, 'aText': aText}
                return context
	elif station == '10':
                weight = random.randint(3, 50) * float(1)
                if weight > 10:
                        tidalVolume = 10
                else:
                        tidalVolume = 15
                circuitFactor = float(2.5)
                respirationRate = random.randint(10,40)
                qText = """A %dkg patient has been admitted with a suspected ruptured diaphragm. The veterinary surgeon wants to anaesthetise 
			the patient and may require you to provide assisted ventilation during anaesthesia<br>
			Using the equipment available, select, assemble and attach the most appropriate anaesthetic breathing system
                        for this patient.<br><br>
                        As this is the first induction of the day, you will also need to check that the anaesthetic machine is ready
                        for use. Explain to the examiner the checks you are making.<br><br>
                        For this patient you are required to calculate:
                        <div align="left">a: Tidal volume (%dml/kg)<br>
                        b; Minute volume<br>
                        c; Fresh gas flow per minute</div>
                        The patient has a pre-anaesthetic respiration rate %d breaths per minute
                """ %(
                weight,
                tidalVolume,
                respirationRate
                )
                aText = """a; Tidal volume = Bodyweight x %dml/kg <br>
                        %d x %d = %dml <br><br>
                b; Minute Volume = Tidal Volume x Respiratory Rate<br>
                        %d x %d = %dml/min<br><br>
                c; FGF = Minute Volume x Circuit Factor <br>
                        %d x %.1f = %.2fml/min

                """ %(
                tidalVolume,
                weight, tidalVolume, weight * tidalVolume,
                weight * tidalVolume, respirationRate, weight * tidalVolume * respirationRate,
                weight * tidalVolume * respirationRate, circuitFactor, circuitFactor * weight * tidalVolume * respirationRate
                )
                context = {'qText': qText, 'aText': aText}
                return context
	elif station == '11':
                weight = random.randint(3, 50) * float(1)
                if weight > 10:
                        tidalVolume = 10
                else:
                        tidalVolume = 15
                circuitFactor = float(1.5)
                respirationRate = random.randint(10,40)
                qText = """The veterinary surgeon wants to anaesthetise a %dkg patient for radiography and has requested that a 
			parallel Lack anaesthetic breathing system is used.<br>
                        Using the equipment available, select, assemble and attach the most appropriate anaesthetic breathing system
                        for this patient.<br><br>
                        As this is the first induction of the day, you will also need to check that the anaesthetic machine is ready
                        for use. Explain to the examiner the checks you are making.<br><br>
                        For this patient you are required to calculate:
                        <div align="left">a: Tidal volume (%dml/kg)<br>
                        b; Minute volume<br>
                        c; Fresh gas flow per minute</div>
                        The patient has a pre-anaesthetic respiration rate %d breaths per minute
                """ %(
                weight,
                tidalVolume,
                respirationRate
                )
                aText = """a; Tidal volume = Bodyweight x %dml/kg <br>
                        %d x %d = %dml <br><br>
                b; Minute Volume = Tidal Volume x Respiratory Rate<br>
                        %d x %d = %dml/min<br><br>
                c; FGF = Minute Volume x Circuit Factor <br>
                        %d x %.1f = %.2fml/min

                """ %(
                tidalVolume,
                weight, tidalVolume, weight * tidalVolume,
                weight * tidalVolume, respirationRate, weight * tidalVolume * respirationRate,
                weight * tidalVolume * respirationRate, circuitFactor, circuitFactor * weight * tidalVolume * respirationRate
                )
                context = {'qText': qText, 'aText': aText}
                return context
	elif station == '12':
                weight = random.randint(3, 50) * float(1)
                if weight > 10:
                        tidalVolume = 10
                else:
                        tidalVolume = 15
                circuitFactor = float(1.5)
                respirationRate = 20
                qText = """The veterinary surgeon wants to anaesthetise a %dkg dog for dental treatment.<br>
                        Using the equipment available, select, assemble and attach the most appropriate anaesthetic breathing system
                        for this patient.<br><br>
			Select and prepare the most appropriate endotracheal tube.<br><br>
                        As this is the first induction of the day, you will also need to check that the anaesthetic machine is ready
                        for use. Explain to the examiner the checks you are making.<br><br>
                        For this patient you are required to calculate:
                        <div align="left">a: Tidal volume (%dml/kg)<br>
                        b; Minute volume<br>
                        c; Fresh gas flow per minute</div>
                        Set the oxygen flowmeter to show the fresh gas flow setting for this patient. The patient has a pre-anaesthetic respiration rate %d breaths per minute
                """ %(
                weight,
                tidalVolume,
                respirationRate
                )
                aText = """a; Tidal volume = Bodyweight x %dml/kg <br>
                        %d x %d = %dml <br><br>
                b; Minute Volume = Tidal Volume x Respiratory Rate<br>
                        %d x %d = %dml/min<br><br>
                c; FGF = Minute Volume x Circuit Factor <br>
                        %d x %.1f = %.2fml/min

                """ %(
                tidalVolume,
                weight, tidalVolume, weight * tidalVolume,
                weight * tidalVolume, respirationRate, weight * tidalVolume * respirationRate,
                weight * tidalVolume * respirationRate, circuitFactor, circuitFactor * weight * tidalVolume * respirationRate
                )
                context = {'qText': qText, 'aText': aText}
                return context
	else:
		context = {'qText': 'other', 'aText': 'other'}
		return context

def osce(request, stn):
	stations = Card._meta.get_field('station').choices
        count = len(stations)
        index = random.random() * (count)
        int_index = int(round(index, 0))
	if stn == '999':
                stn = str(int_index)
	context = stationDetails(stn)
	context['stationNumber'] = stn
	context['station'] = Card._meta.get_field('station').choices[int(stn) - 1][1]
    	return render(request, 'osce.html', context)
