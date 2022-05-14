""" Tests for tables in TRN database. """

import pytest
import pyodbc


@pytest.fixture
def database_connection(driver=r'{ODBC Driver 17 for SQL Server}',
                server=r'EPRUPETW0ECA\SQLEXPRESS', 
                database='TRN'
                ) -> pyodbc.Cursor:
    """ TRN database connection. """
    parameters = f'Driver={driver};Server=' + \
            f'{server};Database={database};Trusted_Connection=yes;' + \
            r'uid=EPAM\Denis_Bulychev'
    cnxn = pyodbc.connect(parameters)
    return cnxn.cursor()


@pytest.mark.countries
def test1_count_rows_in_countries(database_connection):
    """ Check for number of rows in table hr.countries """
    query = 'select count(1) from TRN.hr.countries'
    database_connection.execute(query)
    assert database_connection.fetchone()[0] == 25


@pytest.mark.countries
def test2_most_popular_region_id_in_countries(database_connection):
    """ Check for most popular region in table hr.countries """
    query = 'select top 1 region_id from TRN.hr.countries ' + \
            'group by region_id order by count(1) desc'
    database_connection.execute(query)
    assert database_connection.fetchone()[0] == 1


@pytest.mark.jobs
def test3_biggest_salary_in_jobs(database_connection):
    """ Check for biggest salary in table hr.jobs """
    query = 'select max(max_salary) from hr.jobs'
    database_connection.execute(query)
    assert database_connection.fetchone()[0] == 40000


@pytest.mark.jobs
def test4_smallest_salary_in_jobs(database_connection):
    """ Check for smallest salary in table hr.jobs """
    query = 'select min(min_salary) from hr.jobs'
    database_connection.execute(query)
    assert database_connection.fetchone()[0] == 2000


@pytest.mark.employees
def test5_average_salary_in_employees(database_connection):
    """ Check for average salary in table hr.employees """
    query = 'select avg(salary) from hr.employees'
    database_connection.execute(query)
    assert database_connection.fetchone()[0] == 8060


@pytest.mark.jobs
@pytest.mark.employees
def test6_consistency_salary_between_employees_and_jobs(database_connection):
    """ Check for consistency between tables hr.employees and hr.jobs """
    query = 'select sum(case when e.salary between j.min_salary ' + \
            'and j.max_salary then 1 else 0 end) ' + \
            'from hr.employees e join hr.jobs j on e.job_id = j.job_id'
    database_connection.execute(query)
    assert database_connection.fetchone()[0] == 40
