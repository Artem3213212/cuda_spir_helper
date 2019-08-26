plugin for CudaText.
provides auto-completion for SPIR (i.e. SPIR-V) lexer.

handles two kinds of completions:
- if caret is inside variable (starting with % char). here plugin suggests all possible variables from current file.
- if caret is inside SPIR keyword (for example, starting with "Op"). here plugin suggests possible keywords, from its local database in JSON format (official database for SPIR language).

authors:
  Artem Gavrilov, https://github.com/Artem3213212
  Alexey Torgashin (CudaText)
license: MIT
