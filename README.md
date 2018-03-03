# Project 6: Brevet time calculator service

Simple listing service from project 5 stored in MongoDB database.

## Author and Contact
Luyao Wang

luyaow@uoregon.edu

## Todo

Reusing *project 5* code(https://github.com/UOCIS322/proj5-mongo). Recall: you created the 
following functionalities. 1) Two buttons ("Submit") and ("Display") in
the page where you have controle times. 2) On clicking the Submit 
button, the control times were be entered into the database. 3) On 
clicking the Display button, the entries from the database were be 
displayed in a new page. You also handled error cases appropriately. 

## Functionality add

This project has three parts: 

* Design RESTful service to expose what is stored in MongoDB.
Specifically, use the boilerplate given in DockerRestAPI folder, and
create the following:

   "http://<host:port>/listAll" should return all open and close times in the database
   
   "http://<host:port>/listOpenOnly" should return open times only
   
   "http://<host:port>/listCloseOnly" should return close times only

* Design two different representations: one in csv and one 
 in json. For the above, JSON should be your default representation. 

   "http://<host:port>/listAll/csv" should return all open and close times in CSV format
   
   "http://<host:port>/listOpenOnly/csv" should return open times only in CSV format
   
   "http://<host:port>/listCloseOnly/csv" should return close times only in CSV format

   "http://<host:port>/listAll/json" should return all open and close times in JSON format
   
   "http://<host:port>/listOpenOnly/json" should return open times only in JSON format
   
   "http://<host:port>/listCloseOnly/json" should return close times only in JSON format

* Add a query parameter to get top "k" open and close
times. For examples, see below.

   "http://<host:port>/listOpenOnly/csv?top=3" should return top 3 open times only (in ascending order) in CSV format 
   
   "http://<host:port>/listOpenOnly/json?top=5" should return top 5 open times only (in ascending order) in JSON format

* Consumer in different container.



