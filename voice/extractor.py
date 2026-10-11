import torch

from speechbrain.inference.speaker import EncoderClassifier
from speechbrain.utils.fetching import LocalStrategy

# A function to plug in the ECAPA-TDNN extractor
def load_extractor():
    # EncoderClassifier creates a model based on a configuration and ready weights
    extractor = EncoderClassifier.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="models/ecapa", run_opts={"device": "cpu"}, local_strategy=LocalStrategy.COPY,)

    extractor.eval()

    # Here we go through the network's parameters and turns off their gradient calculations
    for parameter in extractor.parameters():
        parameter.requires_grad_(False)

    return extractor

# A function to extract the embeddings 
def extract_embeddings(extractor, batch):
    # It runs a block without tracking the calculations required for backpropagation
    with torch.inference_mode():
        embeddings = extractor.encode_batch(batch)

    return embeddings.squeeze(1)