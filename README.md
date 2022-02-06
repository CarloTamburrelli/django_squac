## Very Important

Phase 2 of the game (battle part) is yet to be finished implementing.The system currently only redirects players to battle (only multivelox and kerokaznu).

In this moment there are 3 users (and of course admin) :
```sh
test (has no battle)
multivelox (must fight)
kerokaznu (must fight)
```

**To understand how it works, log in first with the "test" and play and then with "multivelox" (the latter user already has a battle to do with kerokaznu)**

## How it works?

After installing the application, go to this address for the rules of the game: http://127.0.0.1:8000/about/ 


## How to login

*All users have 'adminadmin' as the password*

# Install

Type the follow:
```sh
python3 -m venv venv
```

```sh
source venv/bin/activate
```

```sh
pip install -r requirements.txt
```
And run:

```sh
python manage.py runserver
```
**It is not necessary to do any migration because the project uses SQLite**