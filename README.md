[![Release][release badge]][release]
[![Black][black badge]][black]
[![Flake8][flake8 badge]][flake8]
[![Imports][isort badge]][isort]
[![Tests][tests badge]][tests]
[![Code Coverage][coverage-image]][coverage]
[![Last Commit][commit badge]][commit]


<!-- Links -->
[release]: https://github.com/ryanleonbutler/black_star/releases
[black]: https://github.com/psf/black
[flake8]: https://github.com/PyCQA/flake8
[isort]: https://pycqa.github.io/isort/
[tests]: https://github.com/ryanleonbutler/black_star/tree/main/src/black_star/tests
[coverage]: https://codecov.io/gh/ryanleonbutler/black_star
[commit]: https://github.com/ryanleonbutler/black_star/commit/HEAD

<!-- Badges -->
[release badge]: https://img.shields.io/github/v/release/ryanleonbutler/black_star?include_prereleases
[black badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[flake8 badge]: https://github.com/ryanleonbutler/black_star/actions/workflows/lint.yml/badge.svg
[isort badge]: https://img.shields.io/badge/%20imports-isort-%231674b1
[tests badge]: https://github.com/ryanleonbutler/black_star/actions/workflows/tests.yml/badge.svg
[coverage-image]: https://codecov.io/gh/ryanleonbutler/black_star/branch/main/graph/badge.svg
[commit badge]: https://img.shields.io/github/last-commit/ryanleonbutler/black_star

![](https://github.com/ryanleonbutler/black_star/blob/main/docs/black_star.png?raw=true)

# BLACK STAR
**A Text-Based RPG**


### **Developer Notes**

I am a big fan of programming, Star Wars and RPG's. Eager to learn Python,
I thought it would be an awesome project to develop a game, taking all my interests as the inspiration.
What I ended up with was a sci-fi world, far far away in a Galaxy no one has ever heard from.

*Welcome to ...BLACK STAR...*

Feel free to reach out to me if you like the game and concept or if you have any ideas on what I can improve or even if you just want to say hi :-)


### **About**

Black Star is a sci-fi RPG, which takes place in a galaxy which is unknown and has never been explored, namely Black Star. A young protagonist, the player, wakes up on board a star cruiser in a holding cell, with no recollection of how he/she got there or even what his/her name is. With no memory the player explores the star cruiser in the hope to discover his/her identity and to find out how they ended up on this ship in the first place. Hold on tight for the adventure of a lifetime as you explore and survive the vast galaxy that is Black Star!


### **Controls**
```
- 'attack(a)' to attack an enemy in the area
- 'view(v)' to look around in this area
- 'map(m)' to look at the map of the world
- 'inspect(y)' to view item attributes
- 'take(t)' to take item into inventory
- 'equip(e)' to equip an item
- 'status(s)' to view current player status, attributes and equipped gear
- 'inventory(i)' to view current player's inventory
- 'up(u)', 'down(d)', 'left(l)' and 'right(r)' to move around between areas
- 'clear(c)' to clear the terminal
- 'help(h)' to to acess the Help Menu
- 'quit(q)' to quit the game
```

### **Contribute**
#### 1. Fork the project

#### 2. Clone the repo on your dev machine
```
git clone git@github.com:ryanleonbutler/black_star.git
```

#### 3. Change directory
```
cd black_star
```

#### 4 Create virtual environment
```
python3.10 -m venv venv 
```

#### 4. Activate virtual environment
```
source venv/bin/activate
```

#### 5. Upgrade pip
```
(venv) pip install --upgrade pip
```

#### 6. Install requirements
```
(venv) pip install -r requirements.txt
```

#### 7. Install development requirements
```
(venv) pip install -r requirements-dev.txt
```

#### 8. Pre-commit setup
```
(venv) pre-commit install
```

#### 9. Run tox
```
(venv) tox
```

Now make your changes and perform a pull request. You can create a branch if you are making larger feature changes. Don't hesitate to reach out to me if you need some guidance.

To run the game, just run `main.py` in `src/black_star`.
```
(venv) python src/black_star/main.py
```
