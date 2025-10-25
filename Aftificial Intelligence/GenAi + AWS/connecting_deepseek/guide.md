# Get Started with Generative AI

Generative AI is a type of artificial intelligence that can create new content and ideas, including conversations, stories, images, videos, and music. Like all artificial intelligence, generative AI is powered by machine learning models—very large models that are pre-trained on vast amounts of data and commonly referred to as foundation models (FMs). Apart from content creation, generative AI is also used to improve the quality of digital images, edit video, build prototypes quickly for manufacturing, augment data with synthetic datasets, and more.

## Using DeepSeek models 

---
This demo notebook shows how to interact with a deployed DeepSeek model endpoint on Amazon SageMaker AI by using the SageMaker Python SDK for text generation. DeepSeek models are known for their strong performance, particularly in coding and reasoning tasks. We show several example prompt engineering use cases, including code generation, question answering, and controlled model output.

Note: This notebook assumes you've already deployed a DeepSeek model to a SageMaker endpoint. You connect to this existing endpoint.
---

### Model details

---
DeepSeek LLM is a family of models developed by DeepSeek AI. The models come in various sizes and are trained on large datasets, with a significant portion dedicated to code, making them adept at programming-related tasks. 

This notebook focuses on interacting with a predeployed endpoint. For details on the specific DeepSeek model version, training data, and potential limitations (such as language support or inherent biases), refer to the model's documentation or the SageMaker JumpStart page used for its deployment.

DeepSeek models often include the following characteristics:
- Provide strong coding and mathematical reasoning capabilities
- Available in base and instruction-tuned/chat variants
- Trained on a diverse datasets, including web text and code

DeepSeek models include the following limitations:
- Like most large language models (LLMs), DeepSeek models can inherit biases from their training data. Use guardrails and appropriate precautions for production use.
- Performance can vary across different languages or highly specialized domains not well-represented in the training data.

---