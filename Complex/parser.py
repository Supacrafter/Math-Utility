import PeekableStream

class Parser:
    def __init__(self, tokens, stop_at):
        self.tokens = tokens
        self.stop_at = stop_at

    def fail_if_at_end(self, expected):
        if self.tokens.next is None:
            raise Exception("Hit end of file - expected '%s'." % expected)

    def multiple_expressions(self, sep, end):
        ret = []
        self.fail_if_at_end(end)
        typ = self.tokens.next[0]
        if typ == end:
            self.tokens.move_next()
        else:
            arg_parser = Parser(self.tokens, (sep, end))
            while typ != end:
                p = arg_parser.next_expression(None)
                if p is not None:
                    ret.append(p)
                typ = self.tokens.next[0]
                self.tokens.move_next()
                self.fail_if_at_end(end)
        return ret


    def next_expression(self, prev):
        self.fail_if_at_end(";")
        typ, value = self.tokens.next
        if typ in self.stop_at:
            return prev
        self.tokens.move_next()
        if typ in ("number", "variable") and prev is None:
            return self.next_expression((typ, value))
        elif typ == "wrapper":
            return self.multiple_expressions((typ, value))
        elif typ == "assignment":
            if self.tokens.next == "assignment":
                return self.next_expression((typ, value))
            else:
                pass
        elif typ == "comparison":
            pass
        elif typ == "operator":
            pass
        else:
            raise Exception(
                "Unexpected Token"
            )

        
def parse(tokens_iterator):
  parser = Parser(PeekableStream(tokens_iterator),
    ";")
  while parser.tokens.next is not None:
    p = parser.next_expression(None)
    if p is not None:
      yield p
    parser.tokens.move_next()