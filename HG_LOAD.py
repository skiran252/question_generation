from transformers import AutoModel,AutoTokenizer

model = AutoModel.from_pretrained("t5-base-qg-hl")
tokenizer = AutoTokenizer.from_pretrained("t5_qg_tokenizer")

model.save_pretrained("T5_MOCHA_2")
tokenizer.save_pretrained("T5_MOCHA_2")
