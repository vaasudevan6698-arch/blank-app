import streamlit as st

st.set_page_config(
    page_title="Auriga Capital Inc.",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

        :root {
            --bg: #0B0F14;
            --panel: #11161D;
            --border: #1E2630;
            --text: #E6EDF3;
            --text-secondary: #8B98A5;
            --accent: #2F81F7;
            --light-bg: #F7F9FC;
            --light-panel: #FFFFFF;
            --light-border: #E1E6ED;
            --light-text: #0B0F14;
        }

        .stApp {
            background: var(--bg);
            color: var(--text);
            font-family: 'Inter', 'Segoe UI', sans-serif;
        }

        .main .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }

        h1, h2, h3 { color: var(--text); letter-spacing: -0.02em; }
        h1 { font-size: clamp(36px, 4vw, 42px); font-weight: 600; line-height: 1.2; }
        h2 { font-size: clamp(24px, 3vw, 28px); font-weight: 600; }
        h3 { font-size: clamp(18px, 2.5vw, 20px); font-weight: 500; }
        p, li, div { font-size: 15px; line-height: 1.7; color: var(--text-secondary); }
        small { font-size: 12px; }

        .section {
            background: color-mix(in srgb, var(--panel) 92%, transparent);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 24px;
            margin: 16px 0;
            opacity: 0;
            transform: translateY(12px);
            animation: fadeInUp 260ms ease forwards;
        }

        .hero { margin-top: 8px; padding: 32px; }

        .strip {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px;
            margin: 16px 0;
        }

        .pill {
            border: 1px solid var(--border);
            background: #0D131B;
            padding: 8px 12px;
            border-radius: 999px;
            font-size: 12px;
            color: var(--text-secondary);
            text-align: center;
        }

        .card {
            background: #0F141C;
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 20px;
            height: 100%;
            transition: all 240ms ease;
        }

        .card:hover {
            transform: translateY(-2px);
            border-color: var(--accent);
            box-shadow: 0 8px 20px rgba(47,129,247,0.12);
        }

        .mono { font-family: 'JetBrains Mono', monospace; color: var(--text); font-size: 14px; }

        .timeline { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }
        .timeline-step {
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 14px;
            background: #0D1219;
            text-align: center;
        }

        @media (max-width: 900px) {
            .strip, .timeline { grid-template-columns: 1fr; }
        }

        @keyframes fadeInUp {
            to { opacity: 1; transform: translateY(0); }
        }

        .network-bg {
            position: fixed;
            inset: 0;
            z-index: 0;
            opacity: 0.09;
            pointer-events: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.components.v1.html(
    """
    <canvas id="network" class="network-bg"></canvas>
    <script>
      const canvas = document.getElementById('network');
      const ctx = canvas.getContext('2d');
      let w, h, nodes;
      const N = 55;
      function resize(){ w = canvas.width = window.innerWidth; h = canvas.height = window.innerHeight; }
      function init(){
        nodes = Array.from({length:N},()=>({
          x: Math.random()*w, y: Math.random()*h,
          vx: (Math.random()-0.5)*0.2, vy: (Math.random()-0.5)*0.2
        }));
      }
      function draw(){
        ctx.clearRect(0,0,w,h);
        for (let i=0;i<N;i++){
          const a = nodes[i];
          a.x += a.vx; a.y += a.vy;
          if (a.x<0||a.x>w) a.vx*=-1;
          if (a.y<0||a.y>h) a.vy*=-1;
          ctx.fillStyle = '#2F81F7';
          ctx.beginPath(); ctx.arc(a.x,a.y,1.4,0,Math.PI*2); ctx.fill();
          for (let j=i+1;j<N;j++){
            const b = nodes[j];
            const dx=a.x-b.x, dy=a.y-b.y, d=Math.hypot(dx,dy);
            if (d<120){
              ctx.strokeStyle = `rgba(139,152,165,${(1-d/120)*0.35})`;
              ctx.lineWidth = 0.6;
              ctx.beginPath(); ctx.moveTo(a.x,a.y); ctx.lineTo(b.x,b.y); ctx.stroke();
            }
          }
        }
        requestAnimationFrame(draw);
      }
      resize(); init(); draw();
      window.addEventListener('resize', ()=>{resize(); init();});
    </script>
    """,
    height=0,
)

st.markdown('<div class="section hero">', unsafe_allow_html=True)
st.markdown("# Institutional-Grade Capital Management & Market Intelligence")
st.write("We help serious investors manage and grow capital using structured systems and controlled risk methods.")
st.markdown(
    """
    <div class="strip">
      <div class="pill">Not a retail advisory</div>
      <div class="pill">Not a signal-selling platform</div>
      <div class="pill">Not open for mass participation</div>
    </div>
    """,
    unsafe_allow_html=True,
)
cta1, cta2 = st.columns(2)
cta1.button("Request Private Access (Capital Vertical)", use_container_width=True)
cta2.button("Apply for Intelligence Access (Intel Vertical)", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("## What We Do")
st.write("Auriga Capital works with serious investors who want disciplined and structured participation in the stock market. We focus on managing risk first, then returns.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("## Our Two Verticals")
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Capital Management (UHNI / HNI)")
    st.write("We manage capital using structured strategies designed to control losses and improve consistency.")
    st.markdown("- Focus on capital protection\n- Controlled drawdowns\n- Structured decision-making\n- Limited participation model")
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Intelligence & Stewardship")
    st.write("We provide high-quality market insights and structured thinking for serious traders and investors.")
    st.markdown("- Not tips or signals\n- Not retail advice\n- Built for experienced participants\n- Focus on clarity and decision-making")
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("## Proprietary Risk Intelligence System")
st.write("Our process is supported by a structured risk intelligence system developed with CapIntelX Pvt Ltd.")
st.markdown("- Helps control risk\n- Supports decision-making\n- Tracks market scenarios\n- Improves discipline")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("## Restricted Access Model")
st.write("We do not offer open subscriptions. Access is granted only after a qualification process.")
st.markdown(
    """
    <div class="timeline">
      <div class="timeline-step"><div class="mono">01</div>Submit Qualification</div>
      <div class="timeline-step"><div class="mono">02</div>Internal Review</div>
      <div class="timeline-step"><div class="mono">03</div>Interaction / Screening</div>
      <div class="timeline-step"><div class="mono">04</div>Controlled Onboarding</div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("## Qualification Form")
with st.form("qualification_form"):
    capital_range = st.selectbox("Capital Range", ["Below ₹50L", "₹50L - ₹1Cr", "₹1Cr+"])
    exp = st.selectbox("Experience Level", ["Intermediate", "Advanced", "Institutional/Professional"])
    objective = st.text_area("Objective")
    submitted = st.form_submit_button("Submit Qualification")

if submitted:
    path = "Capital Path" if capital_range != "Below ₹50L" else "Intelligence Path"
    st.success(f"Preliminary route: {path}. Our team will contact you after internal review.")

st.caption("Routing logic: ₹50L+ → Capital Path | Below ₹50L → Intelligence Path")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("## Legal & Compliance")
st.write(
    "In alignment with a structured engagement model and applicable Securities and Exchange Board of India (SEBI) norms, "
    "Auriga Capital maintains a controlled, non-public participation process. Investments involve risk. No guaranteed returns "
    "are offered. No public solicitation is made. Services are provided through structured engagement. Proprietary systems and "
    "methods remain confidential."
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("## Built on Discipline, Not Speculation")
st.write("We focus on how capital behaves under risk, not just returns. Our approach is structured, controlled, and execution-driven.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
left, right = st.columns(2)
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### For serious capital allocation")
    st.button("Request Private Mandate Discussion", key="final_capital", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### For structured market insights")
    st.button("Apply for Intelligence Access", key="final_intel", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
