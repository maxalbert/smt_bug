all:

init-sumatra:
	smt init BugWithPlusSignInFilenames
	smt configure -e python -m main.py --plain

run:
	smt run -r "Run to illustrate bug"


purge:
	rm -rf .smt/ Data/
