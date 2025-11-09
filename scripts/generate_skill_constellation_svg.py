from pathlib import Path

WIDTH, HEIGHT = 960, 360
BG1, BG2 = "#0b1020", "#101a35"
LABEL = "Skill Constellation"

nodes = [
    ("Python", 160, 120, "#34d399"),
    ("SQL", 270, 80, "#4479a1"),
    ("Pandas", 360, 110, "#a78bfa"),
    ("NumPy", 420, 180, "#60a5fa"),
    ("Docker", 520, 120, "#2496ed"),
    ("scikit-learn", 380, 240, "#f97316"),
    ("Jupyter", 260, 200, "#f59e0b"),
    ("Excel", 140, 220, "#22c55e"),
    ("AI Tools", 600, 200, "#ff6b6b"),
    ("Git", 680, 150, "#fb7185"),
]

edges = [
    (0, 1), (1, 2), (2, 3), (3, 5), (5, 6), (6, 7), (0, 7),  # Main data flow
    (2, 4), (4, 9), (3, 8), (8, 9), (1, 6)  # Docker & AI connections
]

out_dir = Path("dist")
out_dir.mkdir(parents=True, exist_ok=True)
svg_path = out_dir / "skill-constellation.svg"

defs = f"""
<defs>
  <linearGradient id='bgGrad' x1='0%' y1='0%' x2='100%' y2='0%'>
    <stop offset='0%' stop-color='{BG1}'>
      <animate attributeName='stop-color' values='{BG1};#0f1a2e;{BG1}' dur='18s' repeatCount='indefinite'/>
    </stop>
    <stop offset='100%' stop-color='{BG2}'>
      <animate attributeName='stop-color' values='{BG2};#0c1430;{BG2}' dur='18s' repeatCount='indefinite'/>
    </stop>
  </linearGradient>
  <filter id='glow' x='-50%' y='-50%' width='200%' height='200%'>
    <feGaussianBlur stdDeviation='2' result='coloredBlur'/>
    <feMerge>
      <feMergeNode in='coloredBlur'/>
      <feMergeNode in='SourceGraphic'/>
    </feMerge>
  </filter>
  <style type='text/css'>
    @import url('https://fonts.googleapis.com/css?family=Open+Sans:400,700');
    text, tspan {{ font-family: 'Open Sans', 'Arial', sans-serif; }}
  </style>
</defs>
"""

background = "<rect x='0' y='0' width='100%' height='100%' fill='url(#bgGrad)' rx='16'/>"

edge_elems = []
for i, (a, b) in enumerate(edges):
    x1, y1, _ = nodes[a][1], nodes[a][2], nodes[a][3]
    x2, y2, _ = nodes[b][1], nodes[b][2], nodes[b][3]
    edge = f"""
    <line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}'
          stroke='#334155' stroke-width='1.2' stroke-dasharray='4 6' filter='url(#glow)'>
      <animate attributeName='stroke-dashoffset' values='0; -20' dur='2.8s' repeatCount='indefinite'/>
    </line>
    """
    edge_elems.append(edge)

node_elems = []
for name, x, y, color in nodes:
    node = f"""
    <g>
      <circle cx='{x}' cy='{y}' r='6.5' fill='{color}' filter='url(#glow)'>
        <animate attributeName='r' values='6.5; 8; 6.5' dur='2s' repeatCount='indefinite'/>
      </circle>
      <text x='{x+10}' y='{y+5}' font-size='13' fill='#cbd5e1'>{name}</text>
    </g>
    """
    node_elems.append(node)

title = f"""
<g>
  <text x='40' y='42' font-size='22' font-weight='700' fill='#e2e8f0'>exclipsee</text>
  <text x='40' y='64' font-size='13' fill='#94a3b8'>{LABEL}</text>
</g>
"""

constellation_group_start = "<g id='constellation' >\n" + "\n".join(edge_elems + node_elems) + "\n"
constellation_anim = "  <animateTransform attributeName='transform' type='translate' values='0 0; 3 1; -2 -1; 0 0' dur='24s' repeatCount='indefinite'/>\n"
constellation_group_end = "</g>\n"

svg = f"""
<svg width='{WIDTH}' height='{HEIGHT}' viewBox='0 0 {WIDTH} {HEIGHT}' fill='none' xmlns='http://www.w3.org/2000/svg' role='img' aria-label='Skill Constellation'>
  {defs}
  {background}
  {title}
  {constellation_group_start}{constellation_anim}{constellation_group_end}
</svg>
"""

svg_path.write_text(svg, encoding='utf-8')
print(f"Wrote {svg_path}")
