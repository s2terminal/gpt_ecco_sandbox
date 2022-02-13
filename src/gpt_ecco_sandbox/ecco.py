import papermill

def main():
    models = [
        "rinna/japanese-gpt2-xsmall",
        "rinna/japanese-gpt2-small",
        "rinna/japanese-gpt2-medium",
        "rinna/japanese-gpt-1b",
    ]
    for model in models:
        papermill.execute_notebook(
            'notes/ecco_template.ipynb',
            f'tmp/outputs/{model.replace("/","--")}.ipynb',
            parameters = dict(model_name=model)
        )

if __name__ == '__main__':
    main()
