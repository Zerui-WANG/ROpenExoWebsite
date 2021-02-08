# ROpenExoWebsite

## Requirements

### System
- [Python 3]()
- [Pipenv]()

### App
- [Django]()
- [Fontawesom](https://fontawesome.com/icons?d=gallery)


## Get start

### Front assets (webpack)
- `npm install`
- `npm run watch`

### Django app
1. `pipenv install`
2. `pipenv run manage.py collectstatic`
3. `pipenv run manage.py runserver`


## Deploy with heroku
`heroku login`
`heroku create`
`heroku buildpacks:add --index 1 heroku/nodejs`
`heroku buildpacks:add --index 2 heroku/python`
`git push heroku main`

More info just [here](https://devcenter.heroku.com/articles/git)

### Deploy it yourself
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
