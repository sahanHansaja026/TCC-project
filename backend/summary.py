from sumy.parsers.plaintext import PlaintextParser # type: ignore
from sumy.nlp.tokenizers import Tokenizer # type: ignore
from sumy.summarizers.lsa import LsaSummarizer # type: ignore

def summarize_with_sumy(text:str, sentence_count:int = 5) -> str:
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join(str(sentence) for sentence in summary)