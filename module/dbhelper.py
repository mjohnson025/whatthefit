import pymysql.cursors

class DBhelper(object):
	def __init__(self):
		self.connection = None

	def __openConnection(self):
		self.connection = pymysql.connect(host='localhost',
																 user='allen',
																 password='243546cc',
																 db='wtf',
																 charset='utf8mb4',
																 cursorclass=pymysql.cursors.DictCursor)


	def insertWorkout(self, user, exerciseId, exerciseCount):
		try:
			self.__openConnection()
			with self.connection.cursor() as cursor:
				# Create a new record
				sql = "INSERT INTO `wtf_workouts` (`add_user`, `exercise_id`, `exercise_count`) VALUES (%s, %s, %s)"
				cursor.execute(sql, (user, exerciseId, exerciseCount))
				self.connection.commit()
		except Exception as e:
			print(e)
			raise e
		finally:
			if self.connection:
				self.connection.close()

	def getWorkout(self)
		try:
			self.__openConnection()
			with self.connection.cursor() as cursor:
				sql = ( "SELECT w.add_user w.add_date w.exercise_count s.name exercise_name m.name muscle_group ef.name effort em.name effort_multiplier "
								"FROM wtf_workouts w"
								"LEFT JOIN wtf_exercised s"
								"ON w.exercise_id = s.id"
								"LEFT JOIN wtf_MuscleGroup m"
								"ON s.MuscleGroup = m.id"
								"LEFT JOIN wtf_effort_lkup ef"
								"ON s.effort = ef.id"
								"LEFT JOIN wtf_effort_multiplier_lkup em"
								"ON s.effort_multiplier = em.id")
				cursor.execute(sql)
				result = cursor.fetchall()
				print(result)
				return result
		except Exception as e:
			print(e)
			raise e

	def getExerciseLookup(self):

		try:
			self.__openConnection()
			with self.connection.cursor() as cursor:
				# Create a new record
				sql =	( "SELECT w.id, w.name, m.name muscle_group, e.description effort, x.description effort_multiplier "
								"FROM wtf_exercises w "
								"LEFT JOIN (wtf_MuscleGroup m, wtf_effort_lkup e, wtf_effort_multiplier_lkup x) "
								"ON (w.MuscleGroup=m.id AND w.effort=e.id AND w.effort_multiplier=x.id)")

				cursor.execute(sql)
				result = cursor.fetchall()
				return result
		except Exception as e:
			raise e
		finally:
			if self.connection:
				self.connection.close()

	def getEffortLookup(self):

		try:
			self.__openConnection()
			with self.connection.cursor() as cursor:
				# Create a new record
				sql =	( "SELECT id, description FROM wtf_effort_lkup")

				cursor.execute(sql)
				result = cursor.fetchall()
				return result
		except Exception as e:
			raise e
		finally:
			if self.connection:
				self.connection.close()

	def getEffortMultiplierLookup(self):

		try:
			self.__openConnection()
			with self.connection.cursor() as cursor:
				# Create a new record
				sql =	( "SELECT id, description FROM wtf_effort_multiplier_lkup")

				cursor.execute(sql)
				result = cursor.fetchall()
				return result
		except Exception as e:
			raise e
		finally:
			if self.connection:
				self.connection.close()
