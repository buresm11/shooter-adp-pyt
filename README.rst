Shooter
=======

Shooter je semestrální práce z předmětu MI-ADP, která se zaměřuje na
návrhové vzory. Jedná se o jednoduchou střílečku, jejímž úkolem je pomocí
kanónu sestřelovat nepřátelské jednotky.

Task
===============

Hra bude obsahovat následující prvky:    

* Bude implementována pomocí **pyglet**
* Možnost měnit sílu střely (natahováním ḱánónu)
* Možnost změnit úhel, pod jakým bude kanón střílet
* Změna gravitace (střely budou rychleji padat k zemi)
* Počítání skóre 
* Alespoň dva druhy nepřátel (statičtí, akční, AI)
* Možnost vystřelit více střel najednou
* Krok zpět, který vrátí hru do předcházejícího stavu
* Ukládání/načítání hry ze souboru
* Dvě strategie střel (balistická křivka, přímá)
* Bude obsahovat návrhové vzory:

  * MVC:
  * Strategy
  * Proxy
  * State
  * Visitor
  * Observer
  * Command
  * Memento
  * Abstract Factory

Documentation
===============

Installation
------------

``python setup.py install``

Usage
-----

``python -m shooter``

Keys
------------------

* **Space** - shoots missiles, holding space will increase missile power
* **Left** - rotates cannon counterclockwise
* **Right** - rotates cannon clockwise
* **Up** - moves cannon up
* **Down** - moves cannon down
* **Q** - switches between simple (static enemies, missiles ignore gravity) and smart (enemy moves, missiles drop to ground)
* **W** - switches between one missile/two missile mode
* **A** - decreases gravity
* **S** - increases gravity
* **E** - loads game from file
* **R** - reset save file, all saved progress will be lost
* **T** - saves game to file
* **U** - step back


Usage of patterns
------------------

* **Strategy** pattern is used for moving missile. Misssile that uses SimpleStrategy does not use gravity. Misssile that uses SmartStrategy uses gravity and acts like a ballistic missile.
* **Proxy** pattern is used for accesing model.
* **State** patter is used to decide whether cannon fires one or two missiles. If cannon uses OneMissileCannonState it fires one missile. If cannon uses TwoMissileCannonState it fires two missiles.
* **Visitor** pattern is used for saving state of model to a file.
* **Observer** is used for informing view that model has changed. Model registers view as observer and then notify it when needed.  
* **Memento** patter is used by model for undo. Model can save its state to memento and then go back to its previous state.
* **Command** pattern handle user input. Whenever user press key a command is created. Command also creates new memento for saving state.
* **Abstract Factory** pattern creates new missiles and enemies. SimpleFactory creates enemies that do not move and missiles that use SimpleStrategy. SmartFactory creates enemies that move and missiles that use SmartStrategy.

