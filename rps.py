import streamlit as st
import random
import time

# ─── PAGE CONFIG ─────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Rock · Paper · Scissors",
    page_icon="✊",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── THEMES ──────────────────────────────────────────────────────────────────

THEMES = {
    "🌌 Cosmic Purple": {
        "bg":         "#0d0015",
        "card":       "#1a0030",
        "border":     "#7c3aed",
        "primary":    "#a855f7",
        "accent":     "#818cf8",
        "win":        "#34d399",
        "lose":       "#f87171",
        "tie":        "#fbbf24",
        "text":       "#e9d5ff",
        "subtext":    "#9d7fc4",
        "btn_rock":   "linear-gradient(135deg,#7c3aed,#4f46e5)",
        "btn_paper":  "linear-gradient(135deg,#a855f7,#7c3aed)",
        "btn_sci":    "linear-gradient(135deg,#818cf8,#6366f1)",
        "glow":       "#7c3aed",
        "font":       "Orbitron",
    },
    "🔥 Inferno": {
        "bg":         "#0f0500",
        "card":       "#1c0a00",
        "border":     "#ea580c",
        "primary":    "#f97316",
        "accent":     "#fbbf24",
        "win":        "#34d399",
        "lose":       "#ef4444",
        "tie":        "#fbbf24",
        "text":       "#fef3c7",
        "subtext":    "#d97706",
        "btn_rock":   "linear-gradient(135deg,#dc2626,#b91c1c)",
        "btn_paper":  "linear-gradient(135deg,#ea580c,#c2410c)",
        "btn_sci":    "linear-gradient(135deg,#d97706,#b45309)",
        "glow":       "#f97316",
        "font":       "Bungee",
    },
    "🌊 Deep Ocean": {
        "bg":         "#00080f",
        "card":       "#001524",
        "border":     "#0369a1",
        "primary":    "#38bdf8",
        "accent":     "#22d3ee",
        "win":        "#34d399",
        "lose":       "#f87171",
        "tie":        "#a5f3fc",
        "text":       "#e0f2fe",
        "subtext":    "#7dd3fc",
        "btn_rock":   "linear-gradient(135deg,#0369a1,#075985)",
        "btn_paper":  "linear-gradient(135deg,#0891b2,#0e7490)",
        "btn_sci":    "linear-gradient(135deg,#06b6d4,#0891b2)",
        "glow":       "#38bdf8",
        "font":       "Exo 2",
    },
    "🌿 Jungle": {
        "bg":         "#010f05",
        "card":       "#021a09",
        "border":     "#16a34a",
        "primary":    "#4ade80",
        "accent":     "#86efac",
        "win":        "#34d399",
        "lose":       "#f87171",
        "tie":        "#bef264",
        "text":       "#dcfce7",
        "subtext":    "#86efac",
        "btn_rock":   "linear-gradient(135deg,#166534,#15803d)",
        "btn_paper":  "linear-gradient(135deg,#16a34a,#15803d)",
        "btn_sci":    "linear-gradient(135deg,#22c55e,#16a34a)",
        "glow":       "#4ade80",
        "font":       "Rajdhani",
    },
    "🌸 Sakura": {
        "bg":         "#0f0008",
        "card":       "#1a0014",
        "border":     "#be185d",
        "primary":    "#f472b6",
        "accent":     "#e879f9",
        "win":        "#34d399",
        "lose":       "#f87171",
        "tie":        "#f9a8d4",
        "text":       "#fce7f3",
        "subtext":    "#f9a8d4",
        "btn_rock":   "linear-gradient(135deg,#9d174d,#be185d)",
        "btn_paper":  "linear-gradient(135deg,#db2777,#be185d)",
        "btn_sci":    "linear-gradient(135deg,#ec4899,#db2777)",
        "glow":       "#f472b6",
        "font":       "Poiret One",
    },
    "⚡ Neon Storm": {
        "bg":         "#000a0f",
        "card":       "#001018",
        "border":     "#0ff",
        "primary":    "#00ffff",
        "accent":     "#faff00",
        "win":        "#39ff14",
        "lose":       "#ff3131",
        "tie":        "#faff00",
        "text":       "#e0ffff",
        "subtext":    "#67e8f9",
        "btn_rock":   "linear-gradient(135deg,#0891b2,#06b6d4)",
        "btn_paper":  "linear-gradient(135deg,#00b4d8,#0077b6)",
        "btn_sci":    "linear-gradient(135deg,#00ffff55,#0891b2)",
        "glow":       "#00ffff",
        "font":       "Share Tech Mono",
    },
    "🩸 Midnight Red": {
        "bg":         "#0a0000",
        "card":       "#150000",
        "border":     "#991b1b",
        "primary":    "#ef4444",
        "accent":     "#fca5a5",
        "win":        "#34d399",
        "lose":       "#dc2626",
        "tie":        "#fca5a5",
        "text":       "#fee2e2",
        "subtext":    "#fca5a5",
        "btn_rock":   "linear-gradient(135deg,#7f1d1d,#991b1b)",
        "btn_paper":  "linear-gradient(135deg,#991b1b,#b91c1c)",
        "btn_sci":    "linear-gradient(135deg,#b91c1c,#dc2626)",
        "glow":       "#ef4444",
        "font":       "Oswald",
    },
    "🌙 Moonlight": {
        "bg":         "#05050f",
        "card":       "#0d0d1f",
        "border":     "#4b5563",
        "primary":    "#e2e8f0",
        "accent":     "#94a3b8",
        "win":        "#34d399",
        "lose":       "#f87171",
        "tie":        "#cbd5e1",
        "text":       "#f1f5f9",
        "subtext":    "#94a3b8",
        "btn_rock":   "linear-gradient(135deg,#1e293b,#334155)",
        "btn_paper":  "linear-gradient(135deg,#334155,#475569)",
        "btn_sci":    "linear-gradient(135deg,#475569,#64748b)",
        "glow":       "#e2e8f0",
        "font":       "Josefin Sans",
    },
}

BEATS     = {"R": "S", "P": "R", "S": "P"}
BEAT_MSG  = {
    ("R","S"): "Rock crushes Scissors! 💥",
    ("P","R"): "Paper smothers Rock! 📄",
    ("S","P"): "Scissors slices Paper! ✂️",
    ("S","R"): "Rock crushes Scissors! 💥",
    ("R","P"): "Paper smothers Rock! 📄",
    ("P","S"): "Scissors slices Paper! ✂️",
}
WIN_AT = 5

# ─── SESSION STATE ────────────────────────────────────────────────────────────

def init_state():
    defaults = {
        "screen":       "hero",   # hero | theme | game
        "theme_name":   "🌌 Cosmic Purple",
        "player_score": 0,
        "cpu_score":    0,
        "history":      [],
        "streak":       0,
        "last_result":  None,  # dict with round info
        "winner":       None,  # "player" | "cpu" | None
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

T = THEMES[st.session_state.theme_name]

# ─── GLOBAL CSS ──────────────────────────────────────────────────────────────

def inject_css(t):
    font = t["font"]
    st.markdown(f"""
    <link href="https://fonts.googleapis.com/css2?family={font.replace(' ','+')}:wght@300;400;600;700;900&display=swap" rel="stylesheet">
    <style>
        /* ── Reset & Base ── */
        html, body, [data-testid="stAppViewContainer"] {{
            background: {t['bg']} !important;
            color: {t['text']} !important;
            font-family: '{font}', sans-serif !important;
        }}
        [data-testid="stAppViewContainer"] > .main {{
            background: {t['bg']} !important;
        }}
        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        footer {{ display: none !important; }}
        [data-testid="block-container"] {{
            padding: 1.5rem 1rem 3rem !important;
            max-width: 720px !important;
        }}

        /* ── Scrollbar ── */
        ::-webkit-scrollbar {{ width: 4px; }}
        ::-webkit-scrollbar-track {{ background: {t['bg']}; }}
        ::-webkit-scrollbar-thumb {{ background: {t['border']}; border-radius: 4px; }}

        /* ── Cards ── */
        .rps-card {{
            background: {t['card']};
            border: 1px solid {t['border']};
            border-radius: 16px;
            padding: 1.8rem;
            margin: 0.6rem 0;
            box-shadow: 0 0 32px {t['glow']}22;
        }}
        .rps-card-glow {{
            background: {t['card']};
            border: 1.5px solid {t['glow']};
            border-radius: 16px;
            padding: 1.8rem;
            margin: 0.6rem 0;
            box-shadow: 0 0 48px {t['glow']}44, inset 0 0 32px {t['glow']}11;
        }}

        /* ── Title ── */
        .rps-title {{
            font-family: '{font}', sans-serif;
            font-size: 2.4rem;
            font-weight: 900;
            color: {t['primary']};
            text-align: center;
            text-shadow: 0 0 32px {t['glow']};
            letter-spacing: 0.12em;
            line-height: 1.15;
            margin-bottom: 0.2rem;
        }}
        .rps-subtitle {{
            text-align: center;
            color: {t['subtext']};
            font-size: 0.95rem;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            margin-bottom: 1.2rem;
        }}

        /* ── Score display ── */
        .score-block {{
            text-align: center;
        }}
        .score-number {{
            font-size: 3.5rem;
            font-weight: 900;
            line-height: 1;
        }}
        .score-label {{
            font-size: 0.75rem;
            letter-spacing: 0.25em;
            text-transform: uppercase;
            color: {t['subtext']};
        }}
        .score-you {{ color: {t['primary']}; text-shadow: 0 0 20px {t['primary']}; }}
        .score-cpu {{ color: {t['lose']}; text-shadow: 0 0 20px {t['lose']}; }}
        .score-vs  {{ color: {t['subtext']}; font-size: 1.2rem; font-weight: 400; }}

        /* ── Pip bar ── */
        .pip-row {{ display: flex; gap: 6px; justify-content: center; margin: 6px 0; }}
        .pip-on  {{ width:18px; height:18px; border-radius:50%; background:{t['win']};
                    box-shadow:0 0 8px {t['win']}; }}
        .pip-on-lose {{ width:18px; height:18px; border-radius:50%; background:{t['lose']};
                    box-shadow:0 0 8px {t['lose']}; }}
        .pip-off {{ width:18px; height:18px; border-radius:50%; background:transparent;
                    border: 2px solid {t['border']}; opacity:0.4; }}

        /* ── Choice buttons ── */
        .choice-btn {{
            display: block;
            width: 100%;
            padding: 1.2rem 0.5rem;
            font-family: '{font}', sans-serif;
            font-size: 1.5rem;
            font-weight: 700;
            border: none;
            border-radius: 14px;
            cursor: pointer;
            transition: transform 0.15s, box-shadow 0.15s;
            letter-spacing: 0.05em;
            color: #fff;
            text-shadow: 0 2px 8px #0008;
            box-shadow: 0 4px 20px {t['glow']}33;
        }}
        .btn-rock    {{ background: {t['btn_rock']}; }}
        .btn-paper   {{ background: {t['btn_paper']}; }}
        .btn-sci     {{ background: {t['btn_sci']}; }}
        .choice-btn:hover {{
            transform: translateY(-3px) scale(1.03);
            box-shadow: 0 8px 32px {t['glow']}66;
        }}

        /* ── Result badge ── */
        .result-win  {{ color:{t['win']};  font-size:1.6rem; font-weight:900;
                        text-shadow:0 0 24px {t['win']}; text-align:center; }}
        .result-lose {{ color:{t['lose']}; font-size:1.6rem; font-weight:900;
                        text-shadow:0 0 24px {t['lose']}; text-align:center; }}
        .result-tie  {{ color:{t['tie']};  font-size:1.6rem; font-weight:900;
                        text-shadow:0 0 24px {t['tie']}; text-align:center; }}

        /* ── History dots ── */
        .hist-dot-w {{ display:inline-block; width:14px; height:14px; border-radius:50%;
                       background:{t['win']}; margin:2px; box-shadow:0 0 6px {t['win']}; }}
        .hist-dot-l {{ display:inline-block; width:14px; height:14px; border-radius:50%;
                       background:{t['lose']}; margin:2px; }}
        .hist-dot-t {{ display:inline-block; width:14px; height:14px; border-radius:50%;
                       background:{t['tie']}; margin:2px; opacity:0.7; }}

        /* ── Theme cards ── */
        .theme-card {{
            background: {t['card']};
            border: 1.5px solid {t['border']};
            border-radius: 12px;
            padding: 1rem 1.2rem;
            margin: 0.3rem 0;
            cursor: pointer;
            transition: box-shadow 0.2s;
        }}
        .theme-card:hover {{
            box-shadow: 0 0 20px {t['glow']}55;
        }}
        .theme-active {{
            border-color: {t['primary']};
            box-shadow: 0 0 20px {t['glow']}88;
        }}

        /* ── Streamlit button override ── */
        .stButton > button {{
            background: {t['btn_rock']} !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            font-family: '{font}', sans-serif !important;
            font-weight: 700 !important;
            letter-spacing: 0.05em !important;
            transition: transform 0.15s, box-shadow 0.15s !important;
            box-shadow: 0 4px 16px {t['glow']}44 !important;
        }}
        .stButton > button:hover {{
            transform: translateY(-2px) scale(1.02) !important;
            box-shadow: 0 8px 28px {t['glow']}66 !important;
            color: white !important;
        }}

        /* ── Divider ── */
        .rps-divider {{
            border: none;
            height: 1px;
            background: linear-gradient(to right, transparent, {t['border']}, transparent);
            margin: 1rem 0;
        }}

        /* ── Streak badge ── */
        .streak-win  {{ background:{t['win']}22; border:1px solid {t['win']};
                        border-radius:8px; padding:6px 16px; color:{t['win']};
                        font-weight:700; display:inline-block; font-size:0.95rem; }}
        .streak-lose {{ background:{t['lose']}22; border:1px solid {t['lose']};
                        border-radius:8px; padding:6px 16px; color:{t['lose']};
                        font-weight:700; display:inline-block; font-size:0.95rem; }}

        /* ── Winner banner ── */
        .winner-banner {{
            text-align:center;
            border-radius:20px;
            padding: 2.5rem 1rem;
            background: {t['card']};
            border: 2px solid {t['glow']};
            box-shadow: 0 0 80px {t['glow']}55;
        }}
        .winner-text {{
            font-size: 2.8rem;
            font-weight: 900;
            color: {t['win']};
            text-shadow: 0 0 40px {t['win']};
            letter-spacing: 0.1em;
        }}
        .loser-text {{
            font-size: 2.8rem;
            font-weight: 900;
            color: {t['lose']};
            text-shadow: 0 0 40px {t['lose']};
            letter-spacing: 0.1em;
        }}

        /* ── Hero specific ── */
        .hero-icon {{
            font-size: 4rem;
            text-align: center;
            filter: drop-shadow(0 0 16px {t['glow']});
        }}
        .rule-row {{
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 8px 0;
            border-bottom: 1px solid {t['border']}44;
            color: {t['text']};
            font-size: 1rem;
        }}
        .rule-icon {{ font-size: 1.4rem; min-width: 36px; text-align: center; }}
        .feature-pill {{
            display: inline-block;
            background: {t['primary']}18;
            border: 1px solid {t['primary']}55;
            border-radius: 20px;
            padding: 4px 14px;
            font-size: 0.85rem;
            color: {t['primary']};
            margin: 4px;
        }}

        /* ── Animations ── */
        @keyframes fadeIn {{
            from {{ opacity:0; transform: translateY(12px); }}
            to   {{ opacity:1; transform: translateY(0); }}
        }}
        @keyframes pulse-glow {{
            0%,100% {{ box-shadow: 0 0 32px {t['glow']}44; }}
            50%      {{ box-shadow: 0 0 64px {t['glow']}99; }}
        }}
        .anim-in  {{ animation: fadeIn 0.4s ease both; }}
        .anim-pulse {{ animation: pulse-glow 2.4s ease-in-out infinite; }}
    </style>
    """, unsafe_allow_html=True)

inject_css(T)

# ─── GAME LOGIC ──────────────────────────────────────────────────────────────

def play_round(user_choice):
    cpu = random.choice(["R","P","S"])
    if user_choice == cpu:
        outcome = "T"
        st.session_state.streak = 0
    elif BEATS[user_choice] == cpu:
        outcome = "W"
        st.session_state.player_score += 1
        s = st.session_state.streak
        st.session_state.streak = s + 1 if s >= 0 else 1
    else:
        outcome = "L"
        st.session_state.cpu_score += 1
        s = st.session_state.streak
        st.session_state.streak = s - 1 if s <= 0 else -1

    st.session_state.history.append(outcome)
    icons = {"R":"✊ Rock","P":"✋ Paper","S":"✌️ Scissors"}
    st.session_state.last_result = {
        "user": icons[user_choice],
        "cpu":  icons[cpu],
        "outcome": outcome,
        "msg": BEAT_MSG.get((user_choice, cpu), ""),
    }

    if st.session_state.player_score >= WIN_AT:
        st.session_state.winner = "player"
    elif st.session_state.cpu_score >= WIN_AT:
        st.session_state.winner = "cpu"

def reset_game():
    st.session_state.player_score = 0
    st.session_state.cpu_score    = 0
    st.session_state.history      = []
    st.session_state.streak       = 0
    st.session_state.last_result  = None
    st.session_state.winner       = None

# ─── HELPERS ─────────────────────────────────────────────────────────────────

def pip_html(count, total, mode="you"):
    cls = "pip-on" if mode == "you" else "pip-on-lose"
    dots = "".join([f'<div class="{cls}"></div>']*count +
                   ['<div class="pip-off"></div>']*(total-count))
    return f'<div class="pip-row">{dots}</div>'

def history_html(history):
    dots = ""
    for h in history[-20:]:
        cls = {"W":"w","L":"l","T":"t"}[h]
        dots += f'<span class="hist-dot-{cls}"></span>'
    return f'<div style="text-align:center;margin-top:6px">{dots}</div>'

# ─── SCREENS ─────────────────────────────────────────────────────────────────

# ══════════════════════════════════════════════════════
#  HERO SCREEN
# ══════════════════════════════════════════════════════
if st.session_state.screen == "hero":
    st.markdown('<div class="anim-in">', unsafe_allow_html=True)

    st.markdown('<div class="hero-icon">✊ ✋ ✌️</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="rps-title">ROCK · PAPER<br>SCISSORS</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="rps-subtitle">— The Ultimate Showdown —</div>', unsafe_allow_html=True)

    # Rules
    st.markdown(f"""
    <div class="rps-card anim-in">
      <div style="color:{T['subtext']};font-size:0.7rem;letter-spacing:0.25em;text-transform:uppercase;margin-bottom:0.8rem">⚔️ &nbsp; Battle Rules</div>
      <div class="rule-row"><div class="rule-icon">✊</div> <span>Rock <b>crushes</b> Scissors</span></div>
      <div class="rule-row"><div class="rule-icon">✋</div> <span>Paper <b>smothers</b> Rock</span></div>
      <div class="rule-row" style="border:none"><div class="rule-icon">✌️</div> <span>Scissors <b>slices</b> Paper</span></div>
    </div>
    """, unsafe_allow_html=True)

    # Features
    st.markdown(f"""
    <div class="rps-card anim-in" style="text-align:center">
      <div style="color:{T['subtext']};font-size:0.7rem;letter-spacing:0.25em;text-transform:uppercase;margin-bottom:0.9rem">✨ &nbsp; Features</div>
      <span class="feature-pill">🏆 First to {WIN_AT} wins</span>
      <span class="feature-pill">🔥 Streak tracker</span>
      <span class="feature-pill">🎨 8 live themes</span>
      <span class="feature-pill">📊 Round history</span>
      <span class="feature-pill">⚡ Battle messages</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚔️  Enter the Arena", use_container_width=True):
            st.session_state.screen = "game"
            st.rerun()
    with col2:
        if st.button("🎨  Pick a Theme", use_container_width=True):
            st.session_state.screen = "theme"
            st.rerun()

    st.markdown(f"""
    <div style="text-align:center;margin-top:1.2rem;color:{T['subtext']};font-size:0.78rem;letter-spacing:0.12em">
    Currently: {st.session_state.theme_name}
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════
#  THEME CHOOSER SCREEN
# ══════════════════════════════════════════════════════
elif st.session_state.screen == "theme":
    st.markdown(f'<div class="rps-title" style="font-size:1.8rem">🎨 Choose Your Theme</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="rps-subtitle">Style defines the warrior</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    for tname, tdata in THEMES.items():
        active = "theme-active" if tname == st.session_state.theme_name else ""
        # swatch dots
        swatch = "".join([
            f'<span style="display:inline-block;width:14px;height:14px;border-radius:50%;background:{c};margin:0 3px;box-shadow:0 0 6px {c}"></span>'
            for c in [tdata["primary"], tdata["accent"], tdata["win"]]
        ])
        st.markdown(f"""
        <div class="theme-card {active}" style="display:flex;align-items:center;justify-content:space-between">
          <div>
            <span style="font-weight:700;font-size:1.05rem;color:{tdata['primary']}">{tname}</span><br>
            <span style="color:{tdata['subtext']};font-size:0.78rem">Font: {tdata['font']}</span>
          </div>
          <div>{swatch}</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"Select {tname}", key=f"theme_{tname}", use_container_width=True):
            st.session_state.theme_name = tname
            st.session_state.screen = "game" if st.session_state.player_score > 0 or st.session_state.cpu_score > 0 else "hero"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Back", use_container_width=False):
        st.session_state.screen = "hero"
        st.rerun()


# ══════════════════════════════════════════════════════
#  GAME SCREEN
# ══════════════════════════════════════════════════════
elif st.session_state.screen == "game":

    # ── Winner overlay
    if st.session_state.winner:
        w = st.session_state.winner
        emoji = "🏆" if w == "player" else "🤖"
        cls   = "winner-text" if w == "player" else "loser-text"
        msg   = "YOU WIN!" if w == "player" else "CPU WINS!"
        sub   = "Absolute legend. Pure skill." if w == "player" else "The machine was relentless."

        st.markdown(f"""
        <div class="winner-banner anim-pulse anim-in">
          <div style="font-size:4rem">{emoji}</div>
          <div class="{cls}">{msg}</div>
          <div style="color:{T['subtext']};margin-top:0.5rem;font-size:1rem">{sub}</div>
          <div style="margin-top:0.5rem;color:{T['accent']};font-size:0.9rem">
            Score resets — new match begins!
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄  Play Again", use_container_width=True):
            reset_game()
            st.rerun()

    else:
        # ── Header bar
        col_a, col_b = st.columns([5, 1])
        with col_a:
            st.markdown(f'<div class="rps-title" style="font-size:1.5rem;text-align:left">✊ · ✋ · ✌️</div>', unsafe_allow_html=True)
        with col_b:
            if st.button("🎨", help="Change theme"):
                st.session_state.screen = "theme"
                st.rerun()

        # ── Score board
        ps = st.session_state.player_score
        cs = st.session_state.cpu_score

        st.markdown(f"""
        <div class="rps-card anim-in" style="text-align:center">
          <div style="display:flex;align-items:center;justify-content:center;gap:2rem">
            <div class="score-block">
              <div class="score-label">YOU</div>
              <div class="score-number score-you">{ps}</div>
              {pip_html(ps, WIN_AT, "you")}
            </div>
            <div class="score-vs">VS</div>
            <div class="score-block">
              <div class="score-label">CPU</div>
              <div class="score-number score-cpu">{cs}</div>
              {pip_html(cs, WIN_AT, "cpu")}
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Streak
        sk = st.session_state.streak
        if sk >= 2:
            st.markdown(f'<div style="text-align:center;margin:0.3rem 0"><span class="streak-win">🔥 {sk}-Round Win Streak!</span></div>', unsafe_allow_html=True)
        elif sk <= -2:
            st.markdown(f'<div style="text-align:center;margin:0.3rem 0"><span class="streak-lose">💀 {abs(sk)}-Round Lose Streak!</span></div>', unsafe_allow_html=True)

        # ── History
        if st.session_state.history:
            st.markdown(history_html(st.session_state.history), unsafe_allow_html=True)

        # ── Last result
        if st.session_state.last_result:
            r = st.session_state.last_result
            oc = r["outcome"]
            res_cls = {"W":"result-win","L":"result-lose","T":"result-tie"}[oc]
            res_txt = {"W":"✔ You Win!","L":"✘ CPU Wins","T":"◈ Tie!"}[oc]

            st.markdown(f"""
            <div class="rps-card-glow anim-in">
              <div style="display:flex;justify-content:space-around;font-size:1.1rem;margin-bottom:0.7rem">
                <div style="text-align:center">
                  <div style="color:{T['subtext']};font-size:0.7rem;letter-spacing:0.15em">YOU</div>
                  <div style="font-size:1.8rem">{r['user']}</div>
                </div>
                <div style="color:{T['subtext']};font-size:1.5rem;align-self:center">⚡</div>
                <div style="text-align:center">
                  <div style="color:{T['subtext']};font-size:0.7rem;letter-spacing:0.15em">CPU</div>
                  <div style="font-size:1.8rem">{r['cpu']}</div>
                </div>
              </div>
              <hr class="rps-divider">
              <div class="{res_cls}">{res_txt}</div>
              <div style="color:{T['subtext']};text-align:center;margin-top:0.4rem;font-size:0.9rem">{r['msg']}</div>
            </div>
            """, unsafe_allow_html=True)

        # ── Choice buttons
        st.markdown(f"""
        <div style="color:{T['subtext']};font-size:0.72rem;letter-spacing:0.2em;
             text-transform:uppercase;text-align:center;margin:1rem 0 0.5rem">
          — Make your move —
        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(f'<button class="choice-btn btn-rock">✊<br><span style="font-size:0.75rem">ROCK</span></button>', unsafe_allow_html=True)
            if st.button("✊  Rock", key="rock", use_container_width=True):
                play_round("R")
                st.rerun()
        with c2:
            st.markdown(f'<button class="choice-btn btn-paper">✋<br><span style="font-size:0.75rem">PAPER</span></button>', unsafe_allow_html=True)
            if st.button("✋  Paper", key="paper", use_container_width=True):
                play_round("P")
                st.rerun()
        with c3:
            st.markdown(f'<button class="choice-btn btn-sci">✌️<br><span style="font-size:0.75rem">SCISSORS</span></button>', unsafe_allow_html=True)
            if st.button("✌️  Scissors", key="sci", use_container_width=True):
                play_round("S")
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        col_l, col_r = st.columns(2)
        with col_l:
            if st.button("🏠  Home", use_container_width=True):
                st.session_state.screen = "hero"
                st.rerun()
        with col_r:
            if st.button("🔄  Reset", use_container_width=True):
                reset_game()
                st.rerun()

        st.markdown(f"""
        <div style="text-align:center;margin-top:1rem;color:{T['subtext']};font-size:0.75rem">
        First to {WIN_AT} wins the match · {st.session_state.theme_name}
        </div>
        """, unsafe_allow_html=True)
