# stk-app
personal stock screener

## Installing pip
```
$ curl https://bootstrap.pypa.io/get-pip.py >get-pip.py
$ sudo python get-pip.py 
```

## Installing python3
```
$ brew install python3
```

## Installing virtualenv
```
$ sudo pip install virtualenv
```
```
$ virtualenv stk-screen
$ source stk-screen/bin/activate
$ pip install selenium
$ pip install pymongo

## Installing MongoDb

```
$ brew services stop mongodb
$ brew uninstall mongodb

$ brew tap mongodb/brew
$ brew install mongodb-community
$ brew services start mongodb-community

```