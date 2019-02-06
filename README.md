# Bank App

## Setup

```sh
git clone https://github.com/funkensturm/neue-fische-bank-app.git
git remote add upstream https://github.com/funkensturm/neue-fische-bank-app.git
```

```sh
conda env create --file environment.yml
source activate neue-fische-bank-app
```

## Usage

```sh
conda env update --file environment.yml
source activate neue-fische-bank-app
jupyter notebook
```

## Lessons


### Lesson 1

```bash
 # Check out the branch
 git checkout lesson_1

 # Run the tests
 pytest
 flake8

 # Commit and push your results
 git add .
 git commit -m 'Implement bank'
 git push
```

Die Bank soll folgende Eigenschaften haben:

Properties:
- Namen (String)
- Accounts (List)
- Transactions (List)

Methods:
- open_account()
- add_transaction()

## Tests

```sh
pytest # tests
```

```sh
flake8 # codestyle - Should return `0` if all checks are passed successfully.
```
