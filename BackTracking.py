

answer = []
n = 3

def generate(tar_list, left, right):
    if len(tar_list) == 2 * n:
        answer.append("".join(tar_list))
        return

    if n > left:
        tar_list.append("(")
        generate(tar_list, left + 1, right)
        tar_list.pop()

    if left > right:
        tar_list.append(")")
        generate(tar_list, left, right + 1)
        tar_list.pop()


generate([], 0, 0)