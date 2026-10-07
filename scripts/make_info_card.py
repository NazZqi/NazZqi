
import os

STATIC = os.getenv("STATIC", "0") == "1"

# Dimensiones ajustadas para acompañar al retrato ASCII (ancho: 490)
WIDTH = 490
HEIGHT = 742

css_animation = "" if STATIC else """
    .line {
      opacity: 0;
      animation: fadeIn 0.35s ease-out forwards;
    }
    @keyframes fadeIn {
      to { opacity: 1; }
    }
    .l0 { animation-delay: 0.10s; }
    .l1 { animation-delay: 0.25s; }
    .l2 { animation-delay: 0.40s; }
    .l3 { animation-delay: 0.55s; }
    .l4 { animation-delay: 0.70s; }
    .l5 { animation-delay: 0.85s; }
    .l6 { animation-delay: 1.00s; }
    .l7 { animation-delay: 1.15s; }
    .l8 { animation-delay: 1.30s; }
    .l9 { animation-delay: 1.45s; }
"""

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="auto">
  <style>
    .bg {{ fill: #0d1117; }}
    .term-header {{ font-family: monospace; font-size: 14px; font-weight: bold; fill: #58a6ff; }}
    .divider {{ font-family: monospace; font-size: 13px; fill: #30363d; }}
    .key {{ font-family: monospace; font-size: 13px; font-weight: bold; fill: #7ee787; }}
    .val {{ font-family: monospace; font-size: 13px; fill: #c9d1d9; }}
    .subval {{ font-family: monospace; font-size: 12px; fill: #8b949e; }}
    .accent {{ fill: #ffa657; }}
    {css_animation}
  </style>

  <!-- Fondo de la tarjeta -->
  <rect width="100%" height="100%" class="bg" rx="6" />

  <g transform="translate(28, 45)">
    <!-- Prompt inicial -->
    <text y="0" class="term-header line l0">nazzqi@github ~ $ neofetch</text>
    <text y="24" class="divider line l1">------------------------------------------</text>

    <!-- Información principal -->
    <text y="60" class="key line l2">OS:</text>
    <text x="80" y="60" class="val line l2">Arch Linux x86_64</text>

    <text y="92" class="key line l3">Host:</text>
    <text x="80" y="92" class="val line l3">Ignacio Mendoza (Nazdev)</text>

    <text y="124" class="key line l4">Role:</text>
    <text x="80" y="124" class="val line l4">Software &amp; Systems Developer</text>

    <text y="156" class="key line l5">Stack:</text>
    <text x="80" y="156" class="val line l5">Python, C/C++, Docker, Linux, SQL</text>

    <text y="188" class="key line l6">Focus:</text>
    <text x="80" y="188" class="val line l6">Backend Systems, Hardware &amp; Embedded</text>

    <text y="230" class="term-header line l7">Highlights</text>
    <text y="245" class="divider line l7">------------------------------------------</text>

    <text y="280" class="val line l8">⚡ <tspan class="accent">Building:</tspan> Automated tools &amp; Custom Electronics</text>
    <text y="308" class="val line l8">🛠️ <tspan class="accent">Tools:</tspan> Git, Linux Shell (Fish), Microservices</text>
    <text y="336" class="val line l9">🎯 <tspan class="accent">Goal:</tspan> High-performance architectures</text>

    <!-- Paleta terminal estilo neofetch -->
    <g transform="translate(0, 390)" class="line l9">
      <rect x="0"   y="0" width="22" height="14" fill="#ff7b72" rx="2" />
      <rect x="28"  y="0" width="22" height="14" fill="#7ee787" rx="2" />
      <rect x="56"  y="0" width="22" height="14" fill="#f2cc60" rx="2" />
      <rect x="84"  y="0" width="22" height="14" fill="#58a6ff" rx="2" />
      <rect x="112" y="0" width="22" height="14" fill="#bc8cff" rx="2" />
      <rect x="140" y="0" width="22" height="14" fill="#79c0ff" rx="2" />
      <rect x="168" y="0" width="22" height="14" fill="#d2a8ff" rx="2" />
    </g>
  </g>
</svg>"""

output_path = "info-card.svg"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(svg_content)

print(f"{output_path} generado correctamente.")