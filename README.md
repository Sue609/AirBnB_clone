An airbnb project is a webb-based platform that facilitates the booking and renting of accomodations such as homes, apartments or rooms. The project aims to connect travelers, both local and international tourist with property owners or hosts who are willing to rent out their spaces. The goal of this project is to deploy a simple server a copy of the AirBnB website. In this project we will not implement all features, only some of them to cover all fundermental concepts of the higher level programming track. 

We shall start step by step as each step will link to a concept:
1. The console:
- Here we shall create our data model.
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)
The first piece of deploying our website is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.
This abstraction will allow us to change the type of storage easily without updating all the codebase.
The console will also be a tool to validate the storage engine.

Here are some of the key functionalities that our console will be able to handle:
1. Create: new user, property listing, or reservations.
2. Read: retrieve and display information about existing objects.
3. Update:  you can update and modify the attributes of existing objects. For example, you can change the price or availability of a property listing, update user information, or modify reservation details.
4. Delete: removing a property listing, deleting a user account, or canceling a reservation.
5. Search:  find specific objects based on criteria such as location, availability, price range, or other attributes.
etc


The command interpreter is a program that allows users to interact with a computer system or application by typing commands into text-based interface. It provides a way to control and operate the system without using a graphical user interface. To start the CLI you need to open a terminal or control prompt on your computer. This will provide you witha text-based environment where the user will enter commands and receive the corresponding output based on the desired actions.

Here is a decription of the command interpreter and how to start and use it:
1. Starting the Command Interpreter:
- Open a terminal or command prompt on your computer.
- Navigate to the project directory where the command interpreter is located.
Using the Command Interpreter:

2. Launch the command interpreter by executing the appropriate Python script or command.
- Once the command interpreter is running, you will see a prompt indicating that it is ready to accept commands.
- Enter commands and press Enter to execute them.
- The command interpreter will process the commands and perform actions accordingly.
- The output of the commands will be displayed in the terminal, providing feedback and information.

3. Examples of Command Interpreter Usage in an Airbnb Project:
- create <class_name>: Creates a new instance of a specific class (e.g., creating a new listing or user).
- show <class_name> <instance_id>: Displays information about a specific instance (e.g., showing details of a listing or user).
- update <class_name> <instance_id> <attribute_name> <attribute_value>: Updates the attribute of a specific instance (e.g., updating the price or availability of a listing).
- destroy <class_name> <instance_id>: Deletes a specific instance (e.g., removing a listing or user from the system).
all <class_name>: Displays all instances of a specific class (e.g., showing all listings or users).
- help: Provides help and usage information about the available commands.
quit or exit: Exits the command interpreter.
