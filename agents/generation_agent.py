import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class GenerationAgent:
    def __init__(self, model="gpt-4"):
        self.model = model

    def generate_doc(self, structured_prompt):
        try:
            print("[GenerationAgent] Dökümantasyon oluşturuluyor...\n")

            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Sen profesyonel bir dökümantasyon oluşturucusun."},
                    {"role": "user", "content": structured_prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )

            content = response.choices[0].message.content
            return {
                "generated_doc": content,
                "raw_response": response
            }

        except Exception as e:
            print("bir hata oluştu", e)  
            return None

# test amaçlı
if __name__ == "__main__":
    sample_prompt = """
    - Başlık: Yapay Zeka Tabanlı Müşteri Hizmetleri
    - Tür: Teknik Belge
    - Amaç: Bir müşteri hizmetleri chatbot sisteminin dökümantasyonu
    """
    agent = GenerationAgent()
    result = agent.generate_doc(sample_prompt)
    print("\n--- Oluşturulan Dökümantasyon ---\n")
    print(result["generated_doc"])