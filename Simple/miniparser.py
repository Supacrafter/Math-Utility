from PeekableStream import PeekableStream

class Parser:
    def __init__(self, tokens, stop_at):
        self.tokens = tokens
        self.stop_at = stop_at

    def next_expresion(self, prev):
        typ, value = self.tokens.next
        if typ in self.stop_at:
            return prev
        
        self.tokens.move_next()
        if typ in ("variable", "number") and prev is None:
            return self.next_expresion((typ, value))
        elif typ == "operator":
            return self.next_expresion((typ, value))
        elif typ == "assignment" and prev is not None:
            return self.next_expresion((typ, value))
        else:
            raise Exception(
                "Unexpected token!: " + typ
            )

def parse(token_iterator):
    parser = Parser(token_iterator, ';')