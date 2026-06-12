"""
Trecelo — UML Diagram Generator
Generates three PDF diagrams:
  1. sequence_diagram.pdf
  2. use_case_diagram.pdf
  3. activity_diagram.pdf
"""

import os
import math
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.pdfgen import canvas as pdf_canvas

OUTPUT = os.path.join(os.path.dirname(__file__), "docs", "diagrams")
os.makedirs(OUTPUT, exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# PALETTE
# ─────────────────────────────────────────────────────────────────────────────
C_DARK      = colors.HexColor('#1e293b')
C_BLUE      = colors.HexColor('#1d4ed8')
C_BLUE_LIGHT= colors.HexColor('#eff6ff')
C_BLUE_BDR  = colors.HexColor('#93c5fd')
C_GREEN_BG  = colors.HexColor('#f0fdf4')
C_GREEN     = colors.HexColor('#166534')
C_RED_BG    = colors.HexColor('#fef2f2')
C_RED       = colors.HexColor('#991b1b')
C_AMBER_BG  = colors.HexColor('#fffbeb')
C_AMBER     = colors.HexColor('#92400e')
C_PURPLE_BG = colors.HexColor('#faf5ff')
C_PURPLE    = colors.HexColor('#6d28d9')
C_SLATE     = colors.HexColor('#475569')
C_SLATE_LT  = colors.HexColor('#94a3b8')
C_GREY_BG   = colors.HexColor('#f1f5f9')
C_WHITE     = colors.white
C_YELLOW_BG = colors.HexColor('#fefce8')
C_YELLOW_BDR= colors.HexColor('#fbbf24')

# ─────────────────────────────────────────────────────────────────────────────
# SHARED HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def page_title(c, w, h, title, subtitle):
    c.setFillColor(C_DARK)
    c.setFont("Helvetica-Bold", 15)
    c.drawCentredString(w / 2, h - 32, title)
    c.setFont("Helvetica", 9)
    c.setFillColor(C_SLATE)
    c.drawCentredString(w / 2, h - 48, subtitle)
    # top rule
    c.setStrokeColor(C_BLUE_BDR)
    c.setLineWidth(1.5)
    c.line(40, h - 56, w - 40, h - 56)


def fill_poly(c, pts, col):
    """Draw a filled polygon from a flat list of (x, y) pairs."""
    c.setFillColor(col)
    c.setStrokeColor(col)
    path = c.beginPath()
    path.moveTo(pts[0], pts[1])
    for i in range(2, len(pts), 2):
        path.lineTo(pts[i], pts[i + 1])
    path.close()
    c.drawPath(path, fill=1, stroke=0)


def arrow_head(c, tip_x, tip_y, direction='right', size=7, col=None):
    col = col or C_SLATE
    s = size * 0.45
    if direction == 'right':
        fill_poly(c, [tip_x, tip_y,
                      tip_x - size, tip_y + s,
                      tip_x - size, tip_y - s], col)
    elif direction == 'left':
        fill_poly(c, [tip_x, tip_y,
                      tip_x + size, tip_y + s,
                      tip_x + size, tip_y - s], col)
    elif direction == 'down':
        fill_poly(c, [tip_x, tip_y,
                      tip_x - s, tip_y + size,
                      tip_x + s, tip_y + size], col)


# ═════════════════════════════════════════════════════════════════════════════
# 1. SEQUENCE DIAGRAM
# ═════════════════════════════════════════════════════════════════════════════
def build_sequence_diagram():
    pw, ph = landscape(A4)          # 841.9 × 595.3
    c = pdf_canvas.Canvas(os.path.join(OUTPUT, "sequence_diagram.pdf"),
                          pagesize=landscape(A4))
    page_title(c, pw, ph,
               "Sequence Diagram  —  Trecelo Sample Tracking System",
               "Three core interaction flows: Authentication · Sample Creation · Status Update")

    # ── participants ─────────────────────────────────────────────────────────
    PARTS = ["Browser\n/ User", "Django\nView", "Form\nLayer", "Model\n/ DB"]
    n = len(PARTS)
    left, right = 60, pw - 60
    xs = [left + i * (right - left) / (n - 1) for i in range(n)]
    BOX_W, BOX_H = 98, 34
    TOP = ph - 68

    def draw_participants():
        for x, name in zip(xs, PARTS):
            c.setFillColor(C_DARK)
            c.setStrokeColor(C_DARK)
            c.setLineWidth(0)
            c.roundRect(x - BOX_W / 2, TOP - BOX_H / 2, BOX_W, BOX_H, 6, fill=1, stroke=0)
            c.setFillColor(C_WHITE)
            lines = name.split('\n')
            if len(lines) == 2:
                c.setFont("Helvetica-Bold", 8)
                c.drawCentredString(x, TOP + 5, lines[0])
                c.setFont("Helvetica", 7.5)
                c.drawCentredString(x, TOP - 5, lines[1])
            else:
                c.setFont("Helvetica-Bold", 8.5)
                c.drawCentredString(x, TOP - 3, name)

    draw_participants()

    # lifelines
    BOTTOM = 38
    c.setStrokeColor(C_SLATE_LT)
    c.setLineWidth(0.8)
    c.setDash(4, 3)
    for x in xs:
        c.line(x, TOP - BOX_H / 2, x, BOTTOM)
    c.setDash()

    # ── drawing helpers ───────────────────────────────────────────────────────
    y_cursor = [TOP - BOX_H / 2 - 4]

    def step(delta=16):
        y_cursor[0] -= delta
        return y_cursor[0]

    def msg(frm, to, label, dashed=False, col=None):
        """Horizontal message arrow between two participant indices."""
        col = col or (C_SLATE if dashed else C_BLUE)
        y = step()
        fx, tx = xs[frm], xs[to]
        c.setStrokeColor(col)
        c.setLineWidth(1.1)
        if dashed:
            c.setDash(3, 2)
        else:
            c.setDash()
        c.line(fx, y, tx, y)
        c.setDash()
        direction = 'right' if tx > fx else 'left'
        arrow_head(c, tx, y, direction, size=6, col=col)
        mid = (fx + tx) / 2
        c.setFillColor(C_DARK)
        c.setFont("Helvetica", 7.5)
        c.drawCentredString(mid, y + 4, label)

    def self_msg(idx, label):
        """Self-referential loop arrow."""
        y = step(18)
        x = xs[idx]
        lp = 28          # loop width
        c.setStrokeColor(C_BLUE)
        c.setLineWidth(1.1)
        c.line(x, y, x + lp, y)
        c.line(x + lp, y, x + lp, y - 14)
        c.line(x + lp, y - 14, x, y - 14)
        arrow_head(c, x, y - 14, 'left', size=6, col=C_BLUE)
        c.setFillColor(C_DARK)
        c.setFont("Helvetica", 7.5)
        c.drawString(x + lp + 3, y - 9, label)
        y_cursor[0] -= 4

    def section(label):
        y = step(14)
        c.setFillColor(colors.HexColor('#f0f9ff'))
        c.setStrokeColor(C_BLUE_BDR)
        c.setLineWidth(0.6)
        c.rect(14, y - 7, pw - 28, 16, fill=1, stroke=1)
        c.setFillColor(C_BLUE)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(22, y - 2, f"◆  {label}")
        y_cursor[0] -= 4

    # ── Flow 1 — Authentication ──────────────────────────────────────────────
    section("Flow 1 · User Authentication")
    msg(0, 1, "GET /")
    msg(1, 0, "200 OK — Login page rendered", dashed=True)
    msg(0, 1, "POST credentials (username + password)")
    msg(1, 3, "authenticate(username, password)")
    msg(3, 1, "User object | None", dashed=True)
    self_msg(1, "login(request, user)  ·  create session")
    msg(1, 0, "302 Redirect → /dashboard  +  session cookie", dashed=True)

    # ── Flow 2 — Maker Creates a Sample ─────────────────────────────────────
    section("Flow 2 · Maker Creates a Sample")
    msg(0, 1, "GET /samples/create/")
    msg(1, 3, "is_staff_or_admin(user) check")
    msg(3, 1, "✔ Authorised", dashed=True)
    msg(1, 0, "200 OK — SampleForm (empty)", dashed=True)
    msg(0, 1, "POST sample data + front/back images + challenge images")
    msg(1, 2, "SampleForm(POST, FILES)")
    self_msg(2, "form.is_valid()")
    msg(2, 3, "sample.save()  +  ChallengeImage.objects.create(...)")
    msg(3, 2, "Sample instance (pk assigned)", dashed=True)
    msg(2, 1, "✔ Saved — return instance", dashed=True)
    msg(1, 0, "302 Redirect → /samples/{pk}  +  toast notification", dashed=True)

    # ── Flow 3 — Admin Updates Sample Status ─────────────────────────────────
    section("Flow 3 · Admin Updates Sample Status")
    msg(0, 1, "POST /samples/update/{pk}   data: status = approved")
    msg(1, 3, "is_staff_or_admin(user) check")
    msg(3, 1, "✔ Authorised", dashed=True)
    msg(1, 2, "SampleForm(POST, FILES, instance=sample)")
    self_msg(2, "form.is_valid()")
    msg(2, 3, "sample.save()")
    msg(3, 2, "Updated sample", dashed=True)
    msg(2, 1, "✔ Updated — return instance", dashed=True)
    msg(1, 0, "302 Redirect → sample detail  +  toast  [status = Approved]", dashed=True)

    # bottom participant boxes
    for x, name in zip(xs, PARTS):
        c.setFillColor(C_DARK)
        c.roundRect(x - BOX_W / 2, BOTTOM - BOX_H / 2, BOX_W, BOX_H, 6, fill=1, stroke=0)
        c.setFillColor(C_WHITE)
        lines = name.split('\n')
        if len(lines) == 2:
            c.setFont("Helvetica-Bold", 8)
            c.drawCentredString(x, BOTTOM + 5, lines[0])
            c.setFont("Helvetica", 7.5)
            c.drawCentredString(x, BOTTOM - 5, lines[1])
        else:
            c.setFont("Helvetica-Bold", 8.5)
            c.drawCentredString(x, BOTTOM - 3, name)

    c.save()
    print("  ✓  sequence_diagram.pdf")


# ═════════════════════════════════════════════════════════════════════════════
# 2. USE CASE DIAGRAM
# ═════════════════════════════════════════════════════════════════════════════
def build_use_case_diagram():
    pw, ph = A4
    c = pdf_canvas.Canvas(os.path.join(OUTPUT, "use_case_diagram.pdf"), pagesize=A4)
    page_title(c, pw, ph,
               "Use Case Diagram  —  Trecelo Sample Tracking System",
               "Three actors and their system interactions")

    # ── system boundary ───────────────────────────────────────────────────────
    SX, SY = 128, 52
    SW, SH = pw - SX - 20, ph - SY - 68
    c.setFillColor(colors.HexColor('#f8fafc'))
    c.setStrokeColor(C_SLATE_LT)
    c.setLineWidth(1.5)
    c.rect(SX, SY, SW, SH, fill=1, stroke=1)
    c.setFillColor(C_DARK)
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(SX + SW / 2, SY + SH - 14, "« system »  Trecelo")

    # ── actor helper ──────────────────────────────────────────────────────────
    def draw_actor(ax, ay, label, role_col=C_DARK):
        c.setFillColor(role_col)
        c.setStrokeColor(role_col)
        c.setLineWidth(1.3)
        c.circle(ax, ay + 38, 9, fill=1, stroke=0)          # head
        c.line(ax, ay + 29, ax, ay + 10)                     # body
        c.line(ax - 13, ay + 22, ax + 13, ay + 22)           # arms
        c.line(ax, ay + 10, ax - 11, ay - 5)                 # left leg
        c.line(ax, ay + 10, ax + 11, ay - 5)                 # right leg
        c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(ax, ay - 14, label)

    # ── use-case oval helper ──────────────────────────────────────────────────
    OW, OH = 128, 22

    def draw_uc(ux, uy, label, bg='#eff6ff', bdr='#93c5fd', fg='#1e293b'):
        c.setFillColor(colors.HexColor(bg))
        c.setStrokeColor(colors.HexColor(bdr))
        c.setLineWidth(0.9)
        c.ellipse(ux - OW / 2, uy - OH / 2, ux + OW / 2, uy + OH / 2, fill=1, stroke=1)
        c.setFillColor(colors.HexColor(fg))
        c.setFont("Helvetica", 7.8)
        c.drawCentredString(ux, uy - 3, label)

    # ── connection line helper ────────────────────────────────────────────────
    def connect(ax, ay_mid, ux, uy, from_left=True):
        c.setStrokeColor(C_SLATE_LT)
        c.setLineWidth(0.8)
        edge_x = ux - OW / 2 if from_left else ux + OW / 2
        c.line(ax, ay_mid, edge_x, uy)

    # ── layout: use cases inside system ──────────────────────────────────────
    UX = SX + SW / 2          # horizontal centre of system box
    TOP_UC = SY + SH - 35

    # place use cases top → bottom with labels
    uc_list = [
        # (y-offset, label, bg, bdr, fg)
        (0,   "View Dashboard",              '#eff6ff', '#93c5fd', '#1e293b'),
        (35,  "View Samples",                '#eff6ff', '#93c5fd', '#1e293b'),
        (70,  "Export PDF / Excel",          '#eff6ff', '#93c5fd', '#1e293b'),
        (115, "Create Sample",               '#f0fdf4', '#86efac', '#166534'),
        (150, "Edit Sample",                 '#f0fdf4', '#86efac', '#166534'),
        (185, "Update My Profile",           '#f0fdf4', '#86efac', '#166534'),
        (230, "Manage Buyers",               '#fef2f2', '#fca5a5', '#991b1b'),
        (265, "Manage Makers (Staff)",        '#fef2f2', '#fca5a5', '#991b1b'),
        (300, "Manage Brands / Lookups",     '#fef2f2', '#fca5a5', '#991b1b'),
        (335, "View Credentials (pwd)",      '#fef2f2', '#fca5a5', '#991b1b'),
        (370, "Delete Sample",               '#fef2f2', '#fca5a5', '#991b1b'),
        (405, "Django Admin  /admin/",       '#fef2f2', '#fca5a5', '#991b1b'),
    ]

    uc_y = {}
    for offset, label, bg, bdr, fg in uc_list:
        y = TOP_UC - offset
        draw_uc(UX, y, label, bg, bdr, fg)
        uc_y[label] = y

    # ── actors ────────────────────────────────────────────────────────────────
    # Buyer — left, upper
    BUY_X, BUY_Y = 55, ph - 160
    draw_actor(BUY_X, BUY_Y, "Buyer", role_col=C_PURPLE)
    buy_mid = BUY_Y + 16
    for lbl in ["View Dashboard", "View Samples", "Export PDF / Excel"]:
        connect(BUY_X + 13, buy_mid, UX, uc_y[lbl], from_left=True)

    # Maker — left, middle
    MAK_X, MAK_Y = 55, ph - 330
    draw_actor(MAK_X, MAK_Y, "Maker", role_col=C_BLUE)
    mak_mid = MAK_Y + 16
    for lbl in ["View Dashboard", "View Samples", "Export PDF / Excel",
                "Create Sample", "Edit Sample", "Update My Profile"]:
        connect(MAK_X + 13, mak_mid, UX, uc_y[lbl], from_left=True)

    # Superadmin — right
    ADM_X, ADM_Y = pw - 48, ph - 270
    draw_actor(ADM_X, ADM_Y, "Superadmin", role_col=colors.HexColor('#dc2626'))
    adm_mid = ADM_Y + 16
    for lbl in ["View Dashboard", "View Samples", "Export PDF / Excel",
                "Create Sample", "Edit Sample",
                "Manage Buyers", "Manage Makers (Staff)",
                "Manage Brands / Lookups", "View Credentials (pwd)",
                "Delete Sample", "Django Admin  /admin/"]:
        connect(ADM_X - 13, adm_mid, UX, uc_y[lbl], from_left=False)

    # ── legend ────────────────────────────────────────────────────────────────
    LY, LX = SY + 42, SX + 6
    c.setFillColor(C_GREY_BG)
    c.setStrokeColor(colors.HexColor('#e2e8f0'))
    c.setLineWidth(0.5)
    c.rect(LX, LY - 8, SW - 12, 44, fill=1, stroke=1)
    c.setFont("Helvetica-Bold", 7.5)
    c.setFillColor(C_DARK)
    c.drawString(LX + 6, LY + 26, "Legend")
    items = [
        ('#eff6ff', '#93c5fd', "All Roles  (Buyer, Maker, Superadmin)"),
        ('#f0fdf4', '#86efac', "Maker  +  Superadmin"),
        ('#fef2f2', '#fca5a5', "Superadmin Only"),
    ]
    ix = LX + 10
    for bg, bdr, txt in items:
        c.setFillColor(colors.HexColor(bg))
        c.setStrokeColor(colors.HexColor(bdr))
        c.ellipse(ix, LY + 4, ix + 20, LY + 16, fill=1, stroke=1)
        c.setFillColor(C_SLATE)
        c.setFont("Helvetica", 7.5)
        c.drawString(ix + 24, LY + 6, txt)
        ix += 138

    c.save()
    print("  ✓  use_case_diagram.pdf")


# ═════════════════════════════════════════════════════════════════════════════
# 3. ACTIVITY DIAGRAM
# ═════════════════════════════════════════════════════════════════════════════
def build_activity_diagram():
    pw, ph = A4
    c = pdf_canvas.Canvas(os.path.join(OUTPUT, "activity_diagram.pdf"), pagesize=A4)
    page_title(c, pw, ph,
               "Activity Diagram  —  Trecelo Sample Tracking System",
               "Sample lifecycle: from login through creation, review, and approval / rejection")

    CX = pw / 2

    # ── drawing helpers ───────────────────────────────────────────────────────
    def start_node(x, y):
        c.setFillColor(C_DARK)
        c.circle(x, y, 9, fill=1, stroke=0)

    def end_node(x, y):
        c.setFillColor(C_WHITE)
        c.setStrokeColor(C_DARK)
        c.setLineWidth(2.2)
        c.circle(x, y, 11, fill=1, stroke=1)
        c.setFillColor(C_DARK)
        c.circle(x, y, 6, fill=1, stroke=0)

    def activity(x, y, label, w=148, bg='#eff6ff', bdr='#93c5fd', fg='#1e293b', h=22):
        c.setFillColor(colors.HexColor(bg))
        c.setStrokeColor(colors.HexColor(bdr))
        c.setLineWidth(0.9)
        c.roundRect(x - w / 2, y - h / 2, w, h, 8, fill=1, stroke=1)
        c.setFillColor(colors.HexColor(fg))
        c.setFont("Helvetica-Bold", 7.8)
        c.drawCentredString(x, y - 3, label)

    def decision(x, y, label, w=84):
        d = 17
        c.setFillColor(C_YELLOW_BG)
        c.setStrokeColor(C_YELLOW_BDR)
        c.setLineWidth(1)
        path = c.beginPath()
        path.moveTo(x, y + d)
        path.lineTo(x + w / 2, y)
        path.lineTo(x, y - d)
        path.lineTo(x - w / 2, y)
        path.close()
        c.drawPath(path, fill=1, stroke=1)
        c.setFillColor(colors.HexColor('#78350f'))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawCentredString(x, y - 3, label)

    def fork_bar(x, y, w=200):
        c.setFillColor(C_DARK)
        c.rect(x - w / 2, y - 3, w, 6, fill=1, stroke=0)

    def arr_down(x, y1, y2, label=None, col='#64748b'):
        c.setStrokeColor(colors.HexColor(col))
        c.setLineWidth(1)
        c.setDash()
        c.line(x, y1, x, y2 + 6)
        arrow_head(c, x, y2, 'down', size=6, col=colors.HexColor(col))
        if label:
            c.setFillColor(C_SLATE)
            c.setFont("Helvetica", 7)
            c.drawString(x + 4, (y1 + y2) / 2, label)

    def arr_line(x1, y1, x2, y2, label=None, col='#64748b'):
        c.setStrokeColor(colors.HexColor(col))
        c.setLineWidth(1)
        c.line(x1, y1, x2, y2)
        dx, dy = x2 - x1, y2 - y1
        ln = math.hypot(dx, dy)
        if ln > 0:
            ux, uy = dx / ln, dy / ln
            px, py = -uy, ux
            fill_poly(c, [x2, y2,
                          x2 - ux * 8 + px * 3.5, y2 - uy * 8 + py * 3.5,
                          x2 - ux * 8 - px * 3.5, y2 - uy * 8 - py * 3.5],
                      colors.HexColor(col))
        if label:
            c.setFillColor(C_SLATE)
            c.setFont("Helvetica", 7)
            c.drawString((x1 + x2) / 2 + 3, (y1 + y2) / 2 + 2, label)

    def lbl(x, y, text, bold=False, col='#64748b', size=7):
        c.setFillColor(colors.HexColor(col))
        c.setFont("Helvetica-Bold" if bold else "Helvetica", size)
        c.drawCentredString(x, y, text)

    # ── layout ────────────────────────────────────────────────────────────────
    y = ph - 72

    start_node(CX, y);  arr_down(CX, y - 9, y - 26);  y -= 34

    activity(CX, y, "User Visits Login Page  ( / )");  arr_down(CX, y - 11, y - 26);  y -= 34

    activity(CX, y, "Enter Username + Password")
    arr_down(CX, y - 11, y - 26);  y -= 34

    decision(CX, y, "Valid?")

    # ── No branch ────────────────────────────────────────────────────────────
    err_x = CX - 110
    arr_line(CX - 42, y, err_x, y);   lbl(err_x + 22, y + 8, "No", bold=True, col='#dc2626')
    activity(err_x, y - 36, "Show Error Toast", w=110, bg='#fef2f2', bdr='#fca5a5', fg='#991b1b')
    # loop back up
    arr_line(err_x, y - 47, err_x, y - 82)
    arr_line(err_x, y - 82, CX - 74, y - 82)
    arr_line(CX - 74, y - 82, CX - 74, y + 26 + 22)
    arr_line(CX - 74, y + 26 + 22, CX - 74, y + 26)

    # ── Yes branch ───────────────────────────────────────────────────────────
    lbl(CX + 8, y - 22, "Yes", bold=True, col='#15803d')
    arr_down(CX, y - 17, y - 32);  y -= 40

    activity(CX, y, "Redirect → Dashboard",
             bg='#f0fdf4', bdr='#86efac', fg='#166534')
    arr_down(CX, y - 11, y - 26);  y -= 34

    decision(CX, y, "Role?")

    role_y = y
    GAP = 148

    # ─── Buyer branch (left) ─────────────────────────────────────────────────
    bx = CX - GAP
    arr_line(CX - 42, role_y, bx, role_y - 18)
    lbl(bx + 14, role_y - 13, "Buyer", bold=True, col='#7c3aed')
    by = role_y - 40
    activity(bx, by, "View Brand Samples",  w=118, bg='#faf5ff', bdr='#c4b5fd', fg='#6d28d9');  by -= 30
    activity(bx, by, "Filter / Search",     w=118, bg='#faf5ff', bdr='#c4b5fd', fg='#6d28d9');  by -= 30
    activity(bx, by, "View Sample Detail",  w=118, bg='#faf5ff', bdr='#c4b5fd', fg='#6d28d9');  by -= 30
    activity(bx, by, "Export PDF / Excel",  w=118, bg='#faf5ff', bdr='#c4b5fd', fg='#6d28d9')
    by -= 11
    buy_end = by

    # ─── Maker branch (centre) ───────────────────────────────────────────────
    arr_down(CX, role_y - 17, role_y - 32)
    lbl(CX + 6, role_y - 28, "Maker", bold=True, col='#1d4ed8')
    my = role_y - 50
    activity(CX, my, "View Own Samples",   bg='#eff6ff', bdr='#93c5fd', fg='#1e293b');  my -= 30
    activity(CX, my, "Create / Edit Sample", bg='#eff6ff', bdr='#93c5fd', fg='#1e293b');  my -= 30
    decision(CX, my, "Save as?")

    dmy = my
    # Draft
    arr_line(CX - 42, dmy, CX - 82, dmy - 20)
    activity(CX - 82, dmy - 42, "Draft", w=72, bg='#f1f5f9', bdr='#cbd5e1', fg='#475569')
    lbl(CX - 72, dmy - 12, "Draft", bold=False, col='#64748b')
    # Pending
    arr_line(CX + 42, dmy, CX + 82, dmy - 20)
    activity(CX + 82, dmy - 42, "Pending", w=72, bg='#fffbeb', bdr='#fde68a', fg='#92400e')
    lbl(CX + 66, dmy - 12, "Pending", bold=False, col='#92400e')

    mak_end = dmy - 53

    # ─── Admin branch (right) ────────────────────────────────────────────────
    ax = CX + GAP
    arr_line(CX + 42, role_y, ax, role_y - 18)
    lbl(ax - 14, role_y - 13, "Admin", bold=True, col='#dc2626')
    ay = role_y - 40
    activity(ax, ay, "View All Samples",     w=118, bg='#fef2f2', bdr='#fca5a5', fg='#991b1b');  ay -= 30
    activity(ax, ay, "Manage Users/Brands",  w=118, bg='#fef2f2', bdr='#fca5a5', fg='#991b1b');  ay -= 30
    activity(ax, ay, "Review Pending Items", w=118, bg='#fef2f2', bdr='#fca5a5', fg='#991b1b');  ay -= 12
    decision(ax, ay, "Decision?", w=88)

    ddy = ay
    arr_line(ax - 44, ddy, ax - 80, ddy - 18)
    activity(ax - 80, ddy - 38, "Approve", w=72, bg='#f0fdf4', bdr='#86efac', fg='#166534')
    lbl(ax - 72, ddy - 11, "Approve", bold=False, col='#15803d')

    arr_line(ax + 44, ddy, ax + 48, ddy - 18)
    activity(ax + 48, ddy - 38, "Reject", w=72, bg='#fef2f2', bdr='#fca5a5', fg='#991b1b')
    lbl(ax + 38, ddy - 11, "Reject", bold=False, col='#dc2626')

    adm_end = ddy - 49

    # ─── merge bar ────────────────────────────────────────────────────────────
    merge_y = min(buy_end, mak_end, adm_end) - 18
    fork_bar(CX, merge_y, w=GAP * 2 + 20)
    arr_line(bx,    buy_end, bx,    merge_y + 3)
    arr_line(CX,    mak_end, CX,    merge_y + 3)
    arr_line(ax,    adm_end, ax,    merge_y + 3)
    arr_down(CX, merge_y - 3, merge_y - 18)

    # logout → end
    lo_y = merge_y - 36
    activity(CX, lo_y, "Logout  /  Session Terminated",
             bg='#f1f5f9', bdr='#cbd5e1', fg='#475569')
    arr_down(CX, lo_y - 11, lo_y - 26)
    end_node(CX, lo_y - 38)

    c.save()
    print("  ✓  activity_diagram.pdf")


# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"\nGenerating diagrams → {OUTPUT}\n")
    build_sequence_diagram()
    build_use_case_diagram()
    build_activity_diagram()
    print(f"\nDone — 3 PDFs written to docs/diagrams/\n")
