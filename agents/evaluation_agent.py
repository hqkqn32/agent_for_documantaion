import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class EvaluationAgent:
    def __init__(self, model="gpt-4"):
        self.model = model

    def evaluate_doc(self, generated_doc):
        evaluation_prompt = f"""
        Aşağıdaki dökümantasyonu dikkatlice değerlendir:

        {generated_doc}

        Lütfen şu maddelere göre analiz yap:
        1. Anlaşılabilirlik
        2. Tutarlılık ve yapı
        3. Eksik bilgi var mı?
        4. Dil ve yazım kalitesi
        5. Geliştirme önerileri

        Yanıtı maddelendirilmiş şekilde döndür.
        """

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Sen deneyimli bir teknik editörsün."},
                    {"role": "user", "content": evaluation_prompt}
                ],
                temperature=0.3,
                max_tokens=800
            )

            evaluation = response.choices[0].message.content
            return evaluation

        except Exception as e:
            print("[EvaluationAgent] Hata oluştu:", e)
            return None

# Test amaçlı
if __name__ == "__main__":
    dummy_text = """
    Bu belge, bir yapay zeka destekli müşteri hizmetleri sisteminin nasıl çalıştığını açıklar.
    İçeriğinde sistem mimarisi, kullanıcı senaryoları ve API kullanımı yer almaktadır.
    """
    agent = EvaluationAgent()
    feedback = agent.evaluate_doc(dummy_text)
    print("\n--- Değerlendirme ---\n")
    print(feedback)