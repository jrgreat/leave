1. 查询" 01 "课程比" 02 "课程成绩高的学生的信息及课程分数

select sc1.SId, sc1.score, sc2.score
from SC sc1 , SC sc2 where sc1.sid = sc2.sid and sc1.CId = '01' and sc2.cid = '02' and sc1.score > sc2.score

1.1 查询同时存在" 01 "课程和" 02 "课程的情况
select sc1.Sid,sc1.score,sc2.score
from SC sc1 , SC sc2
where sc1.cid='01' and sc2.cid='02' and sc1.sid = sc2.sid

1.2 查询存在" 01 "课程但可能不存在" 02 "课程的情况(不存在时显示为 null )
select t1.sid, t1.score, t2.score
from (select sid, score from SC where cid = '01') t1 left join (select sid, score from SC where cid = '02') t2 on t1.sid = t2.sid


2. 查询平均成绩大于等于 60 分的同学的学生编号和学生姓名和平均成绩
select *, t2.avg_score
from Student t1
inner join
(select sid, AVG(score) as avg_score
from SC
group by SID
having AVG(score) > 60) t2
on t1.SId = t2.sid


3. 查询在 SC 表存在成绩的学生信息
select *
from Student
where sid in (select sid from SC)


4.查询所有同学的学生编号、学生姓名、选课总数、所有课程的总成绩(没成绩的显示为null)
select t1.SId,t1.Sname,t2.total_courses, t2.total_score
from Student t1 left join
(select sid,count(DISTINCT cid) as total_courses,sum(score) as total_score
from SC
group by sid) t2
on t1.SId = t2.sid


5. 查询「李」姓老师的数量
select count(*)
from Teacher
where Tname like '李%

6. 查询学过「张三」老师授课的同学的信息
select *
from Student
where sid in (
select s.SId
from Course c inner join SC s on c.CId=s.cid inner join Teacher t on t.TId = c.tid
where t.Tname = '张三')

7. 查询没有学全所有课程的同学的信息
select s.*
from Student s left join
(select sid, count(cid) as courses
from SC sc
group by sc.sid
) t
on s.sid = t.sid
where courses is NULL or courses <3

8. 查询至少有一门课与学号为" 01 "的同学所学相同的同学的信息
select *
from Student
where sid in
(
select DISTINCT sid
from SC
where cid in
(select cid
from SC
where sid='01') and sid <>'01')

9.查询和" 01 "号的同学学习的课程完全相同的其他同学的信息
select s.*
from Student s inner join
(
select sid, count(cid)
from SC
where sid <>'01'
group by sid
having count(cid)= (select count(cid) from SC where sid='01')) t
on s.sid = t.sid

10.查询没学过"张三"老师讲授的任一门课程的学生姓名
select *
from Student
where sid not in (
select sc.sid
from Course c INNER join Teacher t on c.tid = t.TId INNER join SC sc on sc.cid = c.cid
where t.Tname = '张三')

11.查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩
select * from Student s
inner join
(select sid, AVG(score) as avg_score
from SC
where score < 60
group by sid
having count(cid) >= 2) t
on s.sid = t.sid

12. 检索" 01 "课程分数小于 60，按分数降序排列的学生信息
select *
from Student s inner join
(select *
from SC
where cid='01' and score<60 order by score DESC) t
on s.sid = t.sid

13. 按平均成绩从高到低显示所有学生的所有课程的成绩以及平均成绩

14. 查询各科成绩最高分、最低分和平均分：
select cid,max(score),min(score),avg(score)
from SC
group by cid

15. 按各科成绩进行排序，并显示排名， Score 重复时保留名次空缺
SELECT Cid, score,
Rank() OVER (PARTITION BY CID ORDER BY score DESC) ranking FROM SC;

16. 查询学生的总成绩，并进行排名，总分重复时保留名次空缺
SELECT sid, sum(score),
Rank() OVER ( ORDER BY sum(score) DESC) ranking FROM SC group by sid

17. 统计各科成绩各分数段人数：课程编号，课程名称，[100-85]，[85-70]，[70-60]，[60-0] 及所占百分比

19. 查询每门课程被选修的学生数
select cid,count(sid)
from SC
group by cid



21.查询男生、女生人数
select Ssex, count(*)
from Student
group by Ssex





