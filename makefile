all: bootstrap

bootstrap: .venv requirements.txt
	. .venv/bin/activate && pip install -r requirements.txt

.venv:
	python -m venv .venv

clean:
	rm -rf .venv

get-access-token: bootstrap
	. .venv/bin/activate && python get-access-token.py

