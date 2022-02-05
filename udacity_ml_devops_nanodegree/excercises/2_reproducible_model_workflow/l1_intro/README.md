1. Install conda
2. Create account on [weight and biases](https://wandb.ai/home).Signup using git is preferable.
3. Install the required libraries and check the installation.
```bash
conda create --name udacity python=3.8 mlflow jupyter pandas matplotlib requests -c conda-forge
conda activate udacity
pip install wandb
wandb login # Get the API key from the account to login
# Test the wandb
echo "wandb test" > wandb_test
wandb artifact put -n testing/artifact_test wandb_test
# Test mlflow
mlflow --help
```
4. Alternatively , virtual environment can be create using [environment.yml](environment.yml) file.
```
conda env create -f environment.yml
```
> Build an ML Pipeline for Rental Prices in NYC Project high level flow


![Project flow](ml-pipeline.png)


## Glossary discussed 

**Machine Learning Operations** : MLops is a set of best practices and methods for an efficient end-to-end development and operation of performant, scalable, reliable, automated and reproducible ML solutions in a real production setting.

**Reproducible Workflow** : An orchestrated, tracked and versioned workflow that can be reproduced and inspected.