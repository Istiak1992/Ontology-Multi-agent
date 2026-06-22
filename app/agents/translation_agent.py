from app.models.model_loader import (
    tokenizer,
    translation_model,
    device
)

import torch


class TranslationAgent:

    def execute(self, text, source_lang, target_lang):

        tokenizer.src_lang = source_lang

        inputs = tokenizer(
            text,
            return_tensors="pt"
        ).to(device)

        forced_bos_token_id = tokenizer.convert_tokens_to_ids(
            target_lang
        )

        with torch.no_grad():
            outputs = translation_model.generate(
                **inputs,
                forced_bos_token_id=forced_bos_token_id,
                max_length=256
            )

        return tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )