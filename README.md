# Un installation
`powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

## project Initlization
2. `uv init .`

## Package installation 
`uvadd pakge_name'  or uv pip install package_name`

## active env
`uv venv .`

## for changing python version 
`change version in .toml file and .python-version`
`un sync`
 or `uv venv --python 3.13`
## run python file
`uv run example.py`

## set third party llm with your project
(globbaly, agnet-wise, runner(running time))

## Mlflow
`uv add  mlflow`
`mlflow server --host 0.0.0.0 --port 8080`

## run mlflow
http://localhost:8080/
