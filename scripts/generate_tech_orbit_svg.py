import math
from pathlib import Path

# Config
WIDTH, HEIGHT = 960, 320
CX, CY = WIDTH // 2, HEIGHT // 2
RADIUS = 100
DUR = "24s"
LABEL = "Tech Orbit (skills snapshot)"
TECHS = [
  ("Python", "#3776AB", "Py"),
  ("C", "#00599C", "C"),
  ("Excel", "#217346", "XL"),
  ("Pandas", "#150458", "Pd"),
  ("NumPy", "#013243", "NP"),
  ("Jupyter", "#F37626", "Ju"),
  ("Git", "#F05032", "Git"),
  ("VS Code", "#007ACC", "VS"),
]

# Output path
out_dir = Path("dist")
out_dir.mkdir(parents=True, exist_ok=True)
svg_path = out_dir / "tech-orbit.svg"

# Helpers

def polar_to_cart(angle_deg: float, r: float):
    rad = math.radians(angle_deg)
    return CX + r * math.cos(rad), CY + r * math.sin(rad)

# Build labeled nodes around a circle
n = len(TECHS)
angle_step = 360.0 / n

# Animated group for orbiting nodes (with labels)
node_items = []
for i, (name, color, abbr) in enumerate(TECHS):
    angle = i * angle_step
    x, y = polar_to_cart(angle, RADIUS)
    lx, ly = polar_to_cart(angle, RADIUS + 18)
    node_items.append(
        f"""
    <g>
      <title>{name}</title>
      <circle cx="{x:.2f}" cy="{y:.2f}" r="8" fill="{color}" filter="url(#shadow)" />
      <text x="{lx:.2f}" y="{ly+4:.2f}" font-size="13" fill="#cbd5e1">{abbr}</text>
    </g>
    """
    )

# Legend at bottom
legend_items = []
legend_x = 60
legend_y = HEIGHT - 40
legend_gap = 95
for i, (name, color) in enumerate(TECHS):
    x = legend_x + i * legend_gap
    legend_items.append(
        f'<g><circle cx="{x}" cy="{legend_y}" r="5" fill="{color}" />\n'
        f'<text x="{x+12}" y="{legend_y+4}" font-size="14" fill="#9aa0a6">{name}</text></g>'
    )

# Background gradient with slow shimmer
background = f"""
<defs>
  <filter id="shadow" x="-50%" y="-50%" width="200%" height="200%">
    <feDropShadow dx="0" dy="1" stdDeviation="1.5" flood-color="#000000" flood-opacity="0.45"/>
  </filter>
  <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#0f172a">
      <animate attributeName="stop-color" values="#0f172a;#0a0f1f;#0f172a" dur="16s" repeatCount="indefinite"/>
    </stop>
    <stop offset="100%" stop-color="#1e293b">
      <animate attributeName="stop-color" values="#1e293b;#0e2133;#1e293b" dur="16s" repeatCount="indefinite"/>
    </stop>
  </linearGradient>
</defs>
<rect x="0" y="0" width="100%" height="100%" fill="url(#bgGrad)" rx="16"/>
"""

# Central label
center_label = f"""
<text x="{CX}" y="{CY - 8}" text-anchor="middle" font-size="28" font-weight="700" fill="#e2e8f0">exclipsee</text>
<text x="{CX}" y="{CY + 20}" text-anchor="middle" font-size="14" fill="#94a3b8">{LABEL}</text>
"""

# Orbit group with animation
orbit_group = (
    "<g id=\"orbit\" >"
    + "".join(node_items)
    + f"""
  <animateTransform attributeName="transform" attributeType="XML" type="rotate" from="0 {CX} {CY}" to="360 {CX} {CY}" dur="{DUR}" repeatCount="indefinite"/>
</g>
"""
)

# Subtle inner orbit ring
ring = f"<circle cx=\"{CX}\" cy=\"{CY}\" r=\"{RADIUS}\" fill=\"none\" stroke=\"#334155\" stroke-width=\"1.5\" stroke-dasharray=\"3 6\"/>"

# Compose SVG
svg = f"""
<svg width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Tech Orbit">
  {background}
  {ring}
  {orbit_group}
  {center_label}
  <g>
    {''.join(legend_items)}
  </g>
</svg>
"""

svg_path.write_text(svg, encoding="utf-8")
print(f"Wrote {svg_path}")
