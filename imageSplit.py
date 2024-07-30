import numpy as np
import shutil
import os

def pathInitialize(model):
    dataset_dir = f'dataset/originData/{model}'
    train_dir = f'dataset/originDateset/train/{model}'
    test_dir = f'dataset/originDateset/test/{model}'
    valid_dir = f'dataset/originDateset/valid/{model}'
    return dataset_dir, train_dir, test_dir, valid_dir

carModel = ['Benz E Class', 'Benz G class', 'BMW i8', 'BMW series 5', 'BMW x6', 'Genesis g80', 'Genesis gv80', 'KIA K5', 'KIA morning', 'MINI cooper']

for car in carModel:
    dataset_dir, train_dir, test_dir, valid_dir = pathInitialize(car)

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)
    os.makedirs(valid_dir, exist_ok=True)

    files = [f for f in os.listdir(dataset_dir) if os.path.isfile(os.path.join(dataset_dir, f))]

    np.random.shuffle(files)

    total_files = len(files)
    train_size = int(total_files * 0.8)
    test_size = int(total_files * 0.1)
    valid_size = total_files - train_size - test_size

    train_files = files[:train_size]
    test_files = files[train_size:train_size + test_size]
    valid_files = files[train_size + test_size:]

    def copy_files(file_list, source_dir, target_dir):
        for file_name in file_list:
            src_file = os.path.join(source_dir, file_name)
            dst_file = os.path.join(target_dir, file_name)
            shutil.copy2(src_file, dst_file)

    copy_files(train_files, dataset_dir, train_dir)
    copy_files(test_files, dataset_dir, test_dir)
    copy_files(valid_files, dataset_dir, valid_dir)

    print(f"Total files: {total_files}")
    print(f"Training files: {len(train_files)}")
    print(f"Testing files: {len(test_files)}")
    print(f"Validation files: {len(valid_files)}")