.PHONY: test evaluate run
run:
	uvicorn app.main:app --reload
test:
	pytest -q
evaluate:
	python -m app.evaluate
