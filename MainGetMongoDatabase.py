from math import sqrt
from ConnectionDatasetResults import ConnectionDatasetResults

class MainGetMongoDatabase:
	def transform_float_row(self, row):
		fields = ['year', 'height', 'weight', 'insPeakFlow', 'insFlowDuration', 'expPeakFlow', 'expFlowDuration', 'respiratoryRate', 'duration_game', 'result', 'stageId', 'phase', 'level']
		for field in fields:
			row[field] = float(0 if row[field] is None else row[field])
		return row

	# Convert string column to integer
	def transform_data(self, matrix_data):
		for row  in matrix_data:
			self.transform_float_row(row)
			if(row["sex"] == "Male"):
				row["sex"] = 0
			elif(row["sex"] == "Female"):
				row["sex"] = 1
			elif(row["sex"] != "Female" and row["sex"] != "Male"):
				row["sex"] = 99
			if(row["condition"] == "Healthy"):
				row["condition"] = 0
			elif((row["condition"] != "Healthy")):
				row["condition"] = 99
		return matrix_data


	# Calculate the Euclidean distance between two vectors
	def euclidean_distance(self, row1, row2):
		distance = 0.0
		for i in range(len(row1)-1):
			distance += (row1[i] - row2[i])**2
		return sqrt(distance)

	def get_values_list(self, row):
		arrayValues = list(row.values())
		arrayValues.pop(0)
		return arrayValues

	# Locate the most similar neighbors
	def get_neighbors_index(self, train, test_row, num_neighbors):
		distances = list()
		for train_row in train:
			arrayValueTestRow = self.get_values_list(test_row)
			arrayValueTrainRow = self.get_values_list(train_row)
			dist = self.euclidean_distance(arrayValueTestRow, arrayValueTrainRow)
			distances.append((train_row, dist))
		distances.sort(key=lambda tup: tup[1])
		neighbors = []
		for i in range(num_neighbors):
			neighbors.append(distances[i][0])
		return neighbors
		

	def get_neighbors_ids(self, pacientTestId):
		# Variable Configurations
		num_neighbors = 5

		# Get Data Pacient Train
		connectionDatasetResults = ConnectionDatasetResults()

		if(pacientTestId):
			dataset = connectionDatasetResults.get_datasetResults(pacientTestId)
			datasetTransformed = self.transform_data(dataset)

			# Teste Row for get Neighbors
			rowTest = connectionDatasetResults.pacientTestInformations(pacientTestId)
			rowTestTransformed = self.transform_data([rowTest])
			pacientTestId = rowTest["pacientId"]

			# Get Neighbors
			neighbors = self.get_neighbors_index(datasetTransformed, rowTestTransformed[0], num_neighbors)
			neighborsPacientIds = [neighbor["pacientId"] for neighbor in neighbors]
		else:
			pacientTestId = None
			neighborsPacientIds = []
		return { "pacientTestId": pacientTestId, "neighborsPacientIds": neighborsPacientIds }
