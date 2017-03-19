#!/usr/bin/env python

__author__ = "Ben McCamish, Janhavi Kulkarni, and Ted Brekken"
__credits__ = ["Ben McCamish, Janhavi Kulkarni, and Ted Brekken"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Ben McCamish"
__email__ = "mccamisb@oregonstate.edu"
__status__ = "Research"

#Pull out power and multiply by load composition distribution
#
import os, sys
import numpy as np
import constants
import logging as log
import Colorer
import matplotlib.pyplot as plt
import argparse
import copy

#verbose = False
xmin = list()
xmax = list()
xavg = list()
conceptCount = 0

#parser = argparse.ArgumentParser()
#parser.add_argument("-v","--verbose", help="increase output verbosity", action="store_true")
#parser.add_argument("trainon", help="The training csv file that the SVD will be built from")
#parser.add_argument("testRecords", help="csv file containing records to test on")
#args = parser.parse_args()


#if args.verbose:
#    log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
#    log.info("Verbose output.")
#else:
#    log.basicConfig(format="%(levelname)s: %(message)s")

# Globals
testAverage = 0

# Disable corner printing of numpy
np.set_printoptions(threshold='nan', precision=4, linewidth=75)

def getXAvg():
	global xavg
	return xavg

def TestTwoRecords(originalRecord, estimatedRecord):
	#log.info("Comparing difference between the real record and the estimated record for all records")
	differenceList = []
	
	#originalRecord = Denormalize(originalRecord)
	#estimatedRecord = Denormalize(estimatedRecord)

	for i,element in enumerate(originalRecord):
		differenceList.append(abs((element - estimatedRecord[i])) / element)

	return differenceList

# Not done yet...
def SimilarityMatching(newRecord, vBar, sBarTranspose):
	'''Performs Similarity Matching on new record to try and estimate its value'''
	newRecordConcept = np.dot(newRecord, np.dot(vBar, sBarTranspose))
	print newRecordConcept
	
# Currently Testing, but I believe it is done.
def Filtering(newRecord, vBar, vBarTranspose):
	'''Estimates missing values from record using the filtering method'''
	#log.info("Performing Filtering method")
	estimatedRecord = np.dot(newRecord, np.dot(vBar, vBarTranspose))
	#estimatedRecord = np.dot(newRecordConcept, np.dot(sBar, vBarTranspose))
	#log.info("Method complete")
	return estimatedRecord

def MAEIndividual(originalRecord, estimatedRecord):
	MAE_Voltage = np.mean(np.absolute(originalRecord[0::4]-estimatedRecord[0::4]))
	MAE_Phase = np.mean(np.absolute(originalRecord[1::4]-estimatedRecord[1::4]))
	MAE_P = np.mean(np.absolute(originalRecord[2::4]-estimatedRecord[2::4]))
	MAE_Q = np.mean(np.absolute(originalRecord[3::4]-estimatedRecord[3::4]))
	return MAE_Voltage, MAE_Phase, MAE_P, MAE_Q

def MAE(originalRecord, estimatedRecord):
	difference = abs(originalRecord - estimatedRecord)
	#print difference
	arraySum = np.sum(difference)
	error = arraySum / difference.size
	return error

# Generates matrix filled with test records
def GetTestRecords(fileName):
	return np.genfromtxt(fileName,delimiter=",")

# Creates a numpy matrix from specified .csv file
def CreateMatrix(fileName):
	'''Creates a numpy matrix from specified .csv file'''
	#log.info("Uploading Training Matrix...")
	return np.genfromtxt(fileName,delimiter=",")

def computeConcept(s):
	#square = np.square(s)
	#squareSum = np.sum(square)
	numSum = np.sum(s)
	kSum = 0
	#print squareSum
	for k,element in enumerate(s):
		#element = element**2
		kSum += element
		if (kSum/numSum) >= 0.9:
			print k+1
			return k+1

def reduceCol(data, epsi):
	getMinMax(copy.deepcopy(data))
	global xmax
	global xmin
	deletedCols = list()

	for i,col in enumerate(data[0]):
		if abs(xmax[i] - xmin[i]) <= epsi:
			data = np.delete(data, i - len(deletedCols), 1)
			deletedCols.append(i)

	return data, deletedCols



# Reduces the SVD values to the specified concept dimension
def Reduce(u, s, v, sNonDiag):
	global conceptCount
	conceptCount = computeConcept(sNonDiag)
	'''Reduces the SVD values to the specified concept dimension'''
	#log.info("Reducing U, S, V, values with concept: %d...",conceptCount)
	uRed = u[:,0:conceptCount]
	sRed = s[0:conceptCount,0:conceptCount]
	vRed = v[0:conceptCount,:]
	#log.info("Reducuction complete")

	return uRed, sRed, vRed

# Calculates SVD on given numpy matrix
def SVD(L):
	'''Calculates SVD on given numpy matrix'''
	#log.info("Performing SVD on %s...", args.trainon)
	u, s, vTranspose = np.linalg.svd(L)
	#log.info("SVD breakdown complete")

	return u, s, vTranspose

def Denormalize(row):
	# global xmax
	# global xmin
	# deRecord = list()
	# for i,element in enumerate(record):
	# 	deRecord.append(((xmax[i] - xmin[i]) * record[i] + 100*xmin[i])/100)
	global xavg
	deRecord = list()
	for i,element in enumerate(row):
		#Voltage
		if (i%4) is 0:
			row[i] = (element*constants.baseVoltage) + xavg[i]
		#Angle
		elif (i%4) is 1:
			row[i] = (element*constants.basePhase) + xavg[i]

		#Power P
		elif (i%4) is 2:
			row[i] = (element*constants.basePower) + xavg[i]

		#Power Q
		elif (i%4) is 3:
			row[i] = (element*constants.basePower) + xavg[i]

	return row
def testEstimateRecord(record, vBarTranspose):
	vBar = vBarTranspose.transpose()

	normalizedRecord = testNormalizeRow(record)
	originalRecord = np.copy(normalizedRecord)
	
	#print "SDL voltage magnitude (normalized)",normalizedRecord[(6-1)*4]
	#print "SDL voltage angle (normalized):",normalizedRecord[(6-1)*4 + 1]
	#print "WESRF voltage magnitude (normalized)",normalizedRecord[(164-1)*4]
	#print "WESRF voltage angle (normalized):",normalizedRecord[(164-1)*4 + 1]
	
	for i,element in enumerate(normalizedRecord):
		if ((i / 4) + 1) not in constants.realValues:
			normalizedRecord[i] = 0

	estimatedRecord = Filtering(normalizedRecord, vBar, vBarTranspose)

	for i in constants.realValues:
		
		# print i, "voltage magnitude (normalized)",estimatedRecord[(i-1)*4]
		# print i, "voltage angle (normalized):",estimatedRecord[(i-1)*4 + 1]
		
		estimatedRecord[(i-1)*4 + 2] = originalRecord[(i-1)*4 + 2]

	# for i,element in enumerate(estimatedRecord):
	# 	if ((i / 4) + 1) in constants.realValues:
	# 		estimatedRecord[i] = originalRecord[i]

	return estimatedRecord
	# recordCounter += 1
	# if recordCounter >= len(recordFileMatrix):
	# 	recordCounter = 0

def reduceNewRecord(record, deletedCols):
	dColCount = 0
	for i, col in enumerate(record):
		if i in deletedCols:
			record = np.delete(record, i - dColCount)
			dColCount += 1

	return record

def estimateRecord(record, reducedRecord, deletedCols, vBarTranspose):
	global xavg
	#if recordCounter == 0:
	#	print 'Reading next file'
	#	recordFileMatrix = svdPortion.GetTestRecords(startingRecordFile)

	newEstimatedRecord = [0] * 1144

	vBar = vBarTranspose.transpose()

	normalizedRecord = normalizeRow(record)
	originalRecord = np.copy(normalizedRecord)
	
	#print "SDL voltage magnitude (normalized)",normalizedRecord[(6-1)*4]
	#print "SDL voltage angle (normalized):",normalizedRecord[(6-1)*4 + 1]
	#print "WESRF voltage magnitude (normalized)",normalizedRecord[(164-1)*4]
	#print "WESRF voltage angle (normalized):",normalizedRecord[(164-1)*4 + 1]

	for i,element in enumerate(normalizedRecord):
		if ((i / 4) + 1) not in constants.realValues:
			normalizedRecord[i] = 0

	#print 'Normalized Input: ', normalizedRecord
	print  '\nNormalized Record Input:'
	print  '          VM       VA       P        Q'
	print ('Gilbert %8.4f %8.4f %8.4f %8.4f') % (normalizedRecord[(165-1)*4], normalizedRecord[(165-1)*4+1], normalizedRecord[(165-1)*4+2], normalizedRecord[(165-1)*4+3])
	print ('WESRF   %8.4f %8.4f %8.4f %8.4f') % (normalizedRecord[(164-1)*4], normalizedRecord[(164-1)*4+1], normalizedRecord[(164-1)*4+2], normalizedRecord[(164-1)*4+3])
	print ('SNELL   %8.4f %8.4f %8.4f %8.4f') % (normalizedRecord[(209-1)*4], normalizedRecord[(209-1)*4+1], normalizedRecord[(209-1)*4+2], normalizedRecord[(209-1)*4+3])
	print ('BUS 1   %8.4f %8.4f %8.4f %8.4f') % (normalizedRecord[(1-1)*4], normalizedRecord[(1-1)*4+1], normalizedRecord[(1-1)*4+2], normalizedRecord[(1-1)*4+3])
	print ('BUS 2   %8.4f %8.4f %8.4f %8.4f') % (normalizedRecord[(2-1)*4], normalizedRecord[(2-1)*4+1], normalizedRecord[(2-1)*4+2], normalizedRecord[(2-1)*4+3])
	np.savetxt("normalizedInputData.csv", normalizedRecord, delimiter=",")

	normalizedRecord = reduceNewRecord(normalizedRecord, deletedCols)
	estimatedRecord = Filtering(normalizedRecord, vBar, vBarTranspose)

	estCount = 0
	for i, val in enumerate(newEstimatedRecord):
		if i in deletedCols:
			newEstimatedRecord[i] = xavg[i]
		else:
			newEstimatedRecord[i] = estimatedRecord[estCount]
			estCount += 1

	#estimatedRecord = Filtering(normalizedRecord, vBar, vBarTranspose)

	for i in constants.realValues:
		# print i, "voltage magnitude (normalized)",estimatedRecord[(i-1)*4]
		# print i, "voltage angle (normalized):",estimatedRecord[(i-1)*4 + 1]
		
		#estimatedRecord[(i-1)*4] = originalRecord[(i-1)*4]
		#estimatedRecord[(i-1)*4 + 1] = originalRecord[(i-1)*4]

		newEstimatedRecord[(i-1)*4] = originalRecord[(i-1)*4]
		newEstimatedRecord[(i-1)*4 + 1] = originalRecord[(i-1)*4 + 1]
		newEstimatedRecord[(i-1)*4 + 2] = originalRecord[(i-1)*4 + 2]
		newEstimatedRecord[(i-1)*4 + 3] = originalRecord[(i-1)*4 + 3]


	# for i,element in enumerate(estimatedRecord):
	# 	if ((i / 4) + 1) in constants.realValues:
	# 		estimatedRecord[i] = originalRecord[i]

	#print 'Estimated Record: ', newEstimatedRecord
	print  '\nEstimated Record: '
	print  '          VM       VA       P        Q'
	print ('Gilbert %8.4f %8.4f %8.4f %8.4f') % (newEstimatedRecord[(165-1)*4], newEstimatedRecord[(165-1)*4+1], newEstimatedRecord[(165-1)*4+2], newEstimatedRecord[(165-1)*4+3])
	print ('WESRF   %8.4f %8.4f %8.4f %8.4f') % (newEstimatedRecord[(164-1)*4], newEstimatedRecord[(164-1)*4+1], newEstimatedRecord[(164-1)*4+2], newEstimatedRecord[(164-1)*4+3])
	print ('SNELL   %8.4f %8.4f %8.4f %8.4f') % (newEstimatedRecord[(209-1)*4], newEstimatedRecord[(209-1)*4+1], newEstimatedRecord[(209-1)*4+2], newEstimatedRecord[(209-1)*4+3])
	print ('BUS 1   %8.4f %8.4f %8.4f %8.4f') % (newEstimatedRecord[(1-1)*4], newEstimatedRecord[(1-1)*4+1], newEstimatedRecord[(1-1)*4+2], newEstimatedRecord[(1-1)*4+3])
	print ('BUS 2   %8.4f %8.4f %8.4f %8.4f') % (newEstimatedRecord[(2-1)*4], newEstimatedRecord[(2-1)*4+1], newEstimatedRecord[(2-1)*4+2], newEstimatedRecord[(2-1)*4+3])
	np.savetxt("estimatedRecord.csv", newEstimatedRecord, delimiter=",")
	return newEstimatedRecord
	#return estimatedRecord
	# recordCounter += 1
	# if recordCounter >= len(recordFileMatrix):
	# 	recordCounter = 0


#def testAllRecords(u, s, vTranspose, uBar, sBar, vBarTranspose):
def testAllRecords(vBarTranspose):
	'''Simple testing function that pulls from defined csv file for records'''
	global xavg
	#log.info("Uploading testbed of records")
	testRecords = GetTestRecords(args.testRecords)
	log.warning("Testing all %d records with %d concept dimensions... this may take a while...",testRecords.shape[0], conceptCount)

	#log.info("Getting mean of all columns...")
	averageColumns = xavg
	#log.info("Mean calculations complete")

	vBar = vBarTranspose.transpose()

	for j,record in enumerate(testRecords):
		#log.info("Starting record %d...", j)
		#print record
		record = normalizeRow(record)
		#print record
		originalRecord = np.copy(record)
		
		for i,element in enumerate(record):
			if ((i / 4) + 1) not in constants.realValues:
				#record[i] = averageColumns[i]
				record[i] = 0

		#estimatedRecord = SimilarityMatching(testRecords[1], vBarTranspose.transpose(), sBar.transpose())
		estimatedRecord = Filtering(record, vBar, vBarTranspose)
		#estimatedRecord = record

		for i,element in enumerate(estimatedRecord):
			if ((i / 4) + 1) in constants.realValues:
				estimatedRecord[i] = originalRecord[i]

		#differenceList = TestTwoRecords(record, estimatedRecord)
		print "Record",str(j),":"
		#print differenceList
		#print "blah",MAE(originalRecord, estimatedRecord)
		MAE_Voltage, MAE_Phase, MAE_P, MAE_Q = MAEIndividual(originalRecord, estimatedRecord)
		print "MAE_Voltage:", MAE_Voltage
		print "MAE_Phase:", MAE_Phase
		print "MAE_P:", MAE_P
		print "MAE_Q:", MAE_Q

def testNormalizeRow(row):

	for i,element in enumerate(row):
		global xavg
		#Voltage
		if (i%4) is 0:
			row[i] = (element-xavg[i])/constants.baseVoltage
		#Angle
		elif (i%4) is 1:
			row[i] = (element-xavg[i])/constants.basePhase

		#Power P
		elif (i%4) is 2:
			row[i] = (element-xavg[i])/constants.basePower

		#Power Q
		elif (i%4) is 3:
			row[i] = (element-xavg[i])/constants.basePower

	return row


def normalizeRow(row):
	#Old Normalization
	# global xmin
	# global xmax
	# for i,element in enumerate(row):
	# 	if (xmax[i] - xmin[i]) < .00001:
	# 		row[i] = 50
	# 	else:
	# 		row[i] = 100*(float(element)-xmin[i])/(xmax[i]-xmin[i])

	# return row

	for i,element in enumerate(row):
		global xavg
		#Voltage
		if (i%4) is 0:
			row[i] = (element-xavg[i])/constants.baseVoltage
		#Angle
		elif (i%4) is 1:
			row[i] = (element-xavg[i])/constants.basePhase

		#Power P
		elif (i%4) is 2:
			row[i] = (element-xavg[i])/constants.basePower

		#Power Q
		elif (i%4) is 3:
			row[i] = (element-xavg[i])/constants.basePower

	return row

def getMinMax(data):
	global xmin
	global xmax

	for col in data.T:
		xmin.append(min(col))
		xmax.append(max(col))


def normalizeFile(data):
	global xmin
	global xmax
	global xavg
	data = np.delete(data, (0), axis=0)
	data = np.delete(data, (0), axis=0)
	getMinMax(data)
	xavg = np.mean(data, axis=0)
	#Skipping headers in csv file, assumes that the data has two rows of headers
	for i,row in enumerate(data):
		data[i] = normalizeRow(row)

	np.savetxt("normalizedData.csv", data, delimiter=",")
	#xavg = np.mean(data, axis=0)
	
	return data

# Main, just for testing right now
def main():
	'''Main, just for testing right now'''
	#log.info("Uploading Training Matrix...")
	trainingData = CreateMatrix(args.trainon)
	#log.info("Training Matrix Uploaded")
	#log.info("Normalizing Training Matrix...")
	normalizedData = normalizeFile(trainingData)
	#log.info("Normalization Complete")
	#log.info("Performing SVD...")
	u, s, vTranspose = SVD(normalizedData)
	#log.info("SVD Complete")

	# Numpy SVD returns 1d matrix for s, this creates a 2d matrix 
	# with proper dimensions and fills the rest in with 0's
	sDiag = np.zeros((u.shape[1], vTranspose.shape[0]))
	sDiag[:s.shape[0], :s.shape[0]] = np.diag(s)

	#log.info("Reducing Matrix...")
	uBar, sBar, vBarTranspose = Reduce(u, sDiag, vTranspose, s)
	#log.info("Reduction Complete")

	#log.info("U*S*V is equal to %s within a small error tolerance: %s", args.trainon, np.allclose(normalizedData, np.dot(u, np.dot(sDiag, vTranspose))))

	#print sDiag
	testAllRecords(vBarTranspose)


# Giving Python the main it deserves
if __name__ == "__main__": 
	main()