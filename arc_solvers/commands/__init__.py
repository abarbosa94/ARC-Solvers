from allennlp.commands import main as main_allennlp


def main(prog: str = None) -> None:
    predictor_overrides = {
        "decomposable_attention": "decompatt",
        "tree_attention": "dgem",
        "bidaf": "bidaf_qa"
    }
    main_allennlp(prog)
