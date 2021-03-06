import mysql.connector

#connect to database server

mydb = mysql.connector.connect(
	host = 'dbclass',
	user = 'yxiao',
	password = 'dbms123456',
	database = 'yxiao_482502fa20')

#create database cursor
mycursor = mydb.cursor()

#create tables
mycursor.execute('\
create table Video(\
	videoCode int,\
	videoLength int,\
	primary key(videoCode));\
	')

mycursor.execute('\
create table Model(\
	modelNo char(10),\
	width numeric(6,2),\
	height numeric(6,2),\
	weight numeric(6,2),\
	depth numeric(6,2),\
	screenSize numeric(6,2),\
	primary key(modelNo));\
	')

mycursor.execute('\
create table Site(\
	siteCode int,\
	type varchar(16),\
	address varchar(100),\
	phone varchar(16),\
	primary key(siteCode),\
	check(type in ('bar', 'restaurant')));\
	')

mycursor.execute('\
create table DigitalDisplay(\
	serialNo char(10),\
	schedulerSystem char(10),\
	modelNo char(10),\
	primary key(serialNo),\
	foreign key(modelNo) references Model(modelNo)\
	on delete set null on update cascade,\
	check(schedulerSystem in ('Random', 'Smart', 'Virtue')));\
	')

mycursor.execute('\
create table Client(\
	clientId int,\
	name varchar(40),\
	phone varchar(16),\
	address varchar(100),\
	primary key(clientId));\
	')

mycursor.execute('\
create table TechnicalSupport(\
	empId int,\
	name varchar(40),\
	gender char(1),\
	primary key(empId));\
	')

mycursor.execute('\
create table Administrator(\
	empId int,\
	name varchar(40),\
	gender char(1),\
	primary key(empId));\
	')

mycursor.execute('\
create table Salesman(\
	empId int,\
	name varchar(40),\
	gender char(1),\
	primary key(empId));\
	')

mycursor.execute('\
create table AirtimePackage(\
	packageId int,\
	class varchar(16),\
	startDate date,\
	lastDate date,\
	frequency int,\
	videoCode int,\
	primary key(packageId),\
	check(class in ('economy', 'whole day', 'golden hours')));\
	')

mycursor.execute('\
create table AdmWorkHours(\
	empId int,\
	day date,\
	hours numeric(4,2),\
	primary key(empId, day),\
	foreign key(empId) references Administrator(empId)\
	on delete cascade on update cascade);\
	')

mycursor.execute('\
create table Broadcasts(\
	videoCode int,\
	siteCode int,\
	primary key(videoCode,siteCode),\
	foreign key(videoCode) references Video(videoCode)\
	on delete cascade on update cascade,\
	foreign key(siteCode) references Site(siteCode)\
	on delete cascade on update cascade); \
	')

mycursor.execute('\
create table Administers(\
	empId int,\
	siteCode int,\
	primary key(empId,siteCode),\
	foreign key(empId) references Administrator(empId)\
	on delete cascade on update cascade,\
	foreign key(siteCode) references Site(siteCode)\
	on delete cascade on update cascade);\
	')

mycursor.execute('\
create table Specializes(\
	empId int,\
	modelNo char(10),\
	primary key(empId, modelNo),\
	foreign key(empId) references TechnicalSupport(empId)\
	on delete cascade on update cascade,\
	foreign key(modelNo) references Model(modelNo)\
	on delete cascade on update cascade);\
	')

mycursor.execute('\
create table Purchases(\
	clientId int,\
	empId int,\
	packageId int,\
	commissionRate numeric(4,2),\
	primary key(clientId, empId, packageId),\
	foreign key(clientId) references Client(clientId)\
	on delete cascade on update cascade, \
	foreign key(empId) references Salesman(empId)\
	on delete cascade on update cascade, \
	foreign key(packageId) references AirtimePackage(packageId)\
	on delete cascade on update cascade); \
	')

mycursor.execute('\
create table Locates(\
	serialNo char(10),\
	siteCode int,\
	primary key(serialNo, siteCode),\
	foreign key(serialNo) references DigitalDisplay(serialNo)\
	on delete cascade on update cascade,\
	foreign key(siteCode) references Site(siteCode)\
	on delete cascade on update cascade);\
	')

# insert data into tables
sql = 'INSERT INTO Video(videoCode, videoLength) VALUES (%s, %s);'
val = [
	('1', '30'), ('2', '60'), ('3', '90')
	]
mycursor.executemany(sql, val)
mbdb.commit()

sql = 'INSERT INTO Model(modelNo, width, height, weight, depth, screenSize) VALUES (%s，%s, %s，%s,%s,%s);'
val = [
	('LGXXXXXXX1', 50, 30, 50, 12, 60),
	('LGXXXXXXX2', 60, 35, 60, 13, 70),
	('LGXXXXXXX3', 70, 40, 70, 14, 80)
	]
mycursor.executemany(sql, val)
mbdb.commit()

sql = 'insert into Site(siteCode, type, address, phone)	values	(%s, %s, %s, %s);'
val = [
	(1, 'bar', '101 E University Ave', '5756211111'),
	(2, 'restaurant', '201 E Union Ave', '5756212222'),
	(3, 'bar', '301 S Espina St', '5756213333')
	]
mycursor.executemany(sql, val)
mbdb.commit()

sql = 'insert into	DigitalDisplay(serialNo, schedulerSystem, modelNo)	values	(%s, %s, %s);'
val = [
	('SNXXXXXXX1', 'Random', 'LGXXXXXXX1'),
	('SNXXXXXXX2', 'Smart', 'LGXXXXXXX2'),
	('SNXXXXXXX3', 'Virtue', 'LGXXXXXXX3')
	]
mycursor.executemany(sql, val)
mbdb.commit()

sql = 'Client(clientId, name, phone, address)	values	(%s, %s, %s, %s);'
val = [
	(1, 'client1', 'cliphone1', 'cliaddr1'),
	(2, 'client2', 'cliphone2', 'cliaddr2'),
	(3, 'client3', 'cliphone3', 'cliaddr3')
	]
mycursor.executemany(sql, val)
mbdb.commit()

sql = 'insert into TechnicalSupport(empId, name, gender) values (%s, %s, %s);'
val = [
	(11, 'tech1', 'm'),
	(22, 'tech2', 'm'),
	(33, 'tech3', 'm')
	]
mycursor.executemany(sql, val)
mbdb.commit()

sql = 'insert into	Administrator(empId, name, gender)	values	(%s, %s, %s);'
val = [
	(1, 'admin1', 'm'),
	(2, 'admin2', 'f'),
	(3, 'admin3', 'm')
	]
mycursor.executemany(sql, val)
mbdb.commit()

sql = 'insert into	Salesman(empId, name, gender)	values	(%s, %s, %s);'
val = [
	(1, 'Peter', 'm'),
	(2, 'Mary', 'f'),
	(3, 'John', 'm'),
	(4, 'Mary', 'f')
	]
mycursor.executemany(sql, val)
mbdb.commit()

sql = 'insert into	AirtimePackage(packageId, class, startDate, lastDate, frequency, videoCode)	values\
	(%s, %s, %s, %s, %s, %s);'
val = [
	(1, 'economy', '2020-01-01', '2020-02-01', 1, 1),
	(2, 'whole day', '2020-02-01', '2020-03-01', 2, 2),
	(3, 'golden hours', '2020-03-01', '2020-04-01', 3, 3)
	]
mycursor.executemany(sql, val)
mbdb.commit()

sql = 'insert into	AdmWorkHours(empId, day, hours)	values	(%s, %s, %s);'
val = [
	(1, '2020-01-01', 6),
	(2, '2020-01-02', 7),
	(3, '2020-01-03', 8)
	]
mycursor.executemany(sql, val)
mbdb.commit()

sql = 'insert into	Broadcasts(videoCode, siteCode)	values	(%s, %s);'
val = [
	('1', '1'), ('2', '2'), ('3', '3')
	]
mycursor.executemany(sql, val)
mbdb.commit()

sql = 'insert into	Administers(empId, siteCode)	values	(%s, %s);'
val = [
	('1', 1), ('2', 2), ('3', 3)
	]
mycursor.executemany(sql, val)
mbdb.commit()

sql = 'insert into	Specializes(empId, modelNo)	values	(%s, %s);'
val = [
	(11, 'LGXXXXXXX1'),
	(22, 'LGXXXXXXX2'),
	(33, 'LGXXXXXXX3')
	]
mycursor.executemany(sql, val)
mbdb.commit()

sql = 'insert into	Purchases(clientId, empId, packageId, commissionRate)	values	(%s, %s, %s, %s);'
val = [
	('1', 111, 1, 7),
	('2', 222, 2, 8),
	('3', 333, 3, 9)
	]
mycursor.executemany(sql, val)
mbdb.commit()

sql = 'insert into	Locates(serialNo, siteCode)	values	(%s, %s);'
val = [
	('SNXXXXXXX1', 1),
	('SNXXXXXXX2', 2),
	('SNXXXXXXX3', 3)
	]
mycursor.executemany(sql, val)
mbdb.commit()

#main function

