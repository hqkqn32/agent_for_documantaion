
import streamlit as st
from agents.input_agent import InputAgent
from agents.generation_agent import GenerationAgent
from agents.evaluation_agent import EvaluationAgent
from word_exporter import WordExporter

st.set_page_config(page_title="AutoDoc Architect", layout="centered")

st.title(" AutoDoc Architect")
st.markdown("Yapay zeka ile dökümantasyon üret! ")

user_input = st.text_area("Dökümantasyon talebinizi yazın:", placeholder="Örn: Bir yapay zeka destekli müşteri hizmetleri sisteminin teknik dökümantasyonunu oluştur...")

if st.button("Dökümantasyon Oluştur") and user_input:
    with st.spinner(" Agent'lar çalışıyor..."):
        # Agent'ları başlat
        input_agent = InputAgent()
        gen_agent = GenerationAgent()
        eval_agent = EvaluationAgent()
        exporter = WordExporter()

        input_result = input_agent.process_input(user_input)
        gen_result = gen_agent.generate_doc(input_result["structured_prompt"])
        generated_doc = gen_result["generated_doc"]
        evaluation = eval_agent.evaluate_doc(generated_doc)

    st.subheader(" Oluşturulan Dökümantasyon")
    st.code(generated_doc, language="markdown")

    st.subheader(" Değerlendirme")
    st.markdown(evaluation)

    col1, col2 = st.columns(2)
    with col1:
        if st.button(" Beğendim, Word olarak indir"):
            title_line = user_input.strip().split(".")[0][:50] or "Otomatik_Dokumantasyon"
            filepath = exporter.export(title_line, generated_doc)
            with open(filepath, "rb") as f:
                st.download_button(
                    label=" Word Dosyasını İndir",
                    data=f,
                    file_name=filepath.split("/")[-1],
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
    with col2:
        if st.button(" Beğenmedim, yeniden üret"):
            st.warning("Lütfen sayfayı yenileyerek yeniden başlatın.")
