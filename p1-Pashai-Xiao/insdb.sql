/*
use the command <SOURCE insdb.sql> in mysql to run this file
*/

-- select my database to store the tables
USE yxiao_482502fa20;

/*
***** insert data into tables *****
*/

--1 Video
insert into
	Video(videoCode, videoLength)
	values 
	(1, 30), (2, 60), (3, 90);

--2 Model
insert into
	Model(modelNo, width, height, weight, depth, screenSize)
	values
	('LGXXXXXXX1', 50, 30, 50, 12, 60),
	('LGXXXXXXX2', 60, 35, 60, 13, 70),
	('LGXXXXXXX3', 70, 40, 70, 14, 80);

--3 Site
insert into
	Site(siteCode, type, address, phone)
	values
	(1, 'bar', 'site1', 'sitephone1'),
	(2, 'restaurant', 'site2', 'sitephone2'),
	(3, 'bar', 'site3', 'sitephone3');

--4 DigitalDisplay
insert into
	DigitalDisplay(serialNo, schedulerSystem, modelNo)
	values
	('SNXXXXXXX1', 'Random', 'LGXXXXXXX1'),
	('SNXXXXXXX2', 'Smart', 'LGXXXXXXX2'),
	('SNXXXXXXX3', 'Virtue', 'LGXXXXXXX3');

--5 Client
insert into
	Client(clientId, name, phone, address)
	values
	(1, 'client1', 'cliphone1', 'cliaddr1'),
	(2, 'client2', 'cliphone2', 'cliaddr2'),
	(3, 'client3', 'cliphone3', 'cliaddr3');

--6 TechnicalSupport
insert into
	TechnicalSupport(empId, name, gender)
	values
	(11, 'tech1', 'm'),
	(22, 'tech2', 'm'),
	(33, 'tech3', 'm');


--7 Administrator
insert into
	Administrator(empId, name, gender)
	values
	(1, 'admin1', 'm'),
	(2, 'admin2', 'f'),
	(3, 'admin3', 'm');

--8 Salesman
insert into
	Salesman(empId, name, gender)
	values
	(111, 'salesman1', 'f'),
	(222, 'salesman2', 'f'),
	(333, 'salesman3', 'f');

--9 AirtimePackage
insert into
	AirtimePackage(packageId, class, startDate, lastDate, frequency, videoCode)
	values
	(1, 'economy', '2020-01-01', '2020-02-01', 1, 1),
	(2, 'whole day', '2020-02-01', '2020-03-01', 2, 2),
	(3, 'golden hours', '2020-03-01', '2020-04-01', 3, 3);

--10 AdmWorkHours
insert into
	AdmWorkHours(empId, day, hours)
	values
	(1, '2020-01-01', 6),
	(2, '2020-01-02', 7),
	(3, '2020-01-03', 8);

--11 Broadcasts
insert into
	Broadcasts(videoCode, siteCode)
	values
	(1, 1), (2, 2), (3, 3);

--12 Administers
insert into
	Administers(empId, siteCode)
	values
	(1, 1), (2, 2), (3, 3);

--13 Specializes
insert into
	Specializes(empId, modelNo)
	values
	(11, 'LGXXXXXXX1'),
	(22, 'LGXXXXXXX2'),
	(33, 'LGXXXXXXX3');

--14 Purchases
insert into
	Purchases(clientId, empId, packageId, commissionRate)
	values
	(1, 111, 1, 7),
	(2, 222, 2, 8),
	(3, 333, 3, 9);


--15 Locates
insert into
	Locates(serialNo, siteCode)
	values
	('SNXXXXXXX1', 1),
	('SNXXXXXXX2', 2),
	('SNXXXXXXX3', 3);




