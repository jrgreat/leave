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
