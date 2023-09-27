import os
from pathlib import Path

DATA = os.path.join(os.getcwd(), "../datasets/")

TRAINING_DATA = os.path.join(DATA, "ml_case_training_data.csv")
TRAINING_HISTORY_DATA = os.path.join(DATA, "ml_case_training_hist_data.csv")
TRAINING_OUTPUT_DATA = os.path.join(DATA, "ml_case_training_output.csv")

TEST_HISTORY = os.path.join(DATA, "ml_case_test_hist_data.csv")
TEST_OUTPUT = os.path.join(DATA, "ml_case_test_output_template.csv")
