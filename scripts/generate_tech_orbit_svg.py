import math
from pathlib import Path

# Config
WIDTH, HEIGHT = 900, 280
CX, CY = WIDTH // 2, HEIGHT // 2
RADIUS = 90
DUR = "22s"
LABEL = "Tech Orbit"
TECHS = [
    ("Python", "#3776AB"),
    ("C", "#00599C"),
    ("Excel", "#217346"),
    ("Pandas", "#150458"),
    ("NumPy", "#013243"),
    ("Jupyter", "#F37626"),
    ("Git", "#F05032"),
    ("VS Code", "#007ACC"),
]

# Output path
out_dir = Path("dist")
out_dir.mkdir(parents=True, exist_ok=True)
svg_path = out_dir / "tech-orbit.svg"

# Helpers

def polar_to_cart(angle_deg: float, r: float):
    rad = math.radians(angle_deg)
    return CX + r * math.cos(rad), CY + r * math.sin(rad)

# Build dots around a circle
n = len(TECHS)
angle_step = 360.0 / n

# Animated group for orbiting dots
dots = [
    f"""
    <g>
      <title>{name}</title>
      <circle cx="{polar_to_cart(i*angle_step, RADIUS)[0]:.2f}" cy="{polar_to_cart(i*angle_step, RADIUS)[1]:.2f}" r="7" fill="{color}" />
    </g>
    """
    for i, (name, color) in enumerate(TECHS)
]

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
    + "".join(dots)
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
