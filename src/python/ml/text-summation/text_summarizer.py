# text_summarizer.py

import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import sys
import traceback

def summarize_text(input_text):
    try:
        # Encode the input text and move tensors to the CPU device
        inputs = tokenizer(
            "summarize: " + input_text,
            return_tensors="pt",
            max_length=1024,
            truncation=True
        ).to(device)

        # Generate the summary
        with torch.no_grad():
            summary_ids = model.generate(
                inputs['input_ids'],
                attention_mask=inputs['attention_mask'],
                max_length=150,
                num_beams=4,    
                early_stopping=True
            )

        # Decode and return the summary
        summary = tokenizer.decode(
            summary_ids[0],
            skip_special_tokens=True
        )

        return summary
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    try:
        # Force the model to use CPU
        device = torch.device('cpu')

        # Load the tokenizer and model from the local directory
        local_model_dir = "./local_text_summarizer_model"
        tokenizer = AutoTokenizer.from_pretrained(local_model_dir)
        model = AutoModelForSeq2SeqLM.from_pretrained(local_model_dir)
        model.to(device)  # Move the model to CPU

        # Read input text from stdin or use a sample text
        # input_text = """
        # The sea, a vast and seemingly boundless expanse of water, covers over 70% of the Earth's surface, playing an integral role in shaping the planet's climate, geography, and ecosystems. It has been a source of fascination, sustenance, and mystery for humanity since the dawn of civilization. From the tranquil, glassy waters of a calm morning to the roaring tempests of stormy seas, the ocean's moods are as diverse and unpredictable as the creatures that inhabit it. The sea is not just a physical entity; it has a profound cultural and emotional significance. It has inspired countless myths, legends, and works of art throughout history, symbolizing both the unknown and the infinite possibilities of exploration.

        # Beneath the surface, the ocean is a realm teeming with life. It houses an extraordinary array of ecosystems, from the sunlit coral reefs bustling with vibrant marine life to the mysterious, pitch-black depths of the abyss, where creatures have adapted to survive under extreme pressure and darkness. These ecosystems are crucial to the health of the planet. The sea produces more than half of the world’s oxygen and absorbs a significant portion of the carbon dioxide emitted by human activities, helping to mitigate the effects of climate change. The ocean’s currents regulate weather patterns and distribute heat around the globe, ensuring that climates remain habitable. Without the sea, life on Earth would be impossible.

        # The sea is also vital to human economies. Fishing, shipping, and tourism industries rely heavily on healthy marine environments. For centuries, the oceans have been the highways of global trade, connecting distant lands and cultures. Today, millions of people around the world depend on the ocean for their livelihoods, whether through fishing, transportation, or recreational activities. Yet, despite its importance, the sea is under threat from human activities. Pollution, overfishing, and climate change have placed immense pressure on marine ecosystems. Plastic waste, for instance, has infiltrated even the most remote parts of the ocean, posing a deadly threat to marine animals that mistake it for food.

        # Overfishing, driven by the global demand for seafood, has led to the depletion of many fish stocks, threatening the balance of marine ecosystems. Furthermore, rising sea temperatures due to climate change are causing coral bleaching, which damages the delicate coral reefs that support vast marine biodiversity. The acidification of the ocean, a result of increased carbon dioxide absorption, is weakening the shells of marine organisms like mollusks and disrupting the food chain. Coastal communities, particularly those in low-lying areas, are also vulnerable to rising sea levels and more frequent extreme weather events caused by global warming.

        # Despite these challenges, efforts are being made to protect the sea and its invaluable resources. International agreements, marine protected areas, and sustainable fishing practices are helping to conserve marine biodiversity and promote the responsible use of ocean resources. Moreover, growing public awareness of the sea’s critical role in supporting life on Earth is encouraging more individuals and organizations to take action. The sea, with its beauty, power, and mystery, will always remain a source of wonder, but it is also a fragile environment that requires careful stewardship to ensure its survival for future generations.
        # """

        input_text = sys.stdin.read()
        print('IN PYTHON', file=sys.stderr)  # Output to stderr for visibility

        # Generate the summary and print the result
        result = summarize_text(input_text)
        print(result)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
