
from agents.input_agent import InputAgent
from agents.generation_agent import GenerationAgent
from agents.evaluation_agent import EvaluationAgent
from agents.feedback_agent import FeedbackAgent
from word_exporter import WordExporter

input_agent = InputAgent()
gen_agent = GenerationAgent()
eval_agent = EvaluationAgent()
feedback_agent = FeedbackAgent()
exporter = WordExporter()

def run_workflow():
    print("⏳ Dökümantasyon oluşturma süreci başlatıldı")

    user_input = input("Ne tür bir dökümantasyon oluşturmak istersiniz?: ")
    input_result = input_agent.process_input(user_input)

    while True:
        gen_result = gen_agent.generate_doc(input_result["structured_prompt"])
        generated_doc = gen_result["generated_doc"]

        evaluation = eval_agent.evaluate_doc(generated_doc)

        decision = feedback_agent.present_to_user(generated_doc, evaluation)

        if decision == "accept":
            title_line = user_input.strip().split(".")[0][:50] or "Otomatik_Dokumantasyon"
            exporter.export(title_line, generated_doc)
            break
        else:
            print("\n Süreç yeniden başlatılıyor...\n")

if __name__ == "__main__":
    run_workflow()
