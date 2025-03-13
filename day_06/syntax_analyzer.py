import re

# Token specifications from previous example
token_specification = [
    ("NUMBER", r"\d+"),
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("TIMES", r"\*"),
    ("DIVIDE", r"/"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("SKIP", r"[ \t\n]+"),
    ("MISMATCH", r"."),
]

# Combined token regex
tok_regex = "|".join(f"(?P<{pair[0]}>{pair[1]})" for pair in token_specification)


def lex(code):
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == "SKIP":
            continue
        elif kind == "MISMATCH":
            raise RuntimeError(f"{value!r} unexpected")
        # print(value)
        yield kind, value


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next_token()

    def next_token(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        result = self.expr()
        if self.current_token is not None:
            raise SyntaxError("Unexpected token")
        return result

    def expr(self):
        result = self.term()
        while self.current_token and self.current_token[0] in ("PLUS", "MINUS"):
            op = self.current_token
            self.next_token()
            result = (op[0], result, self.term())
        return result

    def term(self):
        result = self.factor()
        while self.current_token and self.current_token[0] in ("TIMES", "DIVIDE"):
            op = self.current_token
            self.next_token()
            result = (op[0], result, self.factor())
        return result

    def factor(self):
        if self.current_token[0] == "NUMBER":
            value = int(self.current_token[1])
            self.next_token()
            return value
        elif self.current_token[0] == "LPAREN":
            self.next_token()
            result = self.expr()
            if self.current_token[0] != "RPAREN":
                raise SyntaxError("Expected closing parenthesis")
            self.next_token()
            return result
        else:
            raise SyntaxError("Unexpected token")


# Example usage
code = "3 + 5 * (10 - 4)"
tokens = lex(code)
parser = Parser(tokens)
parsed_expr = parser.parse()
print(parsed_expr)
