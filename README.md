# Kata DNI

**Table of contents**

-   [**Introduction**](#introduction)
-   [**What is a DNI?**](#what-is-a-dni)
-   [**How it works**](#how-it-works)

## Introduction

This is a Kata proposed by my [teacher](https://github.com/dfleta/Python_ejercicios/tree/master/Poo/DNI) to do for Christmas holidays.

The task is to create a create a program that given a DNI's number, gets its corresponding letter.

## What is a DNI?

The Documento nacional de identidad (DNI) or carnet de identidad is the Spanish national identity card.  

The letter corresponding to a DNI is calculated using the following algorithm:  
* The remainder is obtained by dividing the ID number by 23.
* The resulting number indicates the position of the letter corresponding to that DNI in the following string:

![assignment-table](https://user-images.githubusercontent.com/117761602/211127472-94543dcd-9d86-4507-857e-9f258c0910f8.jpg)

The following letters are not used: I, Ñ, O, U.  

The "I" and "O" are avoided to avoid confusion with other characters, such as "1", "l" or "0".  

## How it works

The program is formed by two classes: `AssignmentTable` and `Dni`.  

* `AssignmentTable`, as its name indicates, has the assignment table used to calculate the DNI's letter and therefore is responsible of the task of calculating the valid letter.
* `Dni` is in charge of analizing the DNIs given and check if both the numbers and the letter are valid.
