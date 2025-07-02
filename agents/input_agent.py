# agents/input_agent.py
# Bu agent, kullanıcıdan dökümantasyon isteğini alır ve yapılandırılmış bir forma dönüştürür.
# Bilerek bazı yerlerde küçük stil ve yazım hataları bırakılmıştır (insan eliyle yazılmış hissi vermek için).

import os
from dotenv import load_dotenv

load_dotenv()

# Kullanıcıdan gelen girdiyi işleyen sınıf
class InputAgent:
    def __init__(self):
        self.prompt_template = """
        Aşağıdaki kullanıcı girdisine göre bir dökümantasyon isteğini yapılandır:
        Girdi: "{user_input}"
        
        Yapılandırılmış çıktı şu şekilde olmalı:
        - Başlık: (ne hakkında olduğu)
        - Tür: (örn: kullanım kılavuzu, teknik belge, proje raporu)
        - Amaç: (neden bu belge oluşturuluyor?)
        """

    def process_input(self, user_input):
        if not user_input:
            raise ValueError("Girdi boş olamaz. lütfen bir şey yaz")

        prompt = self.prompt_template.format(user_input=user_input)

        # Basit yapılandırılmış çıktı dönüyor şimdilik
        # ileride GPT ile enrich edebiliriz
        return {
            "raw_input": user_input,
            "structured_prompt": prompt
        }

# Test amaçlı
if __name__ == "__main__":
    agent = InputAgent()
    input_text = input("Ne tür bir dökümantasyon istersiniz?: ")
    result = agent.process_input(input_text)
    print("\nYapılandırılmış Çıktı:\n", result)
