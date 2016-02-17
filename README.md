# ponger
---------
A restful python app that replies 'pong' to /ping.

```
$ python ponger.py
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
127.0.0.1 - - [13/Feb/2016 15:47:59] "GET /ping HTTP/1.1" 200 -
```

```
$ curl http://localhost:8080/ping
{
    "message": "pong"
}
```

#### Install or Build python wheel
```
git checkout https://github.com/powellchristoph/ponger.git
cd ponger && virtualenv .venv
source .venv/bin/activate

# install locally
pip install -e .

# or build a python wheel
# This will build dist/ponger-0.1.0-py2.py3-none-any.whl
python setup.py bdist_wheel
```

#### Run tests
```
$ python test_ponger.py
.
----------------------------------------------------------------------
Ran 1 test in 0.016s

OK
```
