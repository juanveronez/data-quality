from pydantic import PositiveInt, ValidationError, validate_call


@validate_call
def soma(x: PositiveInt, y: PositiveInt) -> PositiveInt:
    return x + y


print(soma(3, 2))
print(soma(3, 5))

try:
    soma(3, -2)
except ValidationError as e:
    print(e)

try:
    soma(3, "a")
except ValidationError as e:
    print(e)
