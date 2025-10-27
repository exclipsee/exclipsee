from pathlib import Path

# Output dir
out_dir = Path("dist")
out_dir.mkdir(parents=True, exist_ok=True)

# Helper to write a simple animated emoji SVG
def write_emoji_svg(filename: str, emoji: str, anim: str, size: int = 36):
    cx = cy = size // 2
    svg = f"""
<svg width=\"{size}\" height=\"{size}\" viewBox=\"0 0 {size} {size}\" xmlns=\"http://www.w3.org/2000/svg\" role=\"img\" aria-label=\"{emoji}\" >
  <g transform=\"translate({cx},{cy})\">
    <text x=\"0\" y=\"8\" text-anchor=\"middle\" font-size=\"24\">{emoji}</text>
    {anim}
  </g>
</svg>
"""
    (out_dir / filename).write_text(svg, encoding="utf-8")

# Animations
rotate_small = """
  <animateTransform attributeName=\"transform\" attributeType=\"XML\" type=\"rotate\" values=\"-18 0 0; 18 0 0; -18 0 0\" dur=\"2.2s\" repeatCount=\"indefinite\"/>
"""

bounce_small = """
  <animateTransform attributeName=\"transform\" attributeType=\"XML\" type=\"translate\" values=\"0 0; 0 -3; 0 0\" dur=\"1.6s\" repeatCount=\"indefinite\"/>
"""

rise_fall = """
  <animateTransform attributeName=\"transform\" attributeType=\"XML\" type=\"translate\" values=\"0 0; 0 -2; 0 0; 0 2; 0 0\" dur=\"1.8s\" repeatCount=\"indefinite\"/>
"""

pulse = """
  <animateTransform attributeName=\"transform\" attributeType=\"XML\" type=\"scale\" values=\"0.95; 1.05; 0.95\" dur=\"1.6s\" repeatCount=\"indefinite\"/>
"""

twinkle = """
  <animateTransform attributeName=\"transform\" attributeType=\"XML\" type=\"scale\" values=\"0.9; 1.12; 0.9\" dur=\"1.4s\" repeatCount=\"indefinite\"/>
"""

# Generate files
write_emoji_svg("emoji-about.svg", "🚀", rise_fall)
write_emoji_svg("emoji-learning.svg", "🎒", bounce_small)
write_emoji_svg("emoji-tech.svg", "🛠️", rotate_small)
write_emoji_svg("emoji-projects.svg", "🌟", twinkle)
write_emoji_svg("emoji-focus.svg", "🎯", pulse)
write_emoji_svg("emoji-stats.svg", "📈", rise_fall)
write_emoji_svg("emoji-connect.svg", "🤝", pulse)
