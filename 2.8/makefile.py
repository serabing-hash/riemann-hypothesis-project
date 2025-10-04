import os
import subprocess

# Compile LaTeX into PDF
tex_file = "riemann_v2_8.tex"
pdf_file = "riemann_v2_8.pdf"

subprocess.run(["pdflatex", tex_file])
print(f"Compiled {tex_file} → {pdf_file}")
