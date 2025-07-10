# LLM Fine-Tuning for Classification

This repository contains my solution for the [LLM Classification Finetuning](https://www.kaggle.com/competitions/llm-classification-finetuning) competition on Kaggle. The goal is to fine-tune a language model to classify prompts based on a single target label.

## Project Structure

```
README.md
data/
    llm-classification-finetuning.zip
    llm-classification-finetuning/
        sample_submission.csv
        test.csv
        train.csv
src/
```

### Folders and Files

- **`data/`**: Contains the dataset files for training and testing.
  - `train.csv`: Training data for fine-tuning the model.
  - `test.csv`: Test data for evaluation.
  - `sample_submission.csv`: A sample format for submission.
  - `llm-classification-finetuning.zip`: Compressed dataset archive.

- **`src/`**: Directory for source code and scripts for fine-tuning and evaluation.

## Getting Started



###  Download Dataset Using Kaggle API

🔹 Step 1: Get Your Kaggle API Token
1. Go to your Kaggle account settings: https://www.kaggle.com/account

2. Scroll to the API section and click "Create New API Token"

3. This will download a file called kaggle.json — it contains your username and API key

🔹 Step 2: Configure the API Key
    Move the kaggle.json file to the appropriate directory:

On Windows (PowerShell):
    ```powershell
    mkdir ~/.kaggle
    Move-Item .\kaggle.json ~/.kaggle\kaggle.json
    ```
On macOS/Linux:
bash
    ```
    mkdir -p ~/.kaggle
    mv kaggle.json ~/.kaggle/
    chmod 600 ~/.kaggle/kaggle.json
    ```

🔹 Step 3: Install the Kaggle CLI
bash
    ```
    pip install kaggle
    ```

🔹 Step 4: Download the Dataset
On Windows (PowerShell): 

    ```
    kaggle competitions download -c llm-classification-finetuning
    ```

🔹 Step 5: Extract the Dataset
On Windows (PowerShell):

    ```
    Expand-Archive -Path "llm-classification-finetuning.zip" -DestinationPath "data"
    ```


## Dataset

The dataset is located in the `data/llm-classification-finetuning/` directory. Ensure the files are extracted before running the scripts.

