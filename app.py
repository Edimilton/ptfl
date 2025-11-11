import streamlit as st

# configuracao
st.set_page_config(
    page_title="Portfólio - Edimilton Santana",
    page_icon="",
    layout="wide"
)

# estilo
CUSTOM_CSS = """
<style>
/* Deixa o fundo mais clean */
main.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

/* Cards */
.card {
    padding: 1rem 1.2rem;
    border-radius: 0.8rem;
    border: 1px solid rgba(200,200,200,0.35);
    margin-bottom: 0.6rem;
    background-color: #0e1117;
}
.card h4 {
    margin-bottom: 0.2rem;
}
.pill {
    display: inline-block;
    padding: 0.12rem 0.6rem;
    margin-right: 0.25rem;
    border-radius: 999px;
    font-size: 0.7rem;
    background-color: rgba(144,202,249,0.1);
    border: 1px solid rgba(144,202,249,0.4);
}
.section-title {
    font-size: 1.25rem;
    font-weight: 600;
    margin: 1.2rem 0 0.5rem 0;
}
.muted {
    color: #9ca3af;
    font-size: 0.85rem;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# sidebar
with st.sidebar:

    st.image("foto.png", width='stretch')
    st.markdown("### Sobre mim")
    st.write(
        "Motivado por transformar ideias em soluções que realmente fazem a diferença. Estudo Engenharia de Computação e me encontrei no mundo dos dados e da inteligência artificial. Gosto de entender como as coisas funcionam por dentro e usar essas tecnologias pra resolver problemas. Algo que de fato me inspira é ver o impacto prático daquilo que construo e ter a felicidade de trabalhar e aprender com pessoas excepcionais, explorando formas criativas de aplicar essas tecnologias em projetos reais."
    )

    st.markdown("### Localização")
    st.write("Sergipe, Brasil")

    st.markdown("### Contato")
    st.write("edimiltonsantanaferreira@gmail.com")

    st.markdown("### LinkedIn")
    st.write("[linkedin.com/in/edimilton-santana-272267211](https://www.linkedin.com/in/edimilton-santana-272267211)")

    st.markdown("---")
    st.markdown("### Principais Competências")
    st.write(
        "- Engenharia de Machine Learning\n"
        "- Edge IA\n"
        "- Visão Computacional (YOLO, TensorFlow, PyTorch)\n"
        "- Ciência de Dados & Modelagem Preditiva\n"
        "- Dashboards & BI \n"
        "- Desenvolvimento Web (Django, Next.js)\n"
        "- Integração com APIs & IoT"
    )

    st.markdown("---")
    st.markdown("### Tech Stack")
    st.write(
        "Python, Pandas, PyTorch, TensorFlow, YOLO\n"
        "Scikit-Learn, Matplotlib, NumPy\n"
        "SQL, Power BI, M/Power Query\n"
        "AWS, C, IoT, Raspberry Pi\n"
        "Git/GitHub, Docker"
    )

# ----------------- CABEÇALHO -----------------
col1, col2 = st.columns([3, 2])

with col1:
    st.title("Edimilton Santana")
    st.subheader("Engenheiro de Machine Learning | Pesquisador | Cientista de Dados")
    st.markdown(
        """
        Atuo na criação de soluções que conectam dados, IA e dispositivos de borda para resolver 
        problemas reais em cenários como agricultura, saúde, marketing e segurança.
        """
    )

with col2:
    st.markdown("#### Em resumo")
    st.markdown(
        """
        - Experiência com projetos reais em produção  
        - Atuação em pesquisa aplicada (PIBIC)  
        - Participação ativa em comunidade acadêmica e eventos  
        - Forte foco em arquiteturas escaláveis, privacidade e boas práticas
        """
    )

st.markdown("---")

# tabela principal
tabs = st.tabs([
    "Experiência",
    "Projetos",
    "Palestras & Eventos",
    "Formação & Pesquisa"
])

# experencia
with tabs[0]:
    st.markdown('<div class="section-title">Experiência Profissional</div>', unsafe_allow_html=True)

    with st.container():
        st.markdown(
            """
            <div class="card">
                <h4>Engenheiro de Machine Learning – IA Grow Soluções</h4>
                <div class="muted">Set 2025 - Atual</div>
                <p>
                Desenvolvimento de solução de <b>visão computacional embarcada</b> para monitoramento de pragas em campo:
                treinamento de modelos YOLO com datasets próprios, otimização para borda, integração com banco de dados,
                automação em Python, telemetria, e projeto de hardware (câmera, motor de passo, alimentação solar).
                </p>
                <span class="pill">Edge IA</span>
                <span class="pill">YOLO</span>
                <span class="pill">Raspberry Pi</span>
                <span class="pill">Python</span>
                <span class="pill">Visão Computacional</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with st.container():
        st.markdown(
            """
            <div class="card">
                <h4>Pesquisador PIBIC FAPITEC – Reconhecimento Facial, IoT e IA</h4>
                <div class="muted">Jan 2025 - Atual • Universidade Federal de Sergipe</div>
                <p>
                Pesquisa aplicada sobre uso responsável de reconhecimento facial em ambientes privados:
                requisitos legais, arquitetura em <b>edge/fog</b>, anonimização, criptografia e protótipo em Raspberry Pi 5
                com operação em tempo quase real.
                </p>
                <span class="pill">Pesquisa Aplicada</span>
                <span class="pill">Privacidade & LGPD</span>
                <span class="pill">Edge Computing</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with st.container():
        st.markdown(
            """
            <div class="card">
                <h4>Diretor Administrativo & Cofundador – LADATA</h4>
                <div class="muted">Jul 2023 - Atual</div>
                <p>
                Atuação na liderança de projetos de Ciência de Dados e IA, organização de eventos,
                formação de comunidade técnica e conexão entre universidade, mercado e impacto social.
                </p>
                <span class="pill">Liderança</span>
                <span class="pill">Gestão de Projetos</span>
                <span class="pill">Comunidade</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with st.container():
        st.markdown(
            """
            <div class="card">
                <h4>Estagiário de TI – Construtora Stanza</h4>
                <div class="muted">Abr 2023 - Jan 2025</div>
                <p>
                Desenvolvimento de crawlers, automações em Python, modelagem de dados,
                criação de dashboards em Power BI, integrações com APIs e Pipefy, e apoio em adequação à LGPD.
                </p>
                <span class="pill">Python</span>
                <span class="pill">Power BI</span>
                <span class="pill">ETL</span>
                <span class="pill">APIs</span>
                <span class="pill">LGPD</span>
            </div>
            """,
            unsafe_allow_html=True
        )

    with st.container():
        st.markdown(
            """
            <div class="card">
                <h4>Pesquisador PIBIC CNPq – Classificação de Sinais de Miografia</h4>
                <div class="muted">Set 2021 - Ago 2022 • Universidade Federal de Sergipe</div>
                <p>
                Pré-processamento de sinais, treinamento de redes neurais para classificação de movimentos,
                integração com simulação de mão biônica e construção de pipelines reprodutíveis em Python.
                </p>
                <span class="pill">Deep Learning</span>
                <span class="pill">Sinais Biomédicos</span>
                <span class="pill">TensorFlow</span>
            </div>
            """,
            unsafe_allow_html=True
        )

# projetos
with tabs[1]:
    st.markdown('<div class="section-title">Projetos em Destaque</div>', unsafe_allow_html=True)

    # masu
    st.markdown(
        """
        <div class="card">
            <h4>MASU – Plataforma de Saúde com Foco em Autocuidado e IA (Registro de Software)</h4>
            <div class="muted">2025</div>
            <p>
            Atuação no desenvolvimento completo de uma plataforma de autocuidado focada na prevenção do câncer de mama,
            com lembretes dinâmicos, tutoriais interativos, check-ins diários e assistente virtual com IA.
            Participação reconhecida em registro oficial de software, com percentual sobre o produto.
            </p>
            <p class="muted">
            Tecnologias: React Native, Next.js, TypeScript, Python, AWS, TensorFlow, Prisma, Expo, Firebase, Swagger, Git/GitHub.
            </p>
            <span class="pill">IA em Saúde</span>
            <span class="pill">Full Stack</span>
            <span class="pill">Mobile & Web</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # plataforma de doacoes
    st.markdown(
        """
        <div class="card">
            <h4>Plataforma de Doações para Comunidades Carentes</h4>
            <div class="muted">2025</div>
            <p>
            Plataforma web para conectar doadores a campanhas oficiais de prefeituras, ONGs e instituições,
            com foco em transparência, rastreio de doações e relatórios gerenciais.
            </p>
            <p class="muted">
            Tecnologias: Django, HTML, CSS, JavaScript, Bootstrap, Git/GitHub.
            </p>
            <span class="pill">Impacto Social</span>
            <span class="pill">Transparência</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # incorpora
    st.markdown(
        """
        <div class="card">
            <h4>Incorpora – Sistema de Business Intelligence</h4>
            <div class="muted">2023</div>
            <p>
            Colaboração na modelagem e desenvolvimento de plataforma BI para visualização de dados corporativos
            e dashboards financeiros, integrada ao Pipefy e Power BI.
            </p>
            <p class="muted">
            Tecnologias: Python (Django), HTML, CSS, JavaScript, Power BI, SQL, M, Power Query, Git/GitHub.
            </p>
            <span class="pill">BI</span>
            <span class="pill">Data Visualization</span>
            <span class="pill">Integrações</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # stanza bi
    st.markdown(
        """
        <div class="card">
            <h4>Stanza BI (SERDATA) – Sistema de BI para Marketing</h4>
            <div class="muted">2024</div>
            <p>
            Desenvolvimento de pipelines de dados e dashboards em Power BI para análise de marketing, conectando CRM,
            automação e vendas, com monitoramento de conversão, ROI e desempenho de campanhas.
            </p>
            <p class="muted">
            Tecnologias: Python, Power BI, SQL, M, Power Query.
            </p>
            <span class="pill">Marketing Analytics</span>
            <span class="pill">KPIs</span>
            <span class="pill">Power BI</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# palestras
with tabs[2]:
    st.markdown('<div class="section-title">Palestras & Participações</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="card">
            <h4>Campus Party Brasil – Aprendendo análise de dados com Stardew Valley</h4>
            <div class="muted">Palestrante • 26/11/2025</div>
            <p>
            Palestra prática utilizando o universo de Stardew Valley para introduzir conceitos de engenharia de dados, análise de dados e aprendizado de máquina
            com raciocínio orientado a negócios.
            </p>
            <span class="pill">Educação</span>
            <span class="pill">Data Literacy</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("#### Atividades de Extensão")

    # IV Mostra
    st.markdown(
        """
        <div class="card">
            <h4>IV Mostra de Produtos Desenvolvidos em Práticas Orientadas em Computação - DCOMP</h4>
            <div class="muted">Ministrante • 01/04/2025 - 03/04/2025</div>
            <p>Atuação apresentando soluções desenvolvidas e apoiando atividades acadêmicas do DCOMP/UFS.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # X SEMAC
    st.markdown(
        """
        <div class="card">
            <h4>X SEMAC - CCET - Guia LADATA de Ferramentas para Ciência de Dados</h4>
            <div class="muted">Ministrante • 13/12/2024</div>
            <p>Atuação apresentando soluções na curadoria de ferramentas utilizadas na área de Dados.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # IX SEMAC - Dados, onde vivem?
    st.markdown(
        """
        <div class="card">
            <h4>IX SEMAC - "Dados, onde vivem? Desbravando o Mundo dos Dados Abertos"</h4>
            <div class="muted">Ministrante • 01/12/2023</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # IX SEMAC - Do DCOMP para a UFS
    st.markdown(
        """
        <div class="card">
            <h4>IX SEMAC - "Interdisciplinaridade através da Ciência de Dados"</h4>
            <div class="muted">Ministrante • 29/11/2023</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # wv888-2021
    st.markdown(
        """
        <div class="card">
            <h4>31º Encontro de Iniciação Científica (EV888-2021)</h4>
            <div class="muted"> Palestrante • 10/11/2021</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ----------------- FORMAÇÃO & PESQUISA -----------------
with tabs[3]:
    st.markdown('<div class="section-title">Formação Acadêmica</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="card">
            <h4>Bacharelado em Engenharia de Computação</h4>
            <div class="muted">Universidade Federal de Sergipe • 2020 - 2025</div>
            <p>
            Formação orientada à computação aplicada, sistemas embarcados, inteligência artificial e desenvolvimento de soluções tecnológicas completas.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("#### Linhas de Interesse & Pesquisa")
    st.markdown(
        """
        - Edge IA e visão computacional em dispositivos embarcados  
        - Privacidade, LGPD e arquiteturas distribuídas (edge/fog/cloud)  
        - Sistemas de apoio à decisão baseados em dados  
        - Aplicações de IA em saúde, agro e cidades inteligentes   
        """
    )

    st.markdown("#### Certificações")
    st.markdown(
        """  
        - Unsupervised learning, recommendations, reinforcement learning - Stanford Online
        - Advanced learning algorithms - Stanford Online
        - Machine Learning Training - BairesDev
        - Supervised Machine Learning: Regression and Classification - Stanford Online
        - Python Data Analytics - Squadio
        - Artificial Intelligence HCIA AI - Huawei 
        - Capacitação em Inteligência Artificial - Instituto Federal de Educação, Ciência e Tecnologia de Alagoas
        """
    )

# rodape
st.markdown("---")

