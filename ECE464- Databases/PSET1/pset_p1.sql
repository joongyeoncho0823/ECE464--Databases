/* 
Joongyeon Steven Cho
ECE464- Databases
Problem Set 1
Question 1
*/

-- 1. List, for every boat, the number of times it has been reserved, excluding those boats that have never been reserved (list the id and the name).
SELECT B.bid, B.bname, COUNT(*) AS "# of Reserves"
FROM boats B, reserves R
WHERE B.bid = R.bid
GROUP BY B.bid, B.bname
ORDER BY B.bid;

-- 2. List those sailors who have reserved every red boat (list the id and the name).

SELECT S.sid, S.sname
FROM sailors S
WHERE NOT EXISTS (SELECT B.bid
                  FROM boats B
                  WHERE NOT EXISTS (SELECT *
                                   FROM reserves R
                                   WHERE R.bid = B.bid AND R.sid = S.sid and B.color = 'red'));

-- 3. List those sailors who have reserved only red boats.
                                                        
SELECT S.sid, S.sname
FROM sailors S
WHERE S.sid IN (SELECT R1.sid
                FROM reserves R1, boats B1
                WHERE R1.bid = B1.bid AND B1.color = 'red')
AND S.sid NOT IN (SELECT R2.sid
                  FROM reserves R2, boats B2
                  WHERE R2.bid = B2.bid and B2.color != 'red');
                  
-- 4. For which boat are there the most reservations?

SELECT B.bid, B.bname, COUNT(*) as Num_Res
FROM boats B, reserves R
WHERE B.bid = R.bid
GROUP BY B.bid
ORDER BY Num_Res DESC
LIMIT 1;

-- 5. Select all sailors who have never reserved a red boat.
                        
SELECT S.sid, S.sname
FROM sailors S
WHERE S.sid NOT IN (SELECT R.sid
                    FROM reserves R, boats B
                    WHERE R.bid = B.bid AND B.color = 'red');
            
-- 6. Find the average age of sailors with a rating of 10.

SELECT AVG(age) 
FROM sailors 
WHERE rating = 10;

-- 7. For each rating, find the name and id of the youngest sailor.

SELECT sname, sid, rating, age
FROM sailors 
JOIN (
      SELECT rating, MIN(age) age
      FROM sailors	
      GROUP BY rating
)  
USING (rating, age)
ORDER BY rating;

-- 8. Select, for each boat, the sailor who made the highest number of reservations for that boat.


SELECT DISTINCT B.bname, S.sname, COUNT(*)
FROM boats B 
			JOIN reserves R ON B.bid = R.bid
			JOIN sailors S ON S.sid = R.sid
GROUP BY B.bid, B.bname, S.sid, S.sname
HAVING COUNT(*) >= ALL
					(SELECT COUNT(*)
					FROM reserves R1
					WHERE R1.bid = B.bid
					GROUP BY R1.sid)
ORDER BY B.bname, S.sname;