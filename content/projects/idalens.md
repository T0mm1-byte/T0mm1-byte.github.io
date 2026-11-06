---
title: IDALens
summary: An IDA Pro plugin that adds an interactive cross-reference graph of your functions in its own tab.
date: '2026-11-02'
language: Python
requires: IDA with IDAPython (developed against IDA 9)
license: MIT
repo: https://github.com/T0mm1-byte/IDALens
---

IDALens adds a new tab to IDA with a cross-reference graph of your functions, laid out like the assembly flow chart in IDA View-A. It was my bachelor's degree final project.

<img src="/images/idalens/graph.png" alt="The IDALens tab in IDA, showing main at the top of a call graph with its callees below it" width="1913" height="948" loading="lazy">

## What it does

**The graph is customizable.** Pick a target function (`main` by default) and how many levels of callers (1 by default) and callees (2 by default) to show. A caller level of 1 shows every function that directly calls the target, a level of 2 also shows their callers, and so on. Callees work the same way in the other direction. The current target is shown between square brackets in its node.

If `main` isn't found, in a stripped binary for example, the initial graph is empty and you can build one by choosing the parameters yourself. The default graph can always be restored.

**The graph is interactive.** From any node you can jump straight to that function in IDA View-A or Pseudocode-A.

<img src="/images/idalens/context-menu.png" alt="The IDALens right-click menu open over the graph" loading="lazy">

Levels are capped at 200, to keep the graph readable.

## Install

Copy `idalens.py` into the IDA plugins directory:

- Linux/macOS: `~/.idapro/plugins/`
- Windows: `%APPDATA%\Hex-Rays\IDA Pro\plugins\`

The graph opens automatically when a database is loaded, after the initial auto-analysis. You can also open it from Edit → Plugins → IDALens (`Ctrl+Shift+L`). To turn off the automatic start, set `AUTOSTART = False` in `idalens.py`.

To try it without installing, run it once from File → Script File → `idalens.py`.

## Hotkeys

| Action | Key |
|---|---|
| Choose target function from list | `T` |
| Select clicked node as target | `R` |
| Change levels depth | `D` |
| Return to main | `M` |
| Rebuild graph | `Ctrl+R` |

The right-click menu offers the same actions.

## License

MIT. IDALens does not redistribute any part of IDA Pro, the IDA SDK or IDAPython: it only imports modules provided by an existing IDA installation and requires a valid IDA license to run. IDA Pro and Hex-Rays are trademarks of Hex-Rays SA, and this project is not affiliated with or endorsed by Hex-Rays.
