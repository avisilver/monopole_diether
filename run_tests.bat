setlocal
set PYTHONPATH=.
python -m pytest -v --disable-warnings --maxfail=1 ".\tests"
endlocal
