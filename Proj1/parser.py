import argparse

parser = argparse.ArgumentParser(
    description="Perform some textual analysis on our directory of cipher texts.\n" +
                "Use with option -v to run with human intervention"
)

parser.add_argument("-v", action='store_true')
