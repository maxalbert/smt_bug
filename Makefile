all:

init-sumatra:
	smt init BugWithPlusSignInFilenames
	smt configure -e python -m main.py

run:
	smt run -r "Run to illustrate bug"
