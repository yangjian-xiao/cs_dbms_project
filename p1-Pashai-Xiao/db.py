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




