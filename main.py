from __future__ import annotations


def inverse_sign(string: str) -> str:
    replace = {'-': '+', '+': '-'}
    return ''.join(replace.get(c, c) for c in string)


def task(seq: list[int], goal: int) -> set[str]:
    if len(seq) == 0:
        if goal == 0:
            return {''}
        return set()

    result = set()

    num = 0
    for i, value in enumerate(seq):
        num = num * 10 + value

        for answer in task(seq[i + 1:], goal - num):
            tail = ('+' + answer) if answer else ''
            result.add(str(num) + tail)

        for answer in task(seq[i + 1:], num - goal):
            tail = ('-' + inverse_sign(answer)) if answer else ''
            result.add(str(num) + tail)

    return result


def main():
    seq = list(map(int, '9876543210'))
    for item in sorted(task(seq, 200)):
        print(item)


if __name__ == '__main__':
    main()
