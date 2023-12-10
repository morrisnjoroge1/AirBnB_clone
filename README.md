<strong>0x00. AirBnB clone - The console<strong>


![image](https://github.com/AnneMbulwa/AirBnB_clone/assets/91100743/8caf3204-f769-433c-9dec-8e09d1551859)

PROJECT FINAL DERAVATIVES


After 4 months, you will have a complete web application composed by:

A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
A website (the front-end) that shows the final product to everybody: static and dynamic
A database or files that store data (data = objects)
An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)



![image](https://github.com/AnneMbulwa/AirBnB_clone/assets/91100743/18168b9e-53b5-438d-9b18-15059b7863e4)



Description of the project


This is the first part of the AirBnB clone project where we worked on the backend of the project whiles interfacing it with a console application with the help of the cmd module in python.

Data (python objects) generated are stored in a json file and can be accessed with the help of the json module in python

0x01 Introduction
Team project to build a clone of AirBnB.

The console is a command interpreter to manage objects abstraction between objects and how they are stored.

To see the fundamental background of the project visit the Wiki.

The console will perform the following tasks:

create a new object
retrive an object from a file
do operations on objects
destroy an object


Description of the command interpreter


The interface of the application is just like the Bash shell except that this has a limited number of accepted commands that were solely defined for the purposes of the usage of the AirBnB website.

This command line interpreter serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming.

some of the commands in our interpreter
<br>
Create a new object (ex: a new User or a new Place)
<br>
Retrieve an object from a file, a database etc…
<br>
Do operations on objects (count, compute stats, etc…)
<br>
Update attributes of an object
<br>
Destroy an object
<br>

Available commands
<br>
Command	Explanation
<br>
create	Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
<br>
show	Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234
<br>
all	Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel
<br>
update	Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
<br>

Normal command input
<br>


Command	Example
<br>
create	create [class name]
<br>
show	show [class name] [id]
<br>
all	create [class name] [id]
<br>
update	create [class name] [id] [arg_name] [arg_value]
<br>


<u>Available classes</U>
<br>
BaseModel  id, created_at, updated_at
<br>
User	email, password, first_name, last_name
<br>
State	name state_id
<br>
City	name
<br>
Amenity	name
<br>
Place	city_id user_id name description number_rooms number_bathrooms max_guest price_by_night latitude``longitude amenity_ids
<br>
Review	place_id user_id text
<br>

<b>How To Start It</b>
<br>
INSTALLING


first clone the repository:https://github.com/AnneMbulwa/AirBnB_clone.git
<br>

then cd into the AirBnB_clone repository

that contains several files:
<br>
 		console.py : The main executable of the project, the command interpreter
		<br>
		models/engine/file_storage.py: Class that serializes instances to a JSON file and deserializes JSON file to instances
		<br>
		models/__ init __.py: A unique FileStorage instance for the application
		<br>
		models/base_model.py: Class that defines all common attributes/methods for other classes.
		<br>
		models/user.py: User class that inherits from BaseModel
		<br>
		models/state.py: State class that inherits from BaseModel
		<br>
		models/city.py: City class that inherits from BaseModel
		<br>
		models/amenity.py: Amenity class that inherits from BaseModel
		<br>
		models/place.py: Place class that inherits from BaseModel
		<br>
		models/review.py: Review class that inherits from BaseModel
		<br>


<strong>RUN</strong>

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
