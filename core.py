import os 
import hashlib
import json

def scan_directory(directory, mode, progress_callback=None):
    data = {}

    # count total files
    total_files = 0
    for _, _, files in os.walk(directory):
        total_files += len(files)

    processed = 0

    # scan
    for root, dirs, files in os.walk(directory):
        for file in files:
            try:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, directory)

                size = os.path.getsize(full_path)
                entry = {"size": size}

                if mode == "md5":
                    md5 = get_md5(full_path)
                    if md5:
                        entry["hash"] = md5

                data[rel_path] = entry

                processed += 1
                if progress_callback:
                    if total_files > 0:
                        percent = int((processed / total_files) * 100)

                        if percent == 0 and processed > 0:
                            percent = 1
                    else:
                        percent = 100
                    progress_callback(percent, rel_path)

            except Exception:
                continue

    return {
        "type": mode,
        "files": data,
        "total_files": total_files
    }

def get_md5(file_path):
    hash_md5 = hashlib.md5()

    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except:
        return None
    

def save_scan(scan_data, output_file):
    try:

        if not output_file.endswith(".json"):
            output_file += ".json"

        with open(output_file, "w") as f:
            json.dump(scan_data, f, indent=4)

    except Exception:
        return False

    return True


def compare_scans(file1, file2):
    try:
        with open(file1, "r") as f1, open(file2, "r") as f2:
            scan1 = json.load(f1)
            scan2 = json.load(f2)

        files1 = scan1["files"]
        files2 = scan2["files"]

        missing = []
        extra = []
        mismatch = []

        for f in files1:
            if f not in files2:
                missing.append((f, files1[f]["size"]))
            else:
                # size check
                if files1[f]["size"] != files2[f]["size"]:
                    mismatch.append((f, "size mismatch"))

                # hash check
                elif "hash" in files1[f] and "hash" in files2[f]:
                    if files1[f]["hash"] != files2[f]["hash"]:
                        mismatch.append((f, "hash mismatch"))

        for f in files2:
            if f not in files1:
                extra.append((f, files2[f]["size"]))

        return missing, extra, mismatch

    except Exception:
        return None, None, None



