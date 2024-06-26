#!/bin/bash
set -e

install() {
  yarn
  yarn build
}

tests() {
  yarn test
}

run() {
  if [ "$APPLICATION_ENV" = "prod" ]; then
    serve -s build --no-clipboard -l 3000
  else
    tail -f
  fi
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
*)
    echo "Custom command : $@"
    exec "$@"
    ;;
esac