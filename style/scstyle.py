from pygments.lexers.asm import CppLexer
from pygments.lexers.supercollider import SuperColliderLexer
from pygments.token import Name, Keyword


class MDSCLexer(SuperColliderLexer):
    name = 'MDSC'
    aliases = ['mdsc']

    EXTRA_KEYWORDS = ['SinOsc']

    def get_tokens_unprocessed(self, text):
        for index, token, value in SuperColliderLexer.get_tokens_unprocessed(self, text):
            if token is Name and value in self.EXTRA_KEYWORDS:
                yield index, Keyword, value
            else:
                yield index, token, value