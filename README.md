# Locally Ran PHI-3 mini 128K application

This application is a locally ran chatbot using a microsoft PHI-3 mini SLM. It includes a frontend using Pyside6, a backend using a ONNX PHI-3 model, and finetuning using Olive.

## Application
Breakdown of the application side.

### Frontend
Pyside6 GUI that calls in the generation method from the back.py file. The generate function does all the work. Everything else can be modified. 

### Backend
ONNX runtime and ONNX AI is sued to run a loop that takes in user input and combines it with past responses for the RAG. Sends each token back to GUI as generated. 

Not included in model folder due to size:
- ONNX Model File Weights
- ONNX Data File Weights

You can get the full pretrained model from [here](https://huggingface.co/microsoft/Phi-3-mini-128k-instruct-onnx/tree/main/cpu_and_mobile/cpu-int4-rtn-block-32-acc-level-4) or run finetuning and one will be created for use. 

## Finetuning
Use Micorsofts Olive to finetune the model on a custom dataset. The template is included.

Does the following:
- Finetune model on custom dataset using LoRA
- Convert model to ONNX model and adds new weights from LoRA
- Optimize ONNX model
