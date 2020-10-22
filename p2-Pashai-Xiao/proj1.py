import mysql.connector

#connect to database server
mydb = mysql.connector.connect(
	host = 'dbclass',
	user = 'yxiao',
	password = 'dbms123456',
	database = 'yxiao_482502fa20')

#create database cursor
mycursor = mydb.cursor()


def main():
	import argparse
	ap = argparse.ArgumentParser(description='database queries.')
	ap.add_argument('QuestionNumber',help = 'the sequence number of each specific question.', choices={'1', '2','3','4','5','6','7','8'})
	ap.add_argument('-EI','--ExtraInformation',help='the second parameter for some particular questions.')
	args = vars(ap.parse_args())
	# args = {'QuestionNumber': '3', 'ExtraInformation':'LGXXXXXXX2'}
	if args['QuestionNumber'] == '1':
		sql = 'select * \
				from Site\
				where address like "%s";' % ('%'+args['ExtraInformation']+'%')
		#sel = args['ExtraInformation']
		#sql = 'SELECT * FROM Site WHERE address LIKE "%s";' % ('%%%s%%' % sel)
		mycursor.execute(sql)
		myresult = mycursor.fetchall()

		for x in myresult:
			print(x)	

	elif args['QuestionNumber'] == '2':
		sql = 'select D.serialNo,D.modelNo, S.empId\
				from DigitalDisplay as D, Specializes as S\
				where S.modelNo = D.modelNo and D.schedulerSystem = "%s";'\
				 % (args['ExtraInformation']) 
		mycursor.execute(sql)
		myresult = mycursor.fetchall()

		for x in myresult:
			print(x)	

	elif args['QuestionNumber'] == '3':
		sql = 'select name, count(empId)\
				from Salesman\
				group by name;'
		mycursor.execute(sql)
		myresult = mycursor.fetchall()

		#formated output

		print('{0:<20s}{1:>5s}'.format('Name','cnt'))
		print('{0:-<20}'.format('-'))
		for x in myresult:
			print('{0:<20s}{1:>5d}'.format(x[0],x[1]))

	elif args['QuestionNumber'] == '4':
		sql = 'select *\
				from Client\
				where phone = "%s";'\
				 % (args['ExtraInformation'])
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		for x in myresult:
			print(x)


	elif args['QuestionNumber'] == '5':
		sql = 'select AH.empId, A.name, sum(AH.hours)\
				from AdmWorkHours as AH, Administrator as A\
				where AH.empId = A.empId\
				group by AH.empId\
				order by sum(AH.hours) asc;'
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		for x in myresult:
			print(x)


	elif args['QuestionNumber'] == '6':
		sql = 'select T.name \
				from Specializes as S, TechnicalSupport as T\
				where S.empId = T.empId and S.modelNo = "%s"'\
				 % (args['ExtraInformation'])
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		for x in myresult:
			print(x)



	elif args['QuestionNumber'] == '7':
		sql = 'with empId_avg_CR(empId,avg_CR) as\
				(select empId, avg(commissionRate) as avg_CR\
				 from Purchases\
				 group by empId)\
				select S.name, E.avg_CR\
				from Salesman S, empId_avg_CR E\
				where E.empId = S.empId\
				order by avg_CR desc;'
		mycursor.execute(sql)
		myresult = mycursor.fetchall()
		for x in myresult:
			print(x)
	else:
		print('{0:20s}{1:>5s}'.format('Role','cnt'))
		print('{0:-<20}'.format('-'))
		roles = ['Administrator','Salesman','TechnicalSupport']
		for i in range(len(roles)):
			sql = 'select count(empId)\
				from %s' % (roles[i])
			mycursor.execute(sql)
			myresult = mycursor.fetchall()
			for x in myresult:
				print('{0:20s}{1:>5d}'.format(roles[i],x[0]))

if __name__ == '__main__':
	main()