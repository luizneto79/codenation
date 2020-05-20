"""
Codenation - Acelera DEV - Desafio 2
Author: Luiz Marques Neto
Date: 2020-05-20
"""


import abc


class Department:

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __str__(self):
        return self.code + ' ' + self.name


class Employee(metaclass=abc.ABCMeta):

    def __init__(self, code, name, salary, department):
        self.code = code
        self.name = name
        self.salary = salary
        self.__WORK_HOUR = 8
        self.__departament = department

    def __str__(self):
        return self.name + ' ' + self.get_departament()

    @abc.abstractmethod
    def calc_bonus(self):
        pass

    @abc.abstractmethod
    def get_hours(self):
        return self.__WORK_HOUR

    def get_departament(self):
        return self.__departament.name

    def set_departament(self, description):
        self.__departament = description


class Manager(Employee):

    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * 0.15

    def get_hours(self):
        return super().get_hours()


class Seller(Employee):

    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0

    def calc_bonus(self):
        return self.__sales * 0.15

    def get_sales(self):
        return self.__sales

    def put_sales(self, sales):
        self.__sales += sales

    def get_hours(self):
        return super().get_hours()

