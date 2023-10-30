#!/bin/bash
echo "Compiling $PYFILE ..."
/usr/bin/py3compile $PYFILE && mv __pycache__/$(ls __pycache__/) $PYFILE'c' && rmdir __pycache__
