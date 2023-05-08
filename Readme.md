# Named Entity Recognition

This project demonstrates how to train and use a Named Entity Recognition (NER) model using PyTorch and the Hugging Face Transformers library.

## Prerequisites

- Python 3.11
- transformers==4.28.1
- PyTorch
- restaurant-model/ directory (pre-trained model)
- place pytorch_model.bin (https://drive.google.com/file/d/1UMXelrj96fUBpnnhaQgRDdmXQ3-Yc-KH/view?usp=sharing) in restaurant-model/ 

## Usage

To use the pre-trained model, run the following command:

```python test.py -i 'how many 5 star restaurants are there in my area'```

The output will display the entities found in the input text, along with their entity group:

```
Entity Group : Rating, Word :  5 star
Entity Group : Location, Word :  in my area
```

## Training a Model

To train a NER model using your own dataset, you can modify the train.sh script. Here's an overview of the steps involved:

1. Prepare the dataset
2. Tokenize the dataset
3. Define the model
4. Train the model
5. Evaluate the model

The resulting model can then be saved and used for inference.

## Acknowledgements

This project uses the restaurant dataset from the MIT Conversational Modeling Toolkit, which is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.