-- ans(1)
SELECT DISTINCT s.modelNo
FROM Specializes as s, TechnicalSupport as t
WHERE s.empId = t.empId and t.name = 'Tom';

-- ans(2) 
SELECT t.empId, t.name
FROM TechnicalSupport as t, Specializes as s
WHERE s.empId = t.empId and s.modelNo = 'M01';

-- ans(3)
SELECT t.empId, t.name
FROM DigitalDisplay as d, Specializes as s, TechnicalSupport as t
WHERE d.schedulerSystem = 'Random' and d.modelNo = s.modelNo and s.empId = t.empId

-- ans(4)
(SELECT * FROM Administrator)
UNION
(SELECT * FROM Salesman)
UNION
(SELECT * FROM TechnicalSupport);

-- ans(5)
SELECT videoCode, videoLength
FROM Video 
WHERE videoCode in
((SELECT videoCode FROM Broadcasts WHERE siteCode = 111)
EXCEPT
(SELECT videoCode FROM Broadcasts WHERE siteCode = 112))

--ans(6)
SELECT empId
FROM Administers
GROUP BY empId
HAVING count(siteCode) >= 10;

--ans(7)
SELECT max(videoLength)
FROM Video
WHERE videoCode in
(SELECT videoCode FROM Broadcasts WHERE siteCode = 111);

--ans(8)
WITH video_112(videoCode, videoLength) as
	(SELECT videoCode, videoLength
	FROM Video
	WHERE videoCode in
	(SELECT videoCode FROM Broadcasts WHERE siteCode = 112),
	video_112_max(value) as
	(SELECT max(videoLength)
	FROM video_112)
SELECT videoCode, videoLength
FROM video_112, video_112_max
WHERE video_112.videoLength >= video_112_max.value;

--ans(9) 
SELECT *
FROM Administrator
WHERE empId in 
	(SELECT empId
		FROM Administers
		GROUP BY empId
		HAVING count(siteCode) < 10);

--ans(10)
WITH MAX_CR(value) as
	(SELECT max(commissionRate)
		FROM Purchases),
	empId_CR(empId,commissionRate) as
	(SELECT empId, commissionRate
		FROM Purchases
		WHERE commissionRate = MAX_CR.value)
SELECT E.commissionRate, S.empId, S.name
FROM Salesman AS S, empId_CR AS E 
WHERE S.empId = E.empId

--ans(11)
WITH empId_numPackage(empId, numPackage) AS
	(SELECT empId, count(packageId)
		FROM Purchases
		GROUP BY empId),
	MIN_numPackage(value) AS
	(SELECT min(numPackage)
		FROM empId_numPackage)
SELECT S.empId, S.name
FROM empId_numPackage AS EN, MIN_numPackage AS MN, Salesman AS S
WHERE S.empId = EN.empId and EN.numPackage > MN.value

--ans(12)
SELECT T.empId, T.name, T.gender
FROM Specializes S, TechnicalSupport T
WHERE T.empId = S.empId AND 
	NOT EXISTS((SELECT S2.modelNo
				FROM Specializes S2
				WHERE S2.empId = T.empId AND T.name = 'Tom')
				EXCEPT
				(SELECT S3.modelNo
				 FROM Specializes S3
				 WHERE S3.empId = S.empId));

