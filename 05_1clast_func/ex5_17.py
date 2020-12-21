from ex5_15_clip import clip

from inspect import signature

sig = signature(clip)
print(f"{sig=}")
print(f"{str(sig)=}")
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)