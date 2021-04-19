all: check-syntax-error test

test:
	python -munittest discover tests

check-syntax-error:
	pylint --rcfile pylintrc --disable=W,C pylings/*

check:
	pylint --rcfile pylintrc pylings/*
	black --check -l 79 pylings
