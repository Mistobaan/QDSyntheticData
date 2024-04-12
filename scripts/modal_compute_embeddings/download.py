from modal import Image, Stub, Volume

# We first set out configuration variables for our script.
DATASET_DIR = "/data"
DATASET_NAME = "gsm8k"
DATASET_CONFIG = "main"


# We define our Modal Resources that we'll need
volume = Volume.from_name("embedding-qd-synth", create_if_missing=True)
image = Image.debian_slim(python_version="3.9").pip_install(
    "datasets==2.16.1", "apache_beam==2.53.0", "hf_transfer"
)
stub = Stub(image=image)


# The default timeout is 5 minutes re: https://modal.com/docs/guide/timeouts#handling-timeouts
#  but we override this to
# 3000s to avoid any potential timeout issues
@stub.function(volumes={DATASET_DIR: volume}, timeout=3000)
def download_dataset():
    # Redownload the dataset
    import time

    from datasets import load_dataset

    start = time.time()
    dataset = load_dataset(DATASET_NAME, DATASET_CONFIG, num_proc=6)
    end = time.time()
    print(f"Download complete - downloaded files in {end-start}s")

    dataset.save_to_disk(f"{DATASET_DIR}/{DATASET_NAME}")
    volume.commit()


@stub.local_entrypoint()
def main():
    download_dataset.remote()