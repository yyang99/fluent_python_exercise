from ex5_19_clip_annot import clip
from inspect import signature

sig = signature(clip)
print(f'{sig.return_annotation=}')

for param in sig.parameters.values():
    note = repr(param.annotation).ljust(13)
    print(note, ':', param.name, '=', param.default)