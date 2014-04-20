all:

init-sumatra:
	smt init SumatraBug
	smt configure -e python -m main.py --plain

run:
	smt run -r "Create a Sumatra record."


purge:
	rm -rf .smt/ Data/
