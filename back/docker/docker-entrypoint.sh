#!/bin/bash
set -e

install() {
  permission
  pip install -r requirements.txt
}

tests() {
  install
  python -m unittest discover .
}

run() {
  permission
  if [ "$APPLICATION_ENV" = "prod" ]; then
    python3 -m uvicorn main:app --reload
  else
    tail -f
  fi
}

permission() {
  find . \! -user docker -exec chown docker '{}' +
}

case "$1" in
"install")
    echo "Install"
    install
    ;;
"tests")
    echo "Tests"
    tests
    ;;
"run")
    echo "Run"
    run
    ;;
"permission")
    echo "Permission"
    permission
    ;;
*)
    echo "Custom command : $@"
    exec "$@"
    ;;
esac