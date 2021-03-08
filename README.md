# REST API based on Tornado [Python]

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This project based on simple CRUD method, we can get some information from data base trought this REST API.

### Tech-Stack

- [Tornado] - Backend engine for running Python library.Write by C/C++ language.

- [MySQL] - Relation database, stored data for backend mechanism.

Other:

- [Postman] - Testing

```sh
$ git clone https://github.com/Dursky/Tornado-REST-API.git
$ cd Tornado-REST-API
$ python3 REST-API.py

```

At the end go to link:
http://127.0.0.1:8888/

### Documentation / Dokumentacja

[POST]
[PL] Tworzenie nowego uzytkownika:<br>
[EN] Creating new user <br>
/users/[name]/[email] <br>

[GET]
[PL] Pobieranie uzytkownikow:<br>
[EN] Getting users: <br>
/users

[GET]
[PL] Pobieranie uzytkownikow przez id:<br>
[EN] Getting users by id: <br>
/users/[id]

[PUT]
[PL] Edycja uzytkownika<br>
[EN] Edit the user <br>
127.0.0.1:3000/users/[id]/[name]/[email]<br>
