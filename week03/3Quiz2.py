# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:37:30 2024

@author: doris
"""
import pandas as pd
import csv


#[질의 4-0] emp.csv를 읽어서 DataFrame emp 만들기
emp = pd.read_csv('emp.csv')

#[질의 4-1] emp에 age 열을 만들어 다음을 입력하여라(14명)
#[30,40,50,30,40,50,30,40,50,30,40,50,30,40]

emp['age'] = [30,40,50,30,40,50,30,40,50,30,40,50,30,40]
emp

#[질의 4-2] INSERT INTO Emp(empno, name, job) Values (9999, ‘ALLEN’, ‘SALESMAN’)
new_row = {'EMPNO': 9999, 'ENAME': 'ALLEN', 'JOB': 'SALESMAN', 'MGR': None, 'HIREDATE': None, 'SAL': None, 'COMM': None, 'DEPTNO': None}
emp = pd.concat([emp, pd.DataFrame([new_row])], ignore_index=True)
emp


#[질의 4-3] emp의 ename=‘ALLEN’ 행을 삭제하여라
#(DELETE FROM emp WHERE ename LIKE ‘ALLEN’;)
cond = emp['ENAME'] == 'ALLEN'
emp = emp.drop(emp[cond].index)
emp

#[질의 4-4] emp의 hiredate 열을 삭제하여라
#(ALTER TABLE emp DROP COLUMN hiredate;)
emp = emp.drop(columns = ['HIREDATE'])
emp

#[질의 4-5] emp의 ename=‘SCOTT’의 sal을 3000으로 변경하여라
#(UPDATE emp SET sal=3000 WHERE ename LIKE ‘SCOTT’;
cond = emp.ENAME == 'SCOTT'
emp.loc[cond,'SAL'] = 3000
emp

#[질의 5-1] emp의 sal 컬럼을 oldsal 이름으로 변경하여라.
#(ALTER TABLE emp RENAME sal TO oldsal;)

emp.rename(columns={'SAL':'OLDSAL'},inplace=True)
emp


#[질의 5-2] emp에 newsal 컬럼을 추가하여라, 값은 oldsal 컬럼값
#(ALTER TABLE emp ADD newsal …;)
emp['NEWSAL'] = emp['OLDSAL']
emp


#[질의 5-3] emp의 oldsal 컬럼을 삭제하여라
#(ALTER TABLE emp DROP COLUMN oldsal;)

emp = emp.drop(columns = ['OLDSAL'])
emp
