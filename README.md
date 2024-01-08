# AirBnB clone - The console

<figure>
    <img src="https://drive.google.com/uc?export=view&id=1sWCzpc7sIY0VCsEOpQDmJPS5q7weRhj-" alt="AirBnB fancy logo">
</figure>

The project aims to deploy a fully-fledged and sophisticated, yet simple, copy of the Airbnb website on our server.

## The console:

A command interpreter to manipulate data without a visual interface (perfect for development and debugging).<b/>

+ create data model.
+ manage (create, update, destroy, etc) objects via a console / command interpreter.
+ store and persist objects to a file (JSON file).

The first piece is to manipulate a powerful storage system. This storage engine
will give us an abstraction between “My object” and “How they are stored and persisted”.
This abstraction will also allow us to change the type of storage easily without updating all of your codebase.<b/>

The console will be a tool to validate this storage engine as the figure:

<figure>
    <img src="https://drive.google.com/uc?export=view&id=1Nq8qsHpLmrY6hihJdZaRTjoJWWnXWL6C" alt="The console">
</figure>
