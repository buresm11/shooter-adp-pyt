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
* **Down*** - moves cannon down
* **Q** - switches between simple (static enemies, missiles) and smart (enemy moves, missiles drop to ground)
* **W** - switches between one missile/two missile mode
* **A** - decreases gravity
* **S** - increases gravity
* **E** - loads game from file
* **R** - reset save file
* **T** - saves game to file
* **U** - step back


Usage of patterns
------------------

* Strategy - 
* Proxy - 
* State - 
* Visitor - 
* Observer - 
* Command - 
* Memento -
* Abstract Factory -

