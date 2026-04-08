import random
import os
import re

# ─── ANSI COLOR THEMES ──────────────────────────────────────────────────────

THEMES = {
    "1": {
        "name":    "Cosmic Purple",
        "primary": "\033[95m",
        "accent":  "\033[94m",
        "win":     "\033[92m",
        "lose":    "\033[91m",
        "tie":     "\033[93m",
        "title":   "\033[35m",
        "border":  "\033[35m",
        "reset":   "\033[0m",
        "bold":    "\033[1m",
    },
    "2": {
        "name":    "Fire Orange",
        "primary": "\033[91m",
        "accent":  "\033[33m",
        "win":     "\033[92m",
        "lose":    "\033[31m",
        "tie":     "\033[33m",
        "title":   "\033[31m",
        "border":  "\033[33m",
        "reset":   "\033[0m",
        "bold":    "\033[1m",
    },
    "3": {
        "name":    "Ocean Blue",
        "primary": "\033[94m",
        "accent":  "\033[96m",
        "win":     "\033[92m",
        "lose":    "\033[91m",
        "tie":     "\033[96m",
        "title":   "\033[34m",
        "border":  "\033[34m",
        "reset":   "\033[0m",
        "bold":    "\033[1m",
    },
    "4": {
        "name":    "Forest Green",
        "primary": "\033[92m",
        "accent":  "\033[32m",
        "win":     "\033[92m",
        "lose":    "\033[91m",
        "tie":     "\033[32m",
        "title":   "\033[32m",
        "border":  "\033[32m",
        "reset":   "\033[0m",
        "bold":    "\033[1m",
    },
    "5": {
        "name":    "Rose Pink",
        "primary": "\033[95m",
        "accent":  "\033[35m",
        "win":     "\033[92m",
        "lose":    "\033[91m",
        "tie":     "\033[95m",
        "title":   "\033[35m",
        "border":  "\033[35m",
        "reset":   "\033[0m",
        "bold":    "\033[1m",
    },
}

ICONS = {"R": "✊ Rock", "P": "✋ Paper", "S": "✌  Scissors"}
BEATS = {"R": "S", "P": "R", "S": "P"}
WIN_AT = 5


# ─── HELPERS ────────────────────────────────────────────────────────────────

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def line(t, char="─", width=52):
    c = t["border"]
    r = t["reset"]
    print(f"{c}{char * width}{r}")


def center(text, width=52):
    print(text.center(width))


def header(t):
    clear()
    b = t["border"]
    ti = t["title"]
    bo = t["bold"]
    r = t["reset"]
    print()
    print(f"{b}{'═' * 52}{r}")
    print(f"{b}║{r}{ti}{bo}{'ROCK  ·  PAPER  ·  SCISSORS':^50}{r}{b}║{r}")
    print(f"{b}{'═' * 52}{r}")
    print(f"  {t['accent']}Theme: {t['name']}{r}")
    print()


def score_bar(t, player_score, cpu_score, history):
    p = t["primary"]
    wi = t["win"]
    lo = t["lose"]
    ti2 = t["tie"]
    r = t["reset"]
    bo = t["bold"]
    b = t["border"]

    # Score display
    print(f"  {bo}{'YOU':^10}{r}    {b}VS{r}    {bo}{'CPU':^10}{r}")
    p_disp = f"{p}{bo}{player_score}{r}"
    c_disp = f"{lo}{bo}{cpu_score}{r}"
    print(f"   {p_disp:^18}          {c_disp:^18}")

    # Progress pips toward WIN_AT
    p_pips = f"{wi}{'● ' * player_score}{'○ ' * (WIN_AT - player_score)}{r}"
    c_pips = f"{lo}{'● ' * cpu_score}{'○ ' * (WIN_AT - cpu_score)}{r}"
    print(f"  {p_pips}    {c_pips}")

    # Round history dots
    if history:
        dots = ""
        for h in history:
            if h == "W":
                dots += f"{wi}◆{r} "
            elif h == "L":
                dots += f"{lo}◆{r} "
            else:
                dots += f"{ti2}◇{r} "
        print(f"\n  History: {dots}")
    print()


def show_result(t, user_choice, cpu_choice, outcome):
    wi = t["win"]
    lo = t["lose"]
    ti2 = t["tie"]
    r = t["reset"]
    bo = t["bold"]
    b = t["border"]

    line(t)
    u_icon = ICONS[user_choice]
    c_icon = ICONS[cpu_choice]
    print(f"  {bo}You:{r}  {u_icon}")
    print(f"  {bo}CPU:{r}  {c_icon}")
    line(t, "─")

    if outcome == "W":
        msg = f"{wi}{bo}  ✔  You Win this round!{r}"
    elif outcome == "L":
        msg = f"{lo}{bo}  ✘  CPU Wins this round!{r}"
    else:
        msg = f"{ti2}{bo}  ◈  It's a Tie!{r}"

    print(msg)
    line(t)
    print()


def winner_banner(t, winner):
    clear()
    b = t["border"]
    wi = t["win"]
    lo = t["lose"]
    bo = t["bold"]
    r = t["reset"]

    print()
    print(f"{b}{'╔' + '═'*50 + '╗'}{r}")
    if winner == "player":
        print(f"{b}║{r}{wi}{bo}{'🏆  YOU WIN THE ROUND! 🏆':^50}{r}{b}║{r}")
    else:
        print(f"{b}║{r}{lo}{bo}{'🤖  CPU WINS THE ROUND! 🤖':^50}{r}{b}║{r}")
    print(f"{b}{'╚' + '═'*50 + '╝'}{r}")
    print()
    print(f"  {t['accent']}Score has been reset. Starting fresh!{r}")
    print()
    input(f"  {t['primary']}Press Enter to continue...{r}")


def choose_theme():
    clear()
    print()
    print("\033[1m  Choose Your Theme\033[0m")
    print()
    for key, th in THEMES.items():
        print(f"  [{th['primary']}{key}\033[0m]  {th['primary']}{th['name']}\033[0m")
    print()
    while True:
        choice = input("  Enter theme number (1-5): ").strip()
        if choice in THEMES:
            return THEMES[choice]
        print("  Please enter a number between 1 and 5.")


def show_hero(t):
    clear()
    b = t["border"]
    ti = t["title"]
    p = t["primary"]
    a = t["accent"]
    bo = t["bold"]
    r = t["reset"]

    art = f"""
{b}  ╔══════════════════════════════════════════════════╗{r}
{b}  ║{r}                                                  {b}║{r}
{b}  ║{r}  {ti}{bo}  ✊  ROCK · PAPER · SCISSORS  ✌  {r}  {b}║{r}
{b}  ║{r}                                                  {b}║{r}
{b}  ║{r}  {a}  The classic game. First to {WIN_AT} wins!{r}          {b}║{r}
{b}  ║{r}                                                  {b}║{r}
{b}  ║{r}  {p}  ● Score tracks up to {WIN_AT} — then resets{r}        {b}║{r}
{b}  ║{r}  {p}  ● History dots show each round result{r}              {b}║{r}
{b}  ║{r}  {p}  ● Switch theme anytime mid-game{r}                    {b}║{r}
{b}  ║{r}                                                  {b}║{r}
{b}  ╚══════════════════════════════════════════════════╝{r}
"""
    print(art)
    input(f"  {p}Press Enter to start playing...{r}")


# ─── MAIN GAME ───────────────────────────────────────────────────────────────

def game():
    t = choose_theme()
    show_hero(t)

    player_score = 0
    cpu_score = 0
    history = []

    while True:
        header(t)
        score_bar(t, player_score, cpu_score, history)

        # ── Input
        prompt = (
            f"  {t['primary']}Choose:{t['reset']}  "
            f"[{t['accent']}R{t['reset']}]ock  "
            f"[{t['accent']}P{t['reset']}]aper  "
            f"[{t['accent']}S{t['reset']}]cissors  "
            f"[{t['accent']}T{t['reset']}]heme  "
            f"[{t['accent']}E{t['reset']}]xit\n  > "
        )
        user = input(prompt).strip().upper()

        # ── Validate
        if not re.match(r"^[RSPTE]$", user):
            print(f"\n  {t['lose']}Invalid input. Please enter R, P, S, T, or E.{t['reset']}")
            input(f"  {t['primary']}Press Enter to continue...{t['reset']}")
            continue

        # ── Exit
        if user == "E":
            clear()
            print(f"\n  {t['primary']}Thanks for playing! Goodbye. 👋{t['reset']}\n")
            break

        # ── Switch theme
        if user == "T":
            t = choose_theme()
            continue

        # ── CPU move
        cpu = random.choice(["R", "P", "S"])

        # ── Determine outcome
        if user == cpu:
            outcome = "T"
        elif BEATS[user] == cpu:
            outcome = "W"
            player_score += 1
        else:
            outcome = "L"
            cpu_score += 1

        history.append(outcome)

        # ── Show result
        header(t)
        score_bar(t, player_score, cpu_score, history)
        show_result(t, user, cpu, outcome)
        input(f"  {t['primary']}Press Enter for next round...{t['reset']}")

        # ── Check win condition (first to WIN_AT)
        if player_score >= WIN_AT:
            winner_banner(t, "player")
            player_score = 0
            cpu_score = 0
            history = []
        elif cpu_score >= WIN_AT:
            winner_banner(t, "cpu")
            player_score = 0
            cpu_score = 0
            history = []


# ─── ENTRY POINT ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    game()