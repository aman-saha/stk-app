# stk-app
personal stock screener - Crafted by aman-saha aka darknurd

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

## Setting up virtualenv
```
$ virtualenv stk-screen
$ source stk-screen/bin/activate
$ pip install selenium
$ pip install pymongo
```

## Installing Mongod
```
$ brew services stop mongodb
$ brew uninstall mongodb

$ brew tap mongodb/brew
$ brew install mongodb-community
$ brew services start mongodb-community

```
