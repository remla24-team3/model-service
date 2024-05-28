from lib_ml_group3.load_model import load_model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import random
import re
import pytest
import pandas as pd

INPUT_DIR = "tests/dummy_data/"
OUTPUT_DIR = "tests/dummy_data/"

SENSITIVE_PATTERNS = re.compile(r"(@|token|session|user|userid|"
                                r"password|auth|files|pro)", re.IGNORECASE)

model = load_model(
    "model/model.keras", "model/encoder.pickle", "model/tokenizer.pickle"
)

def read_and_sample_data(file_path, sample_size=100):
    """Read data from a file, sample lines randomly,
    and return the sampled lines."""
    with open(file_path, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines()]
        random.shuffle(lines)
        return lines[:sample_size]

def remove_sensitive_info(text):
    """Remove sensitive information from the text based on
    the SENSITIVE_PATTERNS."""
    return SENSITIVE_PATTERNS.sub("[REDACTED]", text)


@pytest.fixture
def data():
    sample_size = 100  # Set sample size for each file

    train = read_and_sample_data(INPUT_DIR + "sample_train.txt", sample_size)
    val = read_and_sample_data(INPUT_DIR + "sample_val.txt", sample_size)
    test = read_and_sample_data(INPUT_DIR + "sample_test.txt", sample_size)

    # Process train data
    raw_x_train = [remove_sensitive_info(line.split("\t")[1])
                    for line in train]
    raw_y_train = [line.split("\t")[0] for line in train]

    # Process validation data
    raw_x_val = [remove_sensitive_info(line.split("\t")[1]) for line in val]
    raw_y_val = [line.split("\t")[0] for line in val]

    # Process test data
    raw_x_test = [remove_sensitive_info(line.split("\t")[1]) for line in test]
    raw_y_test = [line.split("\t")[0] for line in test]

    return {
            "texts": raw_x_train + raw_x_val + raw_x_test,
            "labels": raw_y_train + raw_y_val + raw_y_test
        }


def test_data_slices(data):
    # Define length thresholds for slicing
    data = pd.DataFrame({'texts': data["texts"], 'labels': data["labels"]})
    short_threshold = 30
    medium_threshold = 50

    # Create slices
    data['text_length'] = data['texts'].apply(len)
    short_texts = data[data['text_length'] <= short_threshold]
    medium_texts = data[(data['text_length'] > short_threshold) & (data['text_length'] <= medium_threshold)]
    long_texts = data[data['text_length'] > medium_threshold]
    assert(len(short_texts["texts"]) == len(short_texts["labels"]))

    y = short_texts['labels']
    short_predictions = model.predict(short_texts['texts'])
    short_accuracy = accuracy_score(y, short_predictions)

    y = medium_texts['labels']
    medium_predictions = model.predict(medium_texts['texts'])
    medium_accuracy = accuracy_score(y, medium_predictions)

    y = long_texts['labels']
    long_predictions = model.predict(long_texts['texts'])
    long_accuracy = accuracy_score(y, long_predictions)

    assert(abs(short_accuracy - medium_accuracy) < 0.25)
    assert(abs(short_accuracy - long_accuracy) < 0.25)
    assert(abs(long_accuracy - medium_accuracy) < 0.25)