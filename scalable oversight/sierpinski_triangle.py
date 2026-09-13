# ============================================================
# Recursive Sierpinski triangle
# Extracted from the Block 3 live-demo code block in
# compass_artifact_..._text_markdown.md so it can run standalone.
# Requires: numpy, matplotlib.
#
# Usage:
#   python sierpinski_triangle.py                # depth 6, opens a window
#   python sierpinski_triangle.py 4              # depth 4
#   python sierpinski_triangle.py 6 out.png      # depth 6, saves to out.png
# ============================================================

import sys
import numpy as np
import matplotlib

# If an output file is requested, use a non-interactive backend so the
# script also works on a machine with no display.
if len(sys.argv) > 2:
    matplotlib.use("Agg")

import matplotlib.pyplot as plt


# ------------------------------------------------------------
# (1) RECURSIVE SIERPINSKI TRIANGLE
#     Base case + inductive step made explicit.
# ------------------------------------------------------------
def sierpinski_recursive(ax, p1, p2, p3, depth):
    """Draw a Sierpinski triangle by recursion.
    Base case: depth == 0  -> fill the triangle (p1,p2,p3).
    Recursive step: split into 3 corner sub-triangles using
    edge midpoints, recurse on each with depth-1.
    """
    if depth == 0:                                   # BASE CASE
        tri = plt.Polygon([p1, p2, p3], edgecolor='none')
        ax.add_patch(tri)
        return
    m12 = (p1 + p2) / 2.0                             # midpoints
    m23 = (p2 + p3) / 2.0
    m31 = (p3 + p1) / 2.0
    sierpinski_recursive(ax, p1,  m12, m31, depth - 1)  # INDUCTIVE STEP
    sierpinski_recursive(ax, m12, p2,  m23, depth - 1)
    sierpinski_recursive(ax, m31, m23, p3,  depth - 1)


def draw_recursive(depth=6, out=None):
    p1 = np.array([0.0, 0.0])
    p2 = np.array([1.0, 0.0])
    p3 = np.array([0.5, np.sqrt(3) / 2.0])
    fig, ax = plt.subplots(figsize=(6, 6))
    sierpinski_recursive(ax, p1, p2, p3, depth)
    ax.set_aspect('equal'); ax.axis('off')
    ax.set_title(f'Recursive Sierpinski (depth={depth}): '
                 f'{3**depth} triangles')
    if out:
        fig.savefig(out, dpi=150, bbox_inches='tight')
        print(f'Saved {out} ({3**depth} filled triangles)')
    else:
        plt.show()


if __name__ == "__main__":
    depth = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    out = sys.argv[2] if len(sys.argv) > 2 else None
    draw_recursive(depth=depth, out=out)
