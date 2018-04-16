This project is my seminary work.
This web is a big library with tutorials and aricles about game development.

As a non-registered user you can:
* Read all the articles
* Register

As a registered user you can:
* Read all the articles
* Create articles
* Comment and rate articles

As an aministrator you can:
* Do all the thing a registered user can
* Confirm(Verify) all written articles but yours

The runing page can be seen [Here!](http://tomcek.pythonanywhere.com/)

To run this project you need to do a couple of simple things.

1. First you have to have python 3.6, pip and git installed
2. Clone this repository using `git clone  https://github.com/Tomik292/GDevLib.git`
3. Type `cd GDevLib/GDevLibrary`
4. Install requirements `pip3 install -r requirements.txt`
4. Set up database
   - Create database `python3 manage.py makemigrations`  
   - Migrate `python3 manage.py migrate`
   - Clean up the database python manage.py flush
5. Create superuser `python3 manage.py createsuperuser`
6. Collect static files `python3 manage.py collectstatic`
7. Run server `python3 manage.py runserver`
