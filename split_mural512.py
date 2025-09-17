#!/usr/bin/env python3
import os
import shutil
import random
from pathlib import Path

def split_mural512_dataset():
    """Split Mural512 images into train/val/visual_test sets"""

    # Set random seed for reproducibility
    random.seed(42)

    # Source and destination paths
    source_dir = Path("Mural512")
    train_dir = Path("mural512_dataset/train")
    val_dir = Path("mural512_dataset/val_source")
    test_dir = Path("mural512_dataset/visual_test_source")
    eval_dir = Path("mural512_dataset/eval_source")

    # Get all PNG files
    png_files = list(source_dir.glob("*.png"))
    print(f"Found {len(png_files)} PNG files in {source_dir}")

    # Shuffle the files
    random.shuffle(png_files)

    # Calculate split indices
    total_files = len(png_files)
    train_count = int(0.8 * total_files)  # 80% for training
    val_count = int(0.1 * total_files)    # 10% for validation
    test_count = int(0.05 * total_files)  # 5% for visual test
    eval_count = total_files - train_count - val_count - test_count  # remaining for eval

    print(f"Splitting into:")
    print(f"  Train: {train_count} images")
    print(f"  Validation: {val_count} images")
    print(f"  Visual test: {test_count} images")
    print(f"  Evaluation: {eval_count} images")

    # Split the files
    train_files = png_files[:train_count]
    val_files = png_files[train_count:train_count + val_count]
    test_files = png_files[train_count + val_count:train_count + val_count + test_count]
    eval_files = png_files[train_count + val_count + test_count:]

    # Copy files to respective directories
    print("Copying files...")

    for i, file_path in enumerate(train_files):
        shutil.copy2(file_path, train_dir / file_path.name)
        if (i + 1) % 500 == 0:
            print(f"  Copied {i + 1}/{len(train_files)} training files")

    for i, file_path in enumerate(val_files):
        shutil.copy2(file_path, val_dir / file_path.name)
        if (i + 1) % 100 == 0:
            print(f"  Copied {i + 1}/{len(val_files)} validation files")

    for i, file_path in enumerate(test_files):
        shutil.copy2(file_path, test_dir / file_path.name)
        if (i + 1) % 100 == 0:
            print(f"  Copied {i + 1}/{len(test_files)} visual test files")

    for i, file_path in enumerate(eval_files):
        shutil.copy2(file_path, eval_dir / file_path.name)
        if (i + 1) % 100 == 0:
            print(f"  Copied {i + 1}/{len(eval_files)} evaluation files")

    print("Data splitting completed!")

    # Verify the splits
    print("\nVerification:")
    print(f"  Train directory: {len(list(train_dir.glob('*.png')))} files")
    print(f"  Val directory: {len(list(val_dir.glob('*.png')))} files")
    print(f"  Visual test directory: {len(list(test_dir.glob('*.png')))} files")
    print(f"  Eval directory: {len(list(eval_dir.glob('*.png')))} files")

if __name__ == "__main__":
    split_mural512_dataset()