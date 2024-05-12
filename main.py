import os
import logging
from datetime import datetime
import chardet
import sys

def get_encoding(file_path):
    with open(file_path, 'rb') as file:
        return chardet.detect(file.read())['encoding']

def is_excluded_ext(file_name: str) -> bool:
    # Checks if a file has an extension that should be excluded from processing.
    file_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg', '.pyc'}
    _, extension = os.path.splitext(file_name)
    return extension.lower() in file_extensions

def append_files_to_project(directory: str = '.', excluded_files: set = None):
    output_dir = '.codestract'
    os.makedirs(output_dir, exist_ok=True)

    if excluded_files is None:
        excluded_files = set()

    total_chars = 0
    file_count = 0
    total_file_size = 0
    skipped_dirs = []
    skipped_files = []

    start_time = datetime.now()
    timestamp = start_time.strftime("%Y%m%d_%H%M%S")
    output_file_name = f"project_export_{timestamp}.txt"
    output_file_path = os.path.join(output_dir, output_file_name)

    try:
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            for root, dirs, files in os.walk(directory):

                # Filter out specific directories to skip
                dirs[:] = [d for d in dirs if d not in {'.git', '.env', '.venv', 'venv', '.idea', '.codestract', '__pycache__'}]
                skipped_dirs.extend([os.path.join(root, d) for d in set(dirs) - set(os.listdir(root))])

                for file in files:
                    if file not in excluded_files and not is_excluded_ext(file):
                        file_path = os.path.join(root, file)
                        try:
                            with open(file_path, 'r', encoding=get_encoding(file_path)) as infile:

                                contents = infile.read()
                                outfile.write(f'# File: {file_path}\n\n')
                                outfile.write(contents)
                                outfile.write("\n\n")
                                total_chars += len(contents)
                                file_count += 1
                                total_file_size += os.path.getsize(file_path)
                        except UnicodeDecodeError:
                            logging.error(f"Skipping file {file_path} due to encoding issues")
                            continue
                    else:
                        skipped_files.append(os.path.join(root, file))

            end_time = datetime.now()
            execution_time = end_time - start_time

            summary = f'Summary:\n'
            summary += f'- Total characters: {total_chars}\n'
            summary += f'- Total files processed: {file_count}\n'
            summary += f'- Total file size: {total_file_size} bytes\n'
            summary += f'- Skipped directories: {len(skipped_dirs)}\n'
            summary += f'- Skipped files: {len(skipped_files)}\n'
            summary += f'- Execution time: {execution_time}\n'

            outfile.write('-' * 40 + '\n')
            outfile.write(summary)
            outfile.write('-' * 40 + '\n')

            logging.info(summary)
            print(summary)

            if skipped_dirs:
                logging.info("Skipped directories:")
                for directory in skipped_dirs:
                    logging.info(directory)
            if skipped_files:
                logging.info("Skipped files:")
                for file in skipped_files:
                    logging.info(file)

        return True
    except Exception as e:
        logging.error(f"Failed to write to {output_file_path}: {e}")
        return False

def setup_logging(log_file_name='logfile.log'):
    output_dir = '.codestract'
    os.makedirs(output_dir, exist_ok=True)
    log_file_path = os.path.join(output_dir, log_file_name)

    # Setup logging to file and console
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # Create handlers
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(log_file_path)
    # Create formatter and add it to handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    # Add handlers to the logger
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)


def main():
    setup_logging()
    # Get the directory path from the command line arguments
    if len(sys.argv) > 1:
        directory_path = sys.argv[1]
    else:
        print("Usage: python main.py <directory_path>")
        sys.exit(1)

    if append_files_to_project(directory=directory_path):
        logging.info("Code base exported successfully.")
    else:
        logging.error("Failed to export code base.")


if __name__ == "__main__":
    main()
